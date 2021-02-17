# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.base import *


class option_is(Variable):
    value_type = Enum
    entity = Entreprise
    possible_values = OuiNon
    default_value = OuiNon.N
    definition_period = YEAR
    label = u"Défini si l'entreprise à opté pour l'IS plutot que l'IT (applicable aux SNC)"
    # reference = "https://law.gov.example/income_tax"  # Always use the most official source


class option_is_possible(Variable):
    value_type = bool
    entity = Entreprise
    definition_period = YEAR
    label = u"Indique que l'entreprise peut opter pour l'IS plutot que l'IT"
    # reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        type_societe = entreprise('type_societe', period)
        return type_societe == TypeSociete.SNC


class redevable_is(Variable):
    value_type = bool
    entity = Entreprise
    definition_period = YEAR
    label = u"Défini si l'entreprise est éligible à l'IS"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        redevable_tpe = entreprise('redevable_tpe', period)
        redevable_it = entreprise('redevable_it', period)
        return not_(redevable_tpe + redevable_it)
