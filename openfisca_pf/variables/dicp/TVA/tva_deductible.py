# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.base import *


class tva_deductible(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"Montant de TVA déductible: \n\n#tva_deductible = #tva_immobilisation_deductible + #tva_autres_biens_deductibles + #report_credit_tva_deductible"
    unit = 'currency-XPF'

    def formula(personne, period, parameters):
        tva_immobilisation_deductible = personne(f'tva_immobilisation_deductible', period)
        tva_autres_biens_deductibles = personne(f'tva_autres_biens_deductibles', period)
        regularisation_tva_deductible = personne(f'regularisation_tva_deductible', period)
        report_credit_tva_deductible = personne(f'report_credit_tva_deductible', period)
        return tva_immobilisation_deductible + tva_autres_biens_deductibles + regularisation_tva_deductible + report_credit_tva_deductible


class tva_immobilisation_deductible(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"Montant d'immobilisation déductible de la TVA"
    unit = 'currency-XPF'


class tva_autres_biens_deductibles(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"Montant autres biens déductible de la TVA"
    unit = 'currency-XPF'


class regularisation_tva_deductible(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"Montant de régularisation de TVA déductible"
    unit = 'currency-XPF'


class report_credit_tva_deductible(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"Montant d'immobilisation déductible de la TVA"
    unit = 'currency-XPF'
