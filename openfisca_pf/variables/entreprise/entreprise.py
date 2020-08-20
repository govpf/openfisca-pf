# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *

# This variable is a pure input: it doesn't have a formula
class entreprise_est_personne_physique(Variable):
    value_type = bool
    entity = Entreprise
    default_value = False
    definition_period = YEAR
    set_input = set_input_divide_by_period  # Optional attribute. Allows user to declare a salary for a year. OpenFisca will spread the yearly amount over the months contained in the year.
    label = "L'entreprise est également une personne physique"
    reference = "https://law.gov.example/salary"  # Always use the most official source
