# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.base import *


class cps_due(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    unit = 'currency-XPF'
    label = u"Montant de CPS dûe: \n\n#cps_due = #base_imposable_cps * #taux_cps, 0"

    def formula(personne, period, parameters):
        base_imposable = personne(f'base_imposable_cps', period)
        taux = personne.pays(f'taux_cps', period)
        return arrondiSup(base_imposable * taux)
