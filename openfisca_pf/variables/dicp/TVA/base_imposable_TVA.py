# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *


class base_imposable_tva_taux_reduit(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = u"Base imposable de la TVA à taux réduit"
    unit = 'currency-XPF'
    reference = "https://law.gov.example/income_tax"  # Always use the most official source


class base_imposable_tva_taux_intermediaire(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = u"Base imposable de la TVA à taux intermediaire"
    unit = 'currency-XPF'
    reference = "https://law.gov.example/income_tax"  # Always use the most official source


class base_imposable_tva_taux_normal(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = u"Base imposable de la TVA à taux normal"
    unit = 'currency-XPF'
    reference = "https://law.gov.example/income_tax"  # Always use the most official source
