# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
# from openfisca_pf.base import *


class IS_resultat_exploitation(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Le résultat d’exploitation (GG)"
    unit = 'currency-XPF'
    reference = "https://www.impot-polynesie.gov.pf/essentiel/limpot-sur-les-societes"  # Always use the most official source
