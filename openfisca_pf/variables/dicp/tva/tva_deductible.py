# -*- coding: utf-8 -*-

from openfisca_pf.base import (
    ArrayLike,
    MONTH,
    Parameters,
    Period,
    Variable
    )
from openfisca_pf.constants import units
from openfisca_pf.entities import Personne


class tva_immobilisation_deductible(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = "Montant d'immobilisation déductible de la TVA"
    unit = units.XPF


class tva_autres_biens_deductibles(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = "Montant autres biens déductible de la TVA"
    unit = units.XPF


class regularisation_tva_deductible(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = "Montant de régularisation de TVA déductible"
    unit = units.XPF


class report_credit_tva_deductible(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = "Montant d'immobilisation déductible de la TVA"
    unit = units.XPF


class prorata_de_deduction(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = "Prorata appliqué pour en arrivé au montants de TVA déductibles"
    unit = units.PER_ONE


class tva_deductible(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = "Montant de TVA déductible"
    unit = units.XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        tva_immobilisation_deductible = personne('tva_immobilisation_deductible', period, parameters)
        tva_autres_biens_deductibles = personne('tva_autres_biens_deductibles', period, parameters)
        regularisation_tva_deductible = personne('regularisation_tva_deductible', period, parameters)
        report_credit_tva_deductible = personne('report_credit_tva_deductible', period, parameters)
        return tva_immobilisation_deductible + tva_autres_biens_deductibles + regularisation_tva_deductible + report_credit_tva_deductible
