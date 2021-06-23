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


class TypesNatureEmprise(Enum):
    equipement_du_pays = u'Equipement du pays'
    terrain_de_sport_avec_electricite = u'Terrain de sport avec électricité'
    terrain_de_sport_sans_electricite = u'Terrain de sport sans électricité'
    infrastructure_de_restauration_aeroportuaire = u'Infrastructure de restauration aéroportuaire'


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


class zone_occupation_redevance_domaniale(Variable):
    value_type = Enum
    possible_values = ZonesOccupations
    default_value = ZonesOccupations.NA
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


class montant_redevance_domaniale(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de la redevance domaniale dûe"

    def formula(personne, period, parameters):
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        return select([nature_emprise_occupation_redevance_domaniale == TypesNatureEmprise.equipement_du_pays,
            nature_emprise_occupation_redevance_domaniale == TypesNatureEmprise.terrain_de_sport_avec_electricite,
            nature_emprise_occupation_redevance_domaniale == TypesNatureEmprise.terrain_de_sport_avec_electricite,
            nature_emprise_occupation_redevance_domaniale == TypesNatureEmprise.infrastructure_de_restauration_aeroportuaire],
        [personne('montant_redevance_domaniale_type_1', period), personne('montant_redevance_domaniale_type_2', period), personne('montant_redevance_domaniale_type_3', period), personne('montant_redevance_domaniale_type_4', period)])


class montant_redevance_domaniale_type_1(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de la redevance domaniale dûe calcul type 1"

    def formula(personne, period, parameters):
        return 1


class montant_redevance_domaniale_type_2(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de la redevance domaniale dûe calcul type 2"

    def formula(personne, period, parameters):
        return 2


class montant_redevance_domaniale_type_3(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de la redevance domaniale dûe calcul type 3"

    def formula(personne, period, parameters):
        return 3


class montant_redevance_domaniale_type_4(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de la redevance domaniale dûe calcul type 4"

    def formula(personne, period, parameters):
        return 4
