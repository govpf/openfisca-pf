# -*- coding: utf-8 -*-

from openfisca_pf.base import (
    asarray,
    date,
    Enum,
    isin,
    not_,
    Parameters,
    Period,
    select,
    Variable,
    YEAR,
    where
    )
from openfisca_pf.entities import Personne


class TypeLocation(Enum):
    NON_MEUBLE = "NON_MEUBLE"
    MEUBLE = "MEUBLE"
    MEUBLE_DE_TOURISME = "MEUBLE_DE_TOURISME"
    VILLA_DE_LUXE = "VILLA_DE_LUXE"


MEUBLE_OU_NON_MEUBLE = TypeLocation.encode(asarray([
    TypeLocation.NON_MEUBLE,
    TypeLocation.MEUBLE
    ]))


class CategorieDuBien(Enum):
    LOGEMENT = "Logement"
    COMMERCE = "Commerce"
    ADMINISTRATIF = "Administratif"
    ASSOCIATIF = "Associatif"
    PROFESSIONNEL = "Professionnel"
    INDUSTRIEL = "Industriel"
    AGRICOLE = "Agricole"
    MIXTE = "Mixte"
    CULTE = "Culte"
    AUTRE = "Autre"


class categorie(Variable):
    value_type = Enum
    possible_values = CategorieDuBien
    entity = Personne
    definition_period = YEAR
    default_value = CategorieDuBien.LOGEMENT
    label = "Catégorie de la construction"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class loue(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True si le local est loué, False sinon."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class occupation_avant_fin_de_travaux(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True si le local est occupé avant la date de fin de travaux, False sinon."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class habitation_principale(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True si c'est une habitation principale, False sinon."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class non_loue(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = True
    label = "True si le local n'est pas loué, False sinon."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameters):
        loue = local('loue', period, parameters)
        return not_(loue)


class social(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True si le local est un logement social, False sinon."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class non_social(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = True
    label = "True si le local n'est pas un logement social, False sinon."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameters):
        social = local('social', period, parameters)
        return not_(social)


class type_location(Variable):
    value_type = Enum
    possible_values = TypeLocation
    entity = Personne
    definition_period = YEAR
    default_value = TypeLocation.NON_MEUBLE
    label = "Type de location"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class location_simple(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True si le local est loué en meublé ou en non meublé mais pas en meublé de tourisme ni en villa de luxe, False sinon."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameters):
        type_location = local('type_location', period, parameters)
        return isin(type_location, MEUBLE_OU_NON_MEUBLE)


class non_meuble(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True si le local est loué en non-meublé, sinon False."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameters):
        type_location = local('type_location', period, parameters)
        return type_location == TypeLocation.NON_MEUBLE


class meuble(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True si le local est loué en meublé, sinon False."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameters):
        type_location = local('type_location', period, parameters)
        return type_location == TypeLocation.MEUBLE


class villa_de_luxe(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True si le local est loué en villa de luxe, sinon False."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameters):
        type_location = local('type_location', period, parameters)
        return type_location == TypeLocation.VILLA_DE_LUXE


class meuble_de_tourisme(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True si le local est loué en meublé de tourisme (Air B&B par exemple), False sinon."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameters):
        type_location = local('type_location', period, parameters)
        return type_location == TypeLocation.MEUBLE_DE_TOURISME


class date_certificat_conformite(Variable):
    value_type = date
    entity = Personne
    definition_period = YEAR
    default_value = date(2000, 1, 1)
    label = "Date du certificat de conformité"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class date_permis_construire(Variable):
    value_type = date
    entity = Personne
    definition_period = YEAR
    default_value = date(2000, 1, 1)
    label = "Date du permis de construire"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class demande_exemption_temporaire_exceptionnelle(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True le propriétaire a demandé une exemption quinquennale pour le local."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class valeur_venale(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Valeur vénale d'un local"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class loyer_janvier(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Loyer de janvier d'un local"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class valeur_locative_loyers(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Valeur locative calculer grace aux loyers d'un local"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameters):
        loyer_janvier = local('loyer_janvier', period, parameters)
        return loyer_janvier * 12


class valeur_locative_direct(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Valeur locative direct d'un local"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameters):
        valeur_venale = local('valeur_venale', period, parameters)
        taux_archipel = local('taux_archipel', period, parameters)
        return valeur_venale * taux_archipel


class valeur_locative_sociale(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Valeur locative direct d'un local utilisé comme logement social"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameters):
        valeur_venale = local('valeur_venale', period, parameters)
        taux_logement_social = local('taux_logement_social', period, parameters)
        return valeur_venale * taux_logement_social


class valeur_locative_meuble_de_tourisme(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Valeur locative d'un local loué en meuble de tourisme"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameters):
        valeur_venale = local('valeur_venale', period, parameters)
        taux_meuble_de_tourisme = local('taux_meuble_de_tourisme', period, parameters)
        return taux_meuble_de_tourisme * valeur_venale


class valeur_locative_villa_de_luxe(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Valeur locative d'un local loué en villa de luxe"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameters):
        valeur_venale = local('valeur_venale', period, parameters)
        taux_villa_de_luxe = local('taux_villa_de_luxe', period, parameters)
        return taux_villa_de_luxe * valeur_venale


class valeur_locative(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Valeur locative d'un local"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameters):
        # variables conditionnelles
        loue = local('loue', period, parameters)
        non_loue = local('non_loue', period, parameters)
        location_simple = local('location_simple', period, parameters)
        meuble_de_tourisme = local('meuble_de_tourisme', period, parameters)
        villa_de_luxe = local('villa_de_luxe', period, parameters)
        social = local('social', period, parameters)
        # differents calculs de la valeur locative
        valeur_locative_direct = local('valeur_locative_direct', period, parameters)
        valeur_locative_sociale = local('valeur_locative_sociale', period, parameters)
        valeur_locative_loyers = local('valeur_locative_loyers', period, parameters)
        valeur_locative_meuble_de_tourisme = local('valeur_locative_meuble_de_tourisme', period, parameters)
        valeur_locative_villa_de_luxe = local('valeur_locative_villa_de_luxe', period, parameters)
        # on choisit le calcul approprié en fonction des conditions
        return select(
            [loue * location_simple, loue * meuble_de_tourisme, loue * villa_de_luxe, non_loue * social],
            [valeur_locative_loyers, valeur_locative_meuble_de_tourisme, valeur_locative_villa_de_luxe, valeur_locative_sociale],
            valeur_locative_direct
            )


class base_imposable_apres_exemption(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "base de l'impot foncier non finale après l'application de l'exemption temporaire"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameters):
        valeur_locative = local('valeur_locative', period, parameters)
        taux_exemption_temporaire = local('taux_exemption_temporaire', period, parameters)
        exemption_permanente = local('exemption_permanente', period, parameters)
        return where(exemption_permanente, 0, valeur_locative * (1.0 - taux_exemption_temporaire))


class base_imposable_apres_premier_abattement(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "base de l'impot foncier non finale après l'application du première abatement"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameters):
        base_imposable_apres_exemption = local('base_imposable_apres_exemption', period, parameters)
        taux_premier_abattement = local('taux_premier_abattement', period, parameters)
        return base_imposable_apres_exemption * (1.0 - taux_premier_abattement)


class base_imposable(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "base de l'impot foncier utilisé pour calculer la part du territoire et la part comunale"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameters):
        base_imposable_apres_premier_abattement = local('base_imposable_apres_premier_abattement', period, parameters)
        taux_second_abattement = local('taux_second_abattement', period, parameters)
        return base_imposable_apres_premier_abattement * (1.0 - taux_second_abattement)


class contribution_fonciere_part_pays(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant de l'impot foncier allant au territoire"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameters):
        base_imposable = local('base_imposable', period, parameters)
        taux_part_pays = local('taux_part_pays', period, parameters)
        return base_imposable * taux_part_pays


class contribution_fonciere_part_commune(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant de l'impot foncier allant à la commune"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameters):
        contribution_fonciere_part_pays = local('contribution_fonciere_part_pays', period, parameters)
        taux_part_commune_fiscale = local('taux_part_commune_fiscale', period, parameters)
        return contribution_fonciere_part_pays * taux_part_commune_fiscale


class contribution_fonciere(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant total de l'impot foncier"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameters):
        contribution_fonciere_part_pays = local('contribution_fonciere_part_pays', period, parameters)
        contribution_fonciere_part_commune = local('contribution_fonciere_part_commune', period, parameters)
        return contribution_fonciere_part_pays + contribution_fonciere_part_commune


class premier_abattement(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Resultat intermediaire du premier abattement"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameters):
        base_imposable_apres_exemption = local('base_imposable_apres_exemption', period, parameters)
        taux_premier_abattement = local('taux_premier_abattement', period, parameters)
        return base_imposable_apres_exemption * taux_premier_abattement


class second_abattement(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Resultat intermediaire du second abattement"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameters):
        base_imposable_apres_premier_abattement = local('base_imposable_apres_premier_abattement', period, parameters)
        taux_second_abattement = local('taux_second_abattement', period, parameters)
        return base_imposable_apres_premier_abattement * taux_second_abattement


class exemption_temporaire(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Resultat intermediaire de l'exemption temporaire"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameters):
        valeur_locative = local('valeur_locative', period, parameters)
        taux_exemption_temporaire = local('taux_exemption_temporaire', period, parameters)
        return valeur_locative * taux_exemption_temporaire


class exemption_permanente(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True, si le local a le droit a une exemption permanente de l'impôt foncier, sinon False"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameters):
        habitation_principale = local('habitation_principale', period, parameters)
        categorie = local('categorie', period, parameters)
        social = local('social', period, parameters)
        loue = local('loue', period, parameters)
        valeur_venale = local('valeur_venale', period, parameters)
        valeur_venale_maximum_pour_exemption_permanente_pays = local.pays('valeur_venale_maximum_pour_exemption_permanente_pays', period, parameters)
        return (habitation_principale * (valeur_venale <= valeur_venale_maximum_pour_exemption_permanente_pays))\
            + ((categorie == CategorieDuBien.LOGEMENT) * social * loue) \
            + ((categorie == CategorieDuBien.ADMINISTRATIF) * not_(loue)) \
            + ((categorie == CategorieDuBien.CULTE) * not_(loue)) \
            + ((categorie == CategorieDuBien.ASSOCIATIF) * not_(loue))
