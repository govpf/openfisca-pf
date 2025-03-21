# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    MONTH,
    ParameterNode,
    Period,
    Population,
    set_input_divide_by_period,
    Variable
    )
from openfisca_pf.constants import units
from openfisca_pf.entities import Personne


class base_imposable_tva_taux_reduit(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = 'Base imposable de la TVA à taux réduit'
    unit = units.XPF
    reference = 'https://www.impot-polynesie.gov.pf/code/3-chap-iii-taux'


class base_imposable_tva_taux_intermediaire(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = 'Base imposable de la TVA à taux intermediaire'
    unit = units.XPF
    reference = 'https://www.impot-polynesie.gov.pf/code/3-chap-iii-taux'


class base_imposable_tva_taux_normal(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = 'Base imposable de la TVA à taux normal'
    unit = units.XPF
    reference = 'https://www.impot-polynesie.gov.pf/code/3-chap-iii-taux'


class base_imposable_tva_taux_livraisons_immeubles_et_cession_parts(Variable):
    value_type = float
    default_value = 0
    entity = Personne
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = "Base imposable de la TVA à taux des livraisons d'immeubles et de cession de parts"
    unit = units.XPF


class montant_ventes_hors_taxes(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = 'Montant des ventes réalisées, hors taxes'
    unit = units.XPF


class montant_prestations_services_hors_taxes(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = 'Montant des prestations de dervices réalisées, hors taxes'
    unit = units.XPF


class montant_exportations_non_taxables(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = 'Montant des exportations, qui ne sont pas taxables, et qui ne sont pas prises en compte dans les calculs de la TVA.'
    unit = units.XPF


class montant_autres_operations_non_taxables(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = 'Montant des autres opérations qui ne sont pas taxables, et qui ne sont pas prises en compte dans les calculs de la TVA.'
    unit = units.XPF


class sous_total_base_imposable(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = 'Somme des bases imposables'
    unit = units.XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        base_imposable_tva_taux_reduit = personne('base_imposable_tva_taux_reduit', period)
        base_imposable_tva_taux_intermediaire = personne('base_imposable_tva_taux_intermediaire', period)
        base_imposable_tva_taux_normal = personne('base_imposable_tva_taux_normal', period)
        return base_imposable_tva_taux_reduit + base_imposable_tva_taux_intermediaire + base_imposable_tva_taux_normal

    def formula_2025(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        base_imposable_tva_taux_reduit = personne('base_imposable_tva_taux_reduit', period)
        base_imposable_tva_taux_intermediaire = personne('base_imposable_tva_taux_intermediaire', period)
        base_imposable_tva_taux_normal = personne('base_imposable_tva_taux_normal', period)
        base_imposable_tva_taux_livraisons_immeubles_et_cession_parts = personne('base_imposable_tva_taux_livraisons_immeubles_et_cession_parts', period)
        return base_imposable_tva_taux_reduit + base_imposable_tva_taux_intermediaire + base_imposable_tva_taux_normal + base_imposable_tva_taux_livraisons_immeubles_et_cession_parts


class sous_total_operations(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = 'Somme des opérations'
    unit = units.XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        montant_prestations_services_hors_taxes = personne('montant_prestations_services_hors_taxes', period)
        montant_ventes_hors_taxes = personne('montant_ventes_hors_taxes', period)
        return montant_ventes_hors_taxes + montant_prestations_services_hors_taxes


class entrants_tva_valides(Variable):
    value_type = bool
    entity = Personne
    definition_period = MONTH
    label = """
    Boolean indiquant si les montant des trois bases imposables sont cohérent
    avec les montants des ventes et des prestations de services réalisées
    """
    unit = units.BOOLEAN

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        sous_total_base_imposable = personne('sous_total_base_imposable', period)
        sous_total_operations = personne('sous_total_operations', period)
        return sous_total_base_imposable == sous_total_operations
