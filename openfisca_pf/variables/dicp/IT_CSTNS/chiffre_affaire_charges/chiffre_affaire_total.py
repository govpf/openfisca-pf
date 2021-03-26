# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *


class chiffre_affaire_total(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant total du chiffre d'affaire"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(personne, period, parameters):
        return personne('chiffre_affaire_total_ventes', period) + personne('chiffre_affaire_total_prestations', period)
