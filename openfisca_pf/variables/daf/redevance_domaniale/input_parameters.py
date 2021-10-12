# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# # Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.variables.daf.redevance_domaniale.enums import *
from openfisca_pf.variables.daf.redevance_domaniale.enums_loc import *


class duree_occupation_redevance_domaniale(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Durée de l'occupation du domaine"


class unite_duree_occupation_redevance_domaniale(Variable):
    value_type = Enum
    possible_values = UnitesDuree
    default_value = UnitesDuree.Jours
    entity = Personne
    definition_period = DAY
    label = "Unité de la durée d'occupation (heures, jours, mois, années...)"


class nombre_unite_redevance_domaniale(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Nombre d'unités dans l'occupation du domaine"


class variable_redevance_domaniale(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Variable de l'occupation du domaine, peut être exprimée en m, en m² ou en m^3, pour définir une unité de longueur, de surface ou de volume"


class zone_occupation_redevance_domaniale(Variable):
    value_type = Enum
    possible_values = ZonesOccupations
    default_value = ZonesOccupations.zone_1
    entity = Personne
    definition_period = DAY
    label = "Zone de l'occupation du domaine"


class nature_emprise_occupation_redevance_domaniale(Variable):
    value_type = Enum
    possible_values = TypesNatureEmprise
    default_value = TypesNatureEmprise.equipement_du_pays
    entity = Personne
    definition_period = DAY
    label = "Type de nature d'emprise"


class nombre_participant_redevance_domaniale(Variable):
    value_type = int
    entity = Personne
    default_value = 0
    definition_period = DAY
    label = "Nombre de participant pour le calcul de la majoration"


class activite_cultuelle(Variable):
    value_type = bool
    entity = Personne
    default_value = False
    definition_period = ETERNITY
    label = "Paramètre permettant de définir si le demandeur est liée à des activités cultuelles"


class commune_domaine_prive(Variable):
    value_type = int
    entity = Personne
    default_value = False
    definition_period = ETERNITY
    label = "Area code for cities in French Polynesia"


class zone_domaine_prive(Variable):
    value_type = Enum
    possible_values = ZoneDomPrive
    default_value = ZoneDomPrive.zone_de_base
    entity = Personne
    definition_period = DAY
    label = "Selected zone for princing on the private domain "
