# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import Personne
from openfisca_pf.base import (YEAR, Variable)

class is_element_imposition_benefice_imposable(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Bénéfice imposable (C1)"

    def formula(person, period):
        benefice_default = person('is_resultat_fiscal_benefice_apres_report_deficitaire', period)
        return benefice_default


class is_element_imposition_deficit(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Déficit (C2)"

    def formula(person, period):
        deficit_default = person('is_resultat_fiscal_deficit_total', period)
        return deficit_default


class is_element_imposition_zrae_ca(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "CA en Zones de Revitalisation des Activités Economiques (ZRAE)  (CA1)"


class is_element_imposition_ca(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "CA total (CA2)"


class is_element_imposition_calcul_taux(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Taux d’impôt sur les sociétés appliqué (TIS)"


class is_element_imposition_calcul_due(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Montant de l’impôt sur les sociétés ou impôt minimum forfaitaire (C3)"

    def formula(person, period):
        calcul_impot = (person('is_element_imposition_benefice_imposable', period)
            * person('is_element_imposition_calcul_taux', period))
        return calcul_impot


class is_element_imposition_deduction_cas_echeant(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Exonération, réduction ou crédit d’impôt (C4)"


class is_element_imposition_impot_du(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Impôt dû (C5)"

    def formula(person, period):
        impot_du = (person('is_element_imposition_calcul_due', period)
            - person('is_element_imposition_deduction_cas_echeant', period))
        return impot_du


class is_element_imposition_impot_a_payer_accompte_1(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Montant des acomptes déjà versés, 1er Acompte (C6)"


class is_element_imposition_impot_a_payer_accompte_2(Variable):
    value_type = int
    default_value = 0
    entity = Personne
    definition_period = YEAR
    label = "Montant des acomptes déjà versés, 2e Acompte (C7)"


class is_element_imposition_solde_a_payer(Variable):
    value_type = int
    default_value = 0
    entity = Personne
    definition_period = YEAR
    label = "SOLDE A PAYER (C8)"

    def formula(person, period):
        impot_solde = (person('is_element_imposition_impot_du', period)
            - person('is_element_imposition_impot_a_payer_accompte_1', period)
            - person('is_element_imposition_impot_a_payer_accompte_2', period))
        return impot_solde
