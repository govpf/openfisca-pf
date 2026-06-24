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


class is_resultat_fiscal_reintegrations_benefice_net_comptable(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Bénéfice net comptable (A1.1)"


class is_resultat_fiscal_deductions_perte_nette_comptable(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Perte nette comptable (A1.2)"


class is_resultat_fiscal_reintegrations_contribution_supplementaire(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Contribution supplémentaire à l’IS (A2)"


class is_resultat_fiscal_reintegrations_impot_sur_les_societes(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Impôt sur les sociétés (A3)"


class is_resultat_fiscal_reintegrations_amortissements_non_deductibles(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Amortissements non déductibles (A4)"


class is_resultat_fiscal_reintegrations_interets_non_deductibles(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Intérêts non déductibles (A5)"


class is_resultat_fiscal_reintegrations_renumerations_non_deductibles(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Rémunérations non déductible (A6)"


class is_resultat_fiscal_reintegrations_provisions_non_deductibles(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Provisions non déductibles (A7)"


# Prêts et autres immobilisations financières
class is_resultat_fiscal_reintegrations_amortissements_reputes_differes(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Amortissements réputés différés (A8)"


class is_resultat_fiscal_reintegrations_depenses_relatives_au_logement_du_personnel(Variable):
    value_type = int
    default_value = 0
    entity = Personne
    definition_period = DAY
    label = "Dépenses relatives au logement du personne (A9)"


class is_resultat_fiscal_reintegrations_autres(Variable):
    value_type = int
    default_value = 0
    entity = Personne
    definition_period = DAY
    label = "Autres réintégrations (A10)"


class is_resultat_fiscal_reintegrations_total(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Total réintégrations (A11)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return personne('is_resultat_fiscal_reintegrations_benefice_net_comptable', period) \
            + personne('is_resultat_fiscal_reintegrations_contribution_supplementaire', period) \
            + personne('is_resultat_fiscal_reintegrations_impot_sur_les_societes', period) \
            + personne('is_resultat_fiscal_reintegrations_amortissements_non_deductibles', period) \
            + personne('is_resultat_fiscal_reintegrations_interets_non_deductibles', period) \
            + personne('is_resultat_fiscal_reintegrations_renumerations_non_deductibles', period) \
            + personne('is_resultat_fiscal_reintegrations_provisions_non_deductibles', period) \
            + personne('is_resultat_fiscal_reintegrations_amortissements_reputes_differes', period) \
            + personne('is_resultat_fiscal_reintegrations_depenses_relatives_au_logement_du_personnel', period) \
            + personne('is_resultat_fiscal_reintegrations_autres', period)


class is_resultat_fiscal_deductions_plus_values_non_imposables(Variable):
    value_type = int
    default_value = 0
    entity = Personne
    definition_period = DAY
    label = "Plus-values non imposables (A12)"


class is_resultat_fiscal_deductions_plus_values_exonerees_sous_conditions_de_remploi(Variable):
    value_type = int
    default_value = 0
    entity = Personne
    definition_period = DAY
    label = "Plus-values exonérées sous conditions de remploi (A13)"


class is_resultat_fiscal_deductions_revenu_net_valeurs_et_capitaux_mobiliers(Variable):
    value_type = int
    default_value = 0
    entity = Personne
    definition_period = DAY
    label = "Revenu net des valeurs et capitaux mobiliers (A14)"


class is_resultat_fiscal_deductions_autres(Variable):
    value_type = int
    default_value = 0
    entity = Personne
    definition_period = DAY
    label = "Autres déductions (A15)"


class is_resultat_fiscal_deductions_total(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Total déductions (A16)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return personne('is_resultat_fiscal_deductions_perte_nette_comptable', period) \
            + personne('is_resultat_fiscal_deductions_plus_values_non_imposables', period) \
            + personne('is_resultat_fiscal_deductions_plus_values_exonerees_sous_conditions_de_remploi', period) \
            + personne('is_resultat_fiscal_deductions_revenu_net_valeurs_et_capitaux_mobiliers', period) \
            + personne('is_resultat_fiscal_deductions_autres', period)


class is_resultat_fiscal_benefice_avant_report_deficitaire(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Bénéfice avant report déficitaire (B1)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        benefice = personne('is_resultat_fiscal_reintegrations_total', period) \
            - personne('is_resultat_fiscal_deductions_total', period)
        return benefice * (benefice > 0)


class is_resultat_fiscal_deficit_total(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Déficit (B2)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        deficit = personne('is_resultat_fiscal_deductions_total', period) \
            - personne('is_resultat_fiscal_reintegrations_total', period)
        return deficit * (deficit > 0)


class is_resultat_fiscal_montant_deficits_anterieurs_reportables_effectivement_imputes(Variable):
    value_type = int
    default_value = 0
    entity = Personne
    definition_period = DAY
    label = "Montant des déficits antérieurs reportables effectivement imputés (B3)"


class is_resultat_fiscal_montant_amortissements_anterieurs_reportables_effectivement_imputes(Variable):
    value_type = int
    default_value = 0
    entity = Personne
    definition_period = DAY
    label = "Montant des amortissements antérieurs réputés différés effectivement imputés (B4)"


class is_resultat_fiscal_benefice_apres_report_deficitaire(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Bénéfice après report déficitaire (B5)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        benefice = personne('is_resultat_fiscal_benefice_avant_report_deficitaire', period) \
            - personne('is_resultat_fiscal_montant_deficits_anterieurs_reportables_effectivement_imputes', period) \
            - personne('is_resultat_fiscal_montant_amortissements_anterieurs_reportables_effectivement_imputes', period)
        return benefice * (benefice > 0)


class is_resultat_fiscal_montant_deficits_restant_a_imputer(Variable):
    value_type = int
    default_value = 0
    entity = Personne
    definition_period = DAY
    label = "Montant des déficits restant à imputer (B6)"


class is_resultat_fiscal_amortissements_reputes_differes_restant_a_imputer(Variable):
    value_type = int
    default_value = 0
    entity = Personne
    definition_period = DAY
    label = "Amortissements réputés différés restant à imputer (B7)"
