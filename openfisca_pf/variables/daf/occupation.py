# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# # Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.base import *


class UnitesDuree(Enum):
    Heures = u'Heures'
    Jours = u'Jours'
    Mois = u'Mois'
    Annees = u'Années'


class ZonesOccupations(Enum):
    NA = u'Non applicable'
    Z1 = u'Zone 1'
    Z2 = u'Zone 2'
    Z3 = u'Zone 3'
    Z4 = u'Zone 4'


class duree_occupation_domaine(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Durée de l'occupation du domaine"


class unite_duree_occupation_domaine(Variable):
    value_type = Enum
    possible_values = UnitesDuree
    default_value = UnitesDuree.Jours
    entity = Personne
    definition_period = DAY
    label = "Unité de la durée d'occupation (heures, jours, mois, années...)"


class zone_occupation_domaine(Variable):
    value_type = Enum
    possible_values = ZonesOccupations
    default_value = ZonesOccupations.NA
    entity = Personne
    definition_period = DAY
    label = "Zone de l'occupation du domaine"
