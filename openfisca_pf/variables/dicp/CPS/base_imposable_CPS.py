# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *


class base_imposable_cps(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = u"Base imposable de la TVA à taux réduit"
    unit = 'currency-XPF'
    reference = ["Code des impots : LP. 358-1 et LP. 358-2", "https://www.impot-polynesie.gov.pf/code/5-titre-v-contribution-pour-la-solidarite"]
    default_value = 0
    end = '2023-09-30'

    def formula(personne, period, parameters):
        base_imposable_tva_taux_reduit = personne(f'base_imposable_tva_taux_reduit', period)
        base_imposable_tva_taux_intermediaire = personne(f'base_imposable_tva_taux_intermediaire', period)
        base_imposable_tva_taux_normal = personne(f'base_imposable_tva_taux_normal', period)
        return base_imposable_tva_taux_reduit + base_imposable_tva_taux_intermediaire + base_imposable_tva_taux_normal
