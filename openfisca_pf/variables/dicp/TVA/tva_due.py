# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.base import *


class tva_due_taux_reduit(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"Montant de TVA dûe au taux réduit: \n\n#tva_due_taux_reduit = #base_imposable_tva_taux_reduit * #taux_tva_reduit"
    set_input = set_input_dispatch_by_period
    unit = 'currency-XPF'

    def formula(personne, period, parameters):
        base_imposable = personne(f'base_imposable_tva_taux_reduit', period)
        taux = personne.pays(f'taux_tva_reduit', period)
        return arrondiSup(base_imposable * taux)


class tva_due_taux_intermediaire(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"Montant de TVA dûe au taux intermédiaire"
    set_input = set_input_dispatch_by_period
    unit = 'currency-XPF'

    def formula(personne, period, parameters):
        base_imposable = personne(f'base_imposable_tva_taux_intermediaire', period)
        taux = personne.pays(f'taux_tva_intermediaire', period)
        return arrondiSup(base_imposable * taux)


class tva_due_taux_normal(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"Montant de TVA dûe au taux normal"
    set_input = set_input_dispatch_by_period
    unit = 'currency-XPF'

    def formula(personne, period, parameters):
        base_imposable = personne(f'base_imposable_tva_taux_normal', period)
        taux = personne.pays(f'taux_tva_normal', period)
        return arrondiSup(base_imposable * taux)
