# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# # Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.base import *
# # This variable is a pure input: it doesn't have a formula


# class salaire(Variable):
#     value_type = float
#     entity = Personne
#     default_value = 0
#     definition_period = MONTH
#     set_input = set_input_divide_by_period  # Optional attribute. Allows user to declare a salary for a year. OpenFisca will spread the yearly amount over the months contained in the year.
#     label = "Salaire"
#     reference = "https://law.gov.example/salary"  # Always use the most official source
class en_activite_salariee(Variable):
    value_type = bool
    entity = Personne
    definition_period = MONTH
    # set_input = set_input_divide_by_period  # Optional attribute. Allows user to declare a salary for a year. OpenFisca will spread the yearly amount over the months contained in the year.
    label = "Indique si la personne exerce une activité (stage ou emploi)"
    # reference = "https://law.gov.example/salary"  # Always use the most official source

    def formula(personne, period, parameters):
        type_contrat_actuel = personne('type_contrat', period)
        return type_contrat_actuel != TypeContrat.Aucun


class type_contrat(Variable):
    value_type = Enum
    possible_values = TypeContrat
    default_value = TypeContrat.Aucun
    entity = Personne
    definition_period = MONTH
    set_input = set_input_dispatch_by_period
    label = "type de contrat du salarié"
    # reference = "https://law.gov.example/salary"  # Always use the most official source


class salaire(Variable):
    value_type = float
    default_value = 0
    entity = Personne
    definition_period = MONTH
    label = "Salaire"
    # reference = "https://law.gov.example/salary"  # Always use the most official source


# class salaire(Variable):
#     value_type = float
#     entity = Personne
#     default_value = 0
#     definition_period = MONTH
#     # set_input = set_input_divide_by_period  # Optional attribute. Allows user to declare a salary for a year. OpenFisca will spread the yearly amount over the months contained in the year.
#     label = "Salaire"
#     # reference = "https://law.gov.example/salary"  # Always use the most official source
