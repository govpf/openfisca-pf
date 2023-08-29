# -*- coding: utf-8 -*-

from openfisca_pf.constants.currency import *
from openfisca_pf.base import *
from openfisca_pf.entities import *


class tva_immobilisation_deductible(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"Montant d'immobilisation déductible de la TVA"
    unit = CURRENCY_XPF


class tva_autres_biens_deductibles(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"Montant autres biens déductible de la TVA"
    unit = CURRENCY_XPF


class regularisation_tva_deductible(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"Montant de régularisation de TVA déductible"
    unit = CURRENCY_XPF


class report_credit_tva_deductible(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"Montant d'immobilisation déductible de la TVA"
    unit = CURRENCY_XPF

class prorata_de_deduction(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"Prorata appliqué pour en arrivé au montants de TVA déductibles"
    unit = "Percent"

class tva_deductible(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"Montant de TVA déductible: \n\n#tva_deductible = #tva_immobilisation_deductible + #tva_autres_biens_deductibles + #report_credit_tva_deductible"
    unit = CURRENCY_XPF

    def formula(personne, period, parameters):
        tva_immobilisation_deductible = personne(f'tva_immobilisation_deductible', period, parameters)
        tva_autres_biens_deductibles = personne(f'tva_autres_biens_deductibles', period, parameters)
        regularisation_tva_deductible = personne(f'regularisation_tva_deductible', period, parameters)
        report_credit_tva_deductible = personne(f'report_credit_tva_deductible', period, parameters)
        return tva_immobilisation_deductible + tva_autres_biens_deductibles + regularisation_tva_deductible + report_credit_tva_deductible
