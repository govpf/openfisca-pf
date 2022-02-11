# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.base import *


class cps_nette_due(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    unit = 'currency-XPF'
    label = u"Montant de CPS nette dûe: \n\n#tva_nette_due = MAX(#cps_due - #cps_en_diminution + #cps_a_reverser, 0)"

    def formula(personne, period, parameters):
        cps_due = personne(f'cps_due', period)
        cps_en_diminution = personne(f'cps_en_diminution', period)
        cps_a_reverser = personne(f'cps_a_reverser', period)
        tva_nette_due = cps_due - cps_en_diminution + cps_a_reverser
        return max_(tva_nette_due, 0)


class tva_plus_cps_nette_due(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    unit = 'currency-XPF'
    label = u"Montant de CPS + TVA nette dûe: \n\n#tva_plus_cps_nette_due = #cps_nette_due + #tva_nette_due"

    def formula(personne, period, parameters):
        cps_nette_due = personne(f'cps_nette_due', period)
        tva_nette_due = personne(f'tva_nette_due', period)
        return cps_nette_due + tva_nette_due
