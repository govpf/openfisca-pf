# -*- coding: utf-8 -*-


from fractions import Fraction
from openfisca_pf.base import (
    ArrayLike,
    DAY,
    Enum,
    Parameters,
    Period,
    select,
    Variable
    )
from openfisca_pf.entities import Personne
from openfisca_pf.enums.rch import (
    TypeAcheteur,
    TypeBien,
    TypeDemarche,
    TypeParente
    )
from openfisca_pf.functions.currency import arrondi_superieur


class type_demarche_rch(Variable):
    value_type = Enum
    possible_values = TypeDemarche
    default_value = TypeDemarche.Acquisition
    entity = Personne
    definition_period = DAY
    label = "Type de démarche auprès de la RCH"


class type_acheteur_rch(Variable):
    value_type = Enum
    possible_values = TypeAcheteur
    default_value = TypeAcheteur.DroitCommun
    entity = Personne
    definition_period = DAY
    label = "Type d'acheteur"


class type_parente_rch(Variable):
    value_type = Enum
    possible_values = TypeParente
    default_value = TypeParente.NonParent
    entity = Personne
    definition_period = DAY
    label = "Type d'acheteur"


class type_bien_rch(Variable):
    value_type = Enum
    possible_values = TypeBien
    default_value = TypeBien.TerrainNu
    entity = Personne
    definition_period = DAY
    label = "Type de bien"


class valeur_totale_bien_achat(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Valeur totale du bien à l'achat"


class valeur_totale_bien_vente(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Valeur totale du bien à la revente"


class valeur_locative_bien(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Valeur totale de location par mois"


class duree_bail_mois(Variable):
    value_type = int
    entity = Personne
    default_value = 3
    definition_period = DAY
    label = "Durée du bail en mois"


class valeur_plus_value_net(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Valeur de la plus-value immobilière nette"


class duree_possession_annee(Variable):
    value_type = int
    entity = Personne
    default_value = 3
    definition_period = DAY
    label = "Durée de possession en année"


class montant_droit_enregistrement(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Montant des droits d'enregistrement"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=521011&idr=208&np=1"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:

        def acquisition_formula():
            """
            Formule qui s'applique dans le cas d'une acquisision.
            """
            type_acheteur_rch = personne('type_acheteur_rch', period, parameters)
            type_bien_rch = personne('type_bien_rch', period, parameters)
            valeur_totale_bien_achat = personne('valeur_totale_bien_achat', period, parameters)
            return select(
                [
                    (type_acheteur_rch == TypeAcheteur.DroitCommun),
                    (type_acheteur_rch == TypeAcheteur.PrimoAcquereur) * (type_bien_rch == TypeBien.TerrainNu),
                    (type_acheteur_rch == TypeAcheteur.PrimoAcquereur) * (type_bien_rch != TypeBien.TerrainNu)
                    ],
                [
                    parameters(period).daf.rch.droit_enregistrement.droit_commun.calc(valeur_totale_bien_achat),
                    parameters(period).daf.rch.droit_enregistrement.primo_acquereur_terrain_nu.calc(valeur_totale_bien_achat),
                    parameters(period).daf.rch.droit_enregistrement.primo_acquereur_terrain_bati.calc(valeur_totale_bien_achat)
                    ]
                )

        def navire_formula():
            """
            Formule qui s'applique dans le cas de la session d'un navire.
            """
            valeur_totale_bien_achat = personne('valeur_totale_bien_achat', period, parameters)
            scale = parameters(period).daf.rch.droit_enregistrement.vente_navire
            return scale.calc(valeur_totale_bien_achat)

        def baux_formula():
            """
            Formule qui s'applique dans le cas d'une prise de bail.
            """
            valeur_totale_bien_achat = personne('valeur_locative_bien', period, parameters)
            duree_bail_mois = personne('duree_bail_mois', period, parameters)
            scale = parameters(period).daf.rch.droit_enregistrement.baux
            rate = scale.calc(duree_bail_mois)
            return valeur_totale_bien_achat * duree_bail_mois * rate

        # On recupère le type de démarche
        type_demarche = personne('type_demarche_rch', period, parameters)

        # On applique la formule qui correspond au type de la démarche
        montant_droit_enregistrement = select(
            [
                (type_demarche == TypeDemarche.Acquisition),
                (type_demarche == TypeDemarche.Baux),
                (type_demarche == TypeDemarche.Navire)
                ],
            [
                acquisition_formula(),
                baux_formula(),
                navire_formula()
                ]
            )
        return arrondi_superieur(montant_droit_enregistrement)


class montant_taxe_publicite(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Montant de la taxe de publicité immobilière"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=521011&idr=208&np=1"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:

        def acquisition_formula():
            """
            Formule qui s'applique dans le cas d'une acquisision.
            """
            valeur_totale_bien_achat = personne('valeur_totale_bien_achat', period, parameters)
            # Ici on converti la valeur florante en fraction pour eviter des erreurs de précision numérique
            # https://docs.python.org/3/tutorial/floatingpoint.html
            rate = Fraction.from_float(parameters(period).daf.rch.taxe_publicite_immobiliere.acquisition.rate)
            return valeur_totale_bien_achat * rate

        def baux_formula():
            """
            Formule qui s'applique dans le cas de la session d'un navire.
            """
            valeur_locative_bien = personne('valeur_locative_bien', period, parameters)
            duree_bail_mois = personne('duree_bail_mois', period, parameters)
            rate = parameters(period).daf.rch.taxe_publicite_immobiliere.baux.calc(duree_bail_mois)
            return arrondi_superieur(valeur_locative_bien * duree_bail_mois * rate)

        # On recupère le type de démarche
        type_demarche = personne('type_demarche_rch', period, parameters)

        # On applique la formule qui correspond au type de la démarche
        return select(
            [
                type_demarche == TypeDemarche.Acquisition,
                type_demarche == TypeDemarche.Baux
                ],
            [
                acquisition_formula(),
                baux_formula()
                ]
            )


class montant_taxe_plus_value(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Montant de la taxe sur la plus-value immobilière"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=521011&idr=208&np=1"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        valeur_plus_value_net = personne('valeur_plus_value_net', period, parameters)
        duree_possession_annee = personne('duree_possession_annee', period, parameters)
        rate = parameters(period).daf.rch.plus_values_immobiliere.calc(duree_possession_annee)
        return arrondi_superieur(valeur_plus_value_net * rate)
