# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    date,
    min_,
    Parameters,
    Period,
    select,
    Variable,
    YEAR
    )
from openfisca_pf.entities import Pays, Personne
from openfisca_pf.enums.impot_foncier import CategoryBien
from openfisca_pf.functions.currency import arrondi_inferieur


class date_de_mise_en_service_installation_photovoltaique(Variable):
    value_type = date
    entity = Personne
    definition_period = YEAR
    default_value = date(1970, 1, 1)
    label = "De de mise en service de installation photovoltaïc"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class date_limite_de_mise_en_service_installation_photovoltaique_pays(Variable):
    value_type = date
    entity = Pays
    definition_period = YEAR
    default_value = date(1970, 1, 1)
    label = "Date limite à partir de laquelle l'installation photovoltaïc peut donner droit à un crédit"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2023(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        anne = parameters(period).dicp.impot_foncier.avantages.credits.photovoltaique.date_limite_de_mise_en_service.annee
        mois = parameters(period).dicp.impot_foncier.avantages.credits.photovoltaique.date_limite_de_mise_en_service.mois
        jour = parameters(period).dicp.impot_foncier.avantages.credits.photovoltaique.date_limite_de_mise_en_service.jour
        return date(anne, mois, jour)  # 2023-01-01


class date_limite_de_mise_en_service_installation_photovoltaique(Variable):
    value_type = date
    entity = Personne
    definition_period = YEAR
    default_value = date(1970, 1, 1)
    label = "Date limite à partir de laquelle l'installation photovoltaïc peut donner droit à un crédit"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2023(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return personne.pays('date_limite_de_mise_en_service_installation_photovoltaique_pays', period, parameters)  # 2023-01-01


class eligible_credit_photovoltaique(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce que le bien est eligible à un crédit d'impôt suite à l'installation de matériel photovoltaïc"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2023(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        categorie = personne('categorie_du_bien', period, parameters)
        habitation_principale = personne('habitation_principale', period, parameters)
        date_limite_de_mise_en_service_installation_photovoltaique = personne('date_limite_de_mise_en_service_installation_photovoltaique', period, parameters)
        date_de_mise_en_service_installation_photovoltaique = personne('date_de_mise_en_service_installation_photovoltaique', period, parameters)
        return (categorie == CategoryBien.LOGEMENT) \
            * habitation_principale \
            * (date_limite_de_mise_en_service_installation_photovoltaique <= date_de_mise_en_service_installation_photovoltaique)


class cout_installation_photovoltaique(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
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

    def formula_2023(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.impot_foncier.avantages.credits.photovoltaique.maximum  # 1 000 000


class maximum_credit_photovoltaique(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant maximum pris en compte pour calculer l'assiette du crédit pour l'installation de matériel photovoltaïc"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2023(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return personne.pays('maximum_credit_photovoltaique_pays', period, parameters)  # 1 000 000


class taux_credit_photovoltaique_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0.
    label = "Taux utilisé pour calculer le montant de base du crédit d'impôt suite à l'installation de matériel photovoltaïc"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2023(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.impot_foncier.avantages.credits.photovoltaique.taux  # 0.3


class taux_credit_photovoltaique(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.
    label = "Taux utilisé pour calculer le montant de base du crédit d'impôt suite à l'installation de matériel photovoltaïc"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2023(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return personne.pays('taux_credit_photovoltaique_pays', period, parameters)  # 0.3


class montant_base_credit_photovoltaique(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant de base du crédit d'impôt suite à l'installation de matériel photovoltaïc"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2023(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        eligible = personne('eligible_credit_photovoltaique', period, parameters)
        cout = personne('cout_installation_photovoltaique', period, parameters)
        maximum = personne('maximum_credit_photovoltaique', period, parameters)
        taux = personne('taux_credit_photovoltaique', period, parameters)

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

    def formula_2023(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        eligible = personne('eligible_credit_photovoltaique', period, parameters)
        reste = personne('reste_credit_photovoltaique', period.offset(-1, 'year'), parameters)
        return select(
            [eligible],
            [reste],
            0
            )


class montant_credit_photovoltaique(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant de crédit d'impôt photovoltaïc imputable"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2023(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        eligible = personne('eligible_credit_photovoltaique', period, parameters)
        brute = personne('impot_foncier_part_pays_brute', period, parameters)
        enveloppe = personne('enveloppe_credit_photovoltaique', period, parameters)

        montant = min_(brute, enveloppe)

        return select(
            [eligible],
            [montant],
            0
            )


class reste_credit_photovoltaique(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Restant de crédit d'impôt photovoltaïc restant après imputation dudis crédit"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2023(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        enveloppe = personne('enveloppe_credit_photovoltaique', period, parameters)
        montant = personne('montant_credit_photovoltaique', period, parameters)
        return enveloppe - montant
