# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation for scheduling the state royalty dor one request.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# # Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.variables.daf.redevance_domaniale.enums import *


class nature_emprise_occupation_redevance_domaniale_echeancier(Variable):
    value_type = Enum
    possible_values = TypesNatureEmprise
    default_value = TypesNatureEmprise.equipement_du_pays
    entity = Personne
    definition_period = ETERNITY
    # set_input = set_input_dispatch_by_period
    label = "Type de nature d'emprise"


class date_validation_redevance_domaniale_echeancier(Variable):
    value_type = date
    entity = Personne
    label = "Date de validation de la redevance domaniale"
    definition_period = ETERNITY


class duree_occupation_redevance_domaniale_echeancier(Variable):
    value_type = int
    entity = Personne
    definition_period = ETERNITY
    label = "Durée de l'occupation du domaine en jours"


class variable_redevance_domaniale_echeancier(Variable):
    value_type = int
    entity = Personne
    definition_period = ETERNITY
    label = "Variable de l'occupation du domaine, peut être exprimée en m, en m² ou en m^3, pour définir une unité de longueur, de surface ou de volume"


class nombre_unite_redevance_domaniale_echeancier(Variable):
    value_type = int
    entity = Personne
    definition_period = ETERNITY
    label = "Nombre d'unités dans l'occupation du domaine"
