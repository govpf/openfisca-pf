# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    Enum,
    isin,
    not_,
    Parameters,
    Period,
    select,
    Variable,
    YEAR
)
from openfisca_pf.constants.time import NOMBRE_DE_MOIS_PAR_AN
from openfisca_pf.entities import Pays, Personne
from openfisca_pf.enums.geographie import Archipel
from openfisca_pf.functions.enum import enum_set


class TypeLocation(Enum):
    NON_MEUBLE = "NON_MEUBLE"
    MEUBLE = "MEUBLE"
    MEUBLE_DE_TOURISME = "MEUBLE_DE_TOURISME"
    VILLA_DE_LUXE = "VILLA_DE_LUXE"


MEUBLE_OU_NON_MEUBLE = enum_set(
    TypeLocation,
    TypeLocation.NON_MEUBLE,
    TypeLocation.MEUBLE
)


class loue(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True si le bien est loué, False sinon."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class non_loue(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = True
    label = "True si le bien n'est pas loué, False sinon."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        loue = personne('loue', period, parameters)
        return not_(loue)


class logement_social(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True si le bien est un logement social, False sinon."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class logement_non_social(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = True
    label = "True si le bien n'est pas un logement social, False sinon."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        logement_social = personne('logement_social', period, parameters)
        return not_(logement_social)


class type_de_location(Variable):
    value_type = Enum
    possible_values = TypeLocation
    entity = Personne
    definition_period = YEAR
    default_value = TypeLocation.NON_MEUBLE
    label = "Type de location qui est faite du bien immobilier"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class location_simple(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True si le bien est loué en meublé ou en non meublé mais pas en meublé de tourisme ni en villa de luxe, False sinon."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        loue = personne('loue', period, parameters)
        type_de_location = personne('type_de_location', period, parameters)
        return loue * isin(type_de_location, MEUBLE_OU_NON_MEUBLE)


class location_non_meuble(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True si le bien est loué en non-meublé, False sinon."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(personne: Personne, period: Period, parameters: Parameters):
        loue = personne('loue', period, parameters)
        type_de_location = personne('type_de_location', period, parameters)
        return loue * (type_de_location == TypeLocation.NON_MEUBLE)


class location_meuble(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True si le bien est loué en meublé, False sinon."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        loue = personne('loue', period, parameters)
        type_de_location = personne('type_de_location', period, parameters)
        return loue * (type_de_location == TypeLocation.MEUBLE)


class location_meuble_de_tourisme(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True si le bien est loué en meublé de tourisme (Air B&B par exemple), False sinon."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        loue = personne('loue', period, parameters)
        type_de_location = personne('type_de_location', period, parameters)
        return loue * (type_de_location == TypeLocation.MEUBLE_DE_TOURISME)


class location_villa_de_luxe(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True si le bien est loué en villa de luxe, False sinon."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        loue = personne('loue', period, parameters)
        type_de_location = personne('type_de_location', period, parameters)
        return loue * (type_de_location == TypeLocation.VILLA_DE_LUXE)


class loyer_de_janvier(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Loyer de janvier percu pour la location bien immobilier"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class valeur_locative_loyers(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Valeur locative calculer grace au loyer perçut pour la location du bien immobilier au mois de janvier"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        loyer_de_janvier = personne('loyer_de_janvier', period, parameters)
        return loyer_de_janvier * NOMBRE_DE_MOIS_PAR_AN


class taux_archipel_australes_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0.
    label = "Taux permettant de calculer la valeur locative direct en fonction de la valeur venale et de l'archipel des Australes"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2001_11_13(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.impot_foncier.assiette.taux.archipel.autres # 0.03

    def formula_2011_09_27(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.impot_foncier.assiette.taux.archipel.australes # 0.02


class taux_archipel_gambiers_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0.
    label = "Taux permettant de calculer la valeur locative direct en fonction de la valeur venale et des archipels des Gambiers"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2001_11_13(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.impot_foncier.assiette.taux.archipel.autres # 0.03

    def formula_2011_09_27(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.impot_foncier.assiette.taux.archipel.gambiers # 0.02


class taux_archipel_iles_du_vent_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0.
    label = "Taux permettant de calculer la valeur locative direct en fonction de la valeur venale et de l'archipel des Îles du vent"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2001_11_13(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.impot_foncier.assiette.taux.archipel.iles_du_vent # 0.04


class taux_archipel_iles_sous_le_vent_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0.
    label = "Taux permettant de calculer la valeur locative direct en fonction de la valeur venale et de l'archipel des Îles sous le vent"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2001_11_13(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.impot_foncier.assiette.taux.archipel.autres # 0.03

    def formula_2011_09_27(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.impot_foncier.assiette.taux.archipel.iles_sous_le_vent # 0.03


class taux_archipel_marquises_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0.
    label = "Taux permettant de calculer la valeur locative direct en fonction de la valeur venale et de l'archipel des Marquises"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2001_11_13(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.impot_foncier.assiette.taux.archipel.autres # 0.03

    def formula_2011_09_27(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.impot_foncier.assiette.taux.archipel.marquises # 0.02


class taux_archipel_tuamotus_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0.
    label = "Taux permettant de calculer la valeur locative direct en fonction de la valeur venale et des archipels des Touamotus"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2001_11_13(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.impot_foncier.assiette.taux.archipel.autres # 0.03

    def formula_2011_09_27(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.impot_foncier.assiette.taux.archipel.tuamotus # 0.02


class taux_archipel_australes(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.
    label = "Taux permettant de calculer la valeur locative direct d'un bien en fonction de la valeur venale et de l'archipel des Australes"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return personne.pays('taux_archipel_australes_pays', period, parameters)


class taux_archipel_gambiers(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.
    label = "Taux permettant de calculer la valeur locative direct d'un bien en fonction de la valeur venale et des archipels des Gambiers"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return personne.pays('taux_archipel_gambiers_pays', period, parameters)


class taux_archipel_iles_du_vent(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.
    label = "Taux permettant de calculer la valeur locative direct d'un bien en fonction de la valeur venale et de l'archipel des Îles du vent"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return personne.pays('taux_archipel_iles_du_vent_pays', period, parameters)


class taux_archipel_iles_sous_le_vent(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.
    label = "Taux permettant de calculer la valeur locative direct d'un bien en fonction de la valeur venale et de l'archipel des Îles sous le vent"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return personne.pays('taux_archipel_iles_sous_le_vent_pays', period, parameters)


class taux_archipel_marquises(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.
    label = "Taux permettant de calculer la valeur locative direct d'un bien en fonction de la valeur venale et de l'archipel des Marquises"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return personne.pays('taux_archipel_marquises_pays', period, parameters)


class taux_archipel_tuamotus(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.
    label = "Taux permettant de calculer la valeur locative direct d'un bien en fonction de la valeur venale et des archipels des Touamotus"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return personne.pays('taux_archipel_tuamotus_pays', period, parameters)


class taux_archipel(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Taux permettant de calculer la valeur locative direct d'un bien en fonction de la valeur venale et de l'archipel du local"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        archipel = personne('archipel', period, parameters)
        taux_archipel_australes = personne('taux_archipel_australes', period, parameters)
        taux_archipel_gambiers = personne('taux_archipel_gambiers', period, parameters)
        taux_archipel_iles_du_vent = personne('taux_archipel_iles_du_vent', period, parameters)
        taux_archipel_iles_sous_le_vent = personne('taux_archipel_iles_sous_le_vent', period, parameters)
        taux_archipel_marquises = personne('taux_archipel_marquises', period, parameters)
        taux_archipel_tuamotus = personne('taux_archipel_tuamotus', period, parameters)
        return select([
            archipel == Archipel.AUSTRALES,
            archipel == Archipel.GAMBIERS,
            archipel == Archipel.ILES_DU_VENT,
            archipel == Archipel.ILES_SOUS_LE_VENT,
            archipel == Archipel.MARQUISES,
            archipel == Archipel.TUAMOTUS
        ], [
            taux_archipel_australes,
            taux_archipel_gambiers,
            taux_archipel_iles_du_vent,
            taux_archipel_iles_sous_le_vent,
            taux_archipel_marquises,
            taux_archipel_tuamotus
        ])


class valeur_venale(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Valeur vénale du bien immobilier"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class valeur_locative_direct(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Valeur locative direct d'un bien immobilier calculer grace à la valeur vénale et le taux archipel"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        valeur_venale = personne('valeur_venale', period, parameters)
        taux_archipel = personne('taux_archipel', period, parameters)
        return valeur_venale * taux_archipel


class taux_logement_social_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0.
    label = "Taux permettant de calculer la valeur locative direct d'un logement social"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2001_11_13(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.impot_foncier.assiette.taux.logement_social # 0.02


class taux_logement_social(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.
    label = "Taux permettant de calculer la valeur locative d'un logement social"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return personne.pays('taux_logement_social_pays', period, parameters)


class valeur_locative_sociale(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Valeur locative direct d'un logement social possédée et occupée par le propriétaire. Et non pas loué par l'OPH."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        valeur_venale = personne('valeur_venale', period, parameters)
        taux_logement_social = personne('taux_logement_social', period, parameters)
        return valeur_venale * taux_logement_social


class taux_meuble_de_tourisme_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0.
    label = "Taux permettant de calculer la valeur locative d'un bien loué en meuble de tourisme en fonction de sa valeur vénale"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    # TODO HISTORIQUE DES TAUX
    def formula_1970_01_01(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.impot_foncier.assiette.taux.meuble_de_tourisme


class taux_meuble_de_tourisme(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.
    label = "Taux permettant de calculer la valeur locative d'un bien loué en meuble de tourisme en fonction de sa valeur vénale"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return personne.pays('taux_meuble_de_tourisme_pays', period, parameters)


class valeur_locative_meuble_de_tourisme(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Valeur locative d'un bien loué en meuble de tourisme"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        valeur_venale = personne('valeur_venale', period, parameters)
        taux_meuble_de_tourisme = personne('taux_meuble_de_tourisme', period, parameters)
        return taux_meuble_de_tourisme * valeur_venale


class taux_villa_de_luxe_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0.
    label = "Taux permettant de calculer la valeur locative d'un loué loué en villa de luxe en fonction de sa valeur vénale"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    # TODO HISTORIQUE DES TAUX
    def formula_1970_01_01(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.impot_foncier.assiette.taux.villa_de_luxe


class taux_villa_de_luxe(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.
    label = "Taux permettant de calculer la valeur locative d'un loué loué en villa de luxe en fonction de sa valeur vénale"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return personne.pays('taux_villa_de_luxe_pays', period, parameters)


class valeur_locative_villa_de_luxe(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Valeur locative d'un bien loué en villa de luxe"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        valeur_venale = personne('valeur_venale', period, parameters)
        taux_villa_de_luxe = personne('taux_villa_de_luxe', period, parameters)
        return taux_villa_de_luxe * valeur_venale


class valeur_locative_brute(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Valeur locative d'un bien immobilier"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        # Variables utilisé comme conditions
        location_simple = personne('location_simple', period, parameters)
        location_meuble_de_tourisme = personne('location_meuble_de_tourisme', period, parameters)
        location_villa_de_luxe = personne('location_villa_de_luxe', period, parameters)
        logement_social = personne('logement_social', period, parameters)

        # Differents calculs de la valeur locative
        valeur_locative_loyers = personne('valeur_locative_loyers', period, parameters)
        valeur_locative_direct = personne('valeur_locative_direct', period, parameters)
        valeur_locative_sociale = personne('valeur_locative_sociale', period, parameters)
        valeur_locative_meuble_de_tourisme = personne('valeur_locative_meuble_de_tourisme', period, parameters)
        valeur_locative_villa_de_luxe = personne('valeur_locative_villa_de_luxe', period, parameters)

        # On choisit le calcul approprié en fonction de la situation du bien immobilier
        return select(
            [
                location_simple,
                location_meuble_de_tourisme,
                location_villa_de_luxe,
                logement_social
            ],
            [
                valeur_locative_loyers,
                valeur_locative_meuble_de_tourisme,
                valeur_locative_villa_de_luxe,
                valeur_locative_sociale
            ],
            valeur_locative_direct
        )
