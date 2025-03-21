# -*- coding: utf-8 -*-


import numpy
from openfisca_pf.base import (
    ArrayLike,
    date,
    ETERNITY,
    floor_divide,
    full,
    GroupPopulation,
    max_,
    mod,
    min_,
    not_,
    ParameterNode,
    Period,
    Population,
    select,
    Variable,
    YEAR
    )
from openfisca_pf.entities import Pays, Personne
from openfisca_pf.enums.impot_foncier import CategoryBien
from openfisca_pf.functions.currency import arrondi_inferieur
from openfisca_pf.functions.time import annee_de_la_date


class date_de_mise_en_service_installation_photovoltaique(Variable):
    value_type = date
    entity = Personne
    definition_period = ETERNITY
    default_value = date(1970, 1, 1)
    label = "De de mise en service de installation photovoltaïc"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class age_installation_photovoltaique(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Nombre d'année d'impôsition au foncier depuis la mise en service de l'installation photovoltaique"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        date_installation = personne('date_de_mise_en_service_installation_photovoltaique', period)
        return max_(
            period.start.year - annee_de_la_date(date_installation),
            0
            )


class date_limite_de_mise_en_service_installation_photovoltaique_pays(Variable):
    value_type = date
    entity = Pays
    definition_period = YEAR
    default_value = date(1970, 1, 1)
    label = "Date limite à partir de laquelle l'installation photovoltaïc peut donner droit à un crédit"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2023_01_01(pays: GroupPopulation, period: Period, parameters: ParameterNode) -> ArrayLike:
        anne = parameters(period).dicp.impot_foncier.avantages.credits.photovoltaique.date_limite_de_mise_en_service.annee
        mois = parameters(period).dicp.impot_foncier.avantages.credits.photovoltaique.date_limite_de_mise_en_service.mois
        jour = parameters(period).dicp.impot_foncier.avantages.credits.photovoltaique.date_limite_de_mise_en_service.jour
        return full(pays.count, date(anne, mois, jour))  # 2023-01-01


class date_limite_de_mise_en_service_installation_photovoltaique(Variable):
    value_type = date
    entity = Personne
    definition_period = YEAR
    default_value = date(1970, 1, 1)
    label = "Date limite à partir de laquelle l'installation photovoltaïc peut donner droit à un crédit"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2023_01_01(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return personne.pays('date_limite_de_mise_en_service_installation_photovoltaique_pays', period)  # 2023-01-01


class eligible_credit_photovoltaique(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce que le bien est eligible à un crédit d'impôt suite à l'installation de matériel photovoltaïc"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2023_01_01(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        categorie = personne('categorie_du_bien', period)
        habitation_principale = personne('habitation_principale', period)
        date_limite_de_mise_en_service_installation_photovoltaique = personne('date_limite_de_mise_en_service_installation_photovoltaique', period)
        date_de_mise_en_service_installation_photovoltaique = personne('date_de_mise_en_service_installation_photovoltaique', period)
        return (categorie == CategoryBien.LOGEMENT) \
            * habitation_principale \
            * (date_limite_de_mise_en_service_installation_photovoltaique <= date_de_mise_en_service_installation_photovoltaique)


class cout_installation_photovoltaique(Variable):
    value_type = int
    entity = Personne
    definition_period = ETERNITY
    default_value = 0
    label = "Coût totale de l'installation photovoltaïc incluant l'achat du matériel et la pose"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class maximum_credit_photovoltaique_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    default_value = 0
    label = "Montant maximum pris en compte pour calculer l'assiette du crédit pour l'installation de matériel photovoltaïc"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2023_01_01(pays: GroupPopulation, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.impot_foncier.avantages.credits.photovoltaique.maximum  # 1 000 000


class maximum_credit_photovoltaique(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant maximum pris en compte pour calculer l'assiette du crédit pour l'installation de matériel photovoltaïc"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2023_01_01(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return personne.pays('maximum_credit_photovoltaique_pays', period)  # 1 000 000


class taux_credit_photovoltaique_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0.
    label = "Taux utilisé pour calculer le montant de base du crédit d'impôt suite à l'installation de matériel photovoltaïc"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2023_01_01(pays: GroupPopulation, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.impot_foncier.avantages.credits.photovoltaique.taux  # 0.3


class taux_credit_photovoltaique(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.
    label = "Taux utilisé pour calculer le montant de base du crédit d'impôt suite à l'installation de matériel photovoltaïc"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2023_01_01(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return personne.pays('taux_credit_photovoltaique_pays', period)  # 0.3


class montant_base_credit_photovoltaique(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant de base du crédit d'impôt suite à l'installation de matériel photovoltaïc"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2023_01_01(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        eligible = personne('eligible_credit_photovoltaique', period)
        cout = personne('cout_installation_photovoltaique', period)
        maximum = personne('maximum_credit_photovoltaique', period)
        taux = personne('taux_credit_photovoltaique', period,)

        base = arrondi_inferieur(min_(cout, maximum) * taux)

        return select(
            [eligible],
            [base],
            0
            )


class enveloppe_credit_photovoltaique(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Envelope de crédit d'impôt photovoltaïc disponible pour imputation"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2023_01_01(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        age = personne('age_installation_photovoltaique', period)
        eligible = personne('eligible_credit_photovoltaique', period)
        enveloppe = numpy.zeros_like(age)
        for i in range(age.size):
            if age[i] == 1:
                enveloppe[i] = personne('montant_base_credit_photovoltaique', period)
            elif age[i] > 1:
                enveloppe[i] = personne('reste_credit_photovoltaique', period.last_year)
        return select(
            [eligible],
            [enveloppe],
            0
            )


class credit_photovoltaique_applique(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce que le crédit d'impôt suite à l'installation de matériel photovoltaïc s'applique au bien"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2023_01_01(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        exoneration_permanente = personne('exoneration_permanente_appliquee', period)
        exoneration_temporaire = personne('exoneration_temporaire_appliquee', period)
        eligible = personne('eligible_credit_photovoltaique', period)

        # Pour le que le crédit puisse s'appliquer, il faut que :
        # – Le bien ne bénéficie pas d'une exonération permanente.
        # – Le bien ne bénéficie pas d'une exonération temporaire.
        # – Le bien soit éligible au crédit photovoltaïque.
        return not_(exoneration_permanente) \
            * not_(exoneration_temporaire) \
            * eligible


class credit_photovoltaique_eligible_et_applique(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce que le crédit d'impôt suite à l'installation de matériel photovoltaïc s'applique au bien"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2023_01_01(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        eligible = personne('eligible_credit_photovoltaique', period)
        applique = personne('credit_photovoltaique_applique', period)
        return eligible * applique


class montant_credit_photovoltaique(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant de crédit d'impôt photovoltaïc imputable"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2023_01_01(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        eligible_et_applique = personne('credit_photovoltaique_eligible_et_applique', period)
        impot = personne('impot_foncier_part_pays_apres_exonerations_temporaires', period)
        enveloppe = personne('enveloppe_credit_photovoltaique', period)
        return select(
            [eligible_et_applique],
            [min_(impot, enveloppe)],
            0
            )


class reste_credit_photovoltaique(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Restant de crédit d'impôt photovoltaïc restant après imputation dudis crédit"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2023_01_01(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        enveloppe = personne('enveloppe_credit_photovoltaique', period)
        montant = personne('montant_credit_photovoltaique', period)
        return enveloppe - montant


class duree_credit_photovoltaique(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Durée d'imputation du crédit photovoltaïque calculé à partir de montant brute de l'impôt foncier part pays et du montant de base du crédit photovoltaïque"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2023_01_01(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        impot_brut = personne('impot_foncier_part_pays_brute', period).astype(numpy.float64)
        base = personne('montant_base_credit_photovoltaique', period).astype(numpy.float64)

        positif = base > 0
        duree = floor_divide(impot_brut, base, where = positif) \
            + (mod(impot_brut, base, where = positif) > 0)

        return select(
            positif,
            [duree],
            0
            )


# ##################################################
# ###             APPLICATION CREITS             ###
# ##################################################


class eligible_credit(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce que le bien est eligible à un crédit d'impôt foncier"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return False

    def formula_2023_01_01(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return personne('eligible_credit_photovoltaique', period)


class credit_applique(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce le bien est éligible à un crédit d'impôt foncier et ce crédit s'applique au bien"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return False

    def formula_2023_01_01(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return personne('credit_photovoltaique_eligible_et_applique', period)


class montant_credit(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Somme des montant des crédits d'impôt foncier s'appliquant au bien"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        montant_credit_photovoltaique = personne('montant_credit_photovoltaique', period)
        return montant_credit_photovoltaique
