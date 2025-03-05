# -*- coding: utf-8 -*-


from openfisca_pf.base import (
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
