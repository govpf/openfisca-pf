# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.base import (
    ArrayLike,
    DAY,
    ParameterNode,
    Period,
    Population,
    Variable
    )
from openfisca_pf.entities import Personne


class is_element_imposition_benefice_imposable(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Bénéfice imposable (C1)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        benefice_default = personne('is_resultat_fiscal_benefice_apres_report_deficitaire', period)
        return benefice_default


class is_element_imposition_deficit(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Déficit (C2)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        deficit_default = personne('is_resultat_fiscal_deficit_total', period)
        return deficit_default


class is_element_imposition_zrae_ca(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "CA en Zones de Revitalisation des Activités Economiques (ZRAE)  (CA1)"


class is_element_imposition_ca(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "CA total (CA2)"


class is_element_imposition_calcul_taux(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Taux d’impôt sur les sociétés appliqué (TIS)"


class is_element_imposition_calcul_due(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Montant de l’impôt sur les sociétés ou impôt minimum forfaitaire (C3)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return personne('is_element_imposition_benefice_imposable', period) \
            * personne('is_element_imposition_calcul_taux', period)


class is_element_imposition_deduction_cas_echeant(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Exonération, réduction ou crédit d’impôt (C4)"


class is_element_imposition_impot_du(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Impôt dû (C5)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return personne('is_element_imposition_calcul_due', period) \
            - personne('is_element_imposition_deduction_cas_echeant', period)


class is_element_imposition_impot_a_payer_accompte_1(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Montant des acomptes déjà versés, 1er Acompte (C6)"


class is_element_imposition_impot_a_payer_accompte_2(Variable):
    value_type = int
    default_value = 0
    entity = Personne
    definition_period = DAY
    label = "Montant des acomptes déjà versés, 2e Acompte (C7)"


class is_element_imposition_solde_a_payer(Variable):
    value_type = int
    default_value = 0
    entity = Personne
    definition_period = DAY
    label = "SOLDE A PAYER (C8)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return personne('is_element_imposition_impot_du', period) \
            - personne('is_element_imposition_impot_a_payer_accompte_1', period) \
            - personne('is_element_imposition_impot_a_payer_accompte_2', period)
