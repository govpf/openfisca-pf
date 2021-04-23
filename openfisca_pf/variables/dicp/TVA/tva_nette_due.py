# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.base import *


class tva_nette_due(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"Montant de TVA nette dûe: \n\n#tva_nette_due = MAX(#tva_exigible - #tva_deductible, 0)"

    def formula(personne, period, parameters):
        tva_deductible = personne(f'tva_deductible', period)
        tva_exigible = personne(f'tva_exigible', period)
        tva_nette_due = tva_exigible - tva_deductible
        return max_(tva_nette_due, 0)


class credit_tva(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"Montant de crédit de TVA : \n\n#credit_tva = MAX(#tva_deductible - #tva_exigible, 0)"

    def formula(personne, period, parameters):
        tva_deductible = personne(f'tva_deductible', period)
        tva_exigible = personne(f'tva_exigible', period)
        credit_tva = tva_deductible - tva_exigible
        return max_(credit_tva, 0)
