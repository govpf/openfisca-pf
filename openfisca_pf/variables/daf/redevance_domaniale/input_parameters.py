# -*- coding: utf-8 -*-

from openfisca_pf.base import (
    date,
    DAY,
    Enum,
    Variable
    )
from openfisca_pf.constants.units import DAYS
from openfisca_pf.entities import Personne
from openfisca_pf.enums.domaine import (
    Commune,
    TypesNatureEmprise,
    ZoneDomPrive,
    ZoneLotAgricole,
    ZonesOccupations,
    UnitesDuree
    )


class duree_occupation_redevance_domaniale(Variable):
    entity = Personne
    definition_period = DAY
    value_type = int
    default_value = 0
    unit = DAYS
    label = "Durée de l'occupation du domaine"


class unite_duree_occupation_redevance_domaniale(Variable):
    entity = Personne
    definition_period = DAY
    value_type = Enum
    possible_values = UnitesDuree
    default_value = UnitesDuree.Jours
    label = "Unité de la durée d'occupation (heures, jours, mois, années)"


class nombre_unite_redevance_domaniale(Variable):
    entity = Personne
    definition_period = DAY
    value_type = int
    default_value = 0
    label = "Nombre d'unités dans l'occupation du domaine"


class variable_redevance_domaniale(Variable):
    entity = Personne
    definition_period = DAY
    # TODO: USE ENUM
    value_type = float
    default_value = 1
    label = "Variable de l'occupation du domaine, peut être exprimée en m, en m² ou en m^3, pour définir une unité de longueur, de surface ou de volume"


class zone_occupation_redevance_domaniale(Variable):
    entity = Personne
    definition_period = DAY
    value_type = Enum
    possible_values = ZonesOccupations
    default_value = ZonesOccupations.zone_1
    label = "Zone de l'occupation du domaine"


class nature_emprise_occupation_redevance_domaniale(Variable):
    entity = Personne
    definition_period = DAY
    value_type = Enum
    possible_values = TypesNatureEmprise
    default_value = TypesNatureEmprise.ip_eco_01_equipement_pays
    label = "Type de nature d'emprise"


class nombre_participant_redevance_domaniale(Variable):
    entity = Personne
    definition_period = DAY
    value_type = int
    default_value = 0
    label = "Nombre de participant à l'évènement"


class activite_cultuelle(Variable):
    entity = Personne
    definition_period = DAY
    value_type = bool
    default_value = False
    label = "Paramètre permettant de définir si la demande vient d'une association culturelle, religieuse ou sportive"


class commune_redevance_domaniale(Variable):
    entity = Personne
    definition_period = DAY
    value_type = Enum
    possible_values = Commune
    default_value = Commune.com340
    label = "Code de la commune en Polynésie Française"


class zone_domaine_prive(Variable):
    value_type = Enum
    entity = Personne
    definition_period = DAY
    possible_values = ZoneDomPrive
    default_value = ZoneDomPrive.zone_bord_de_mer
    label = "Zone du domaine privé "


class zone_lot_agricole(Variable):
    entity = Personne
    definition_period = DAY
    value_type = Enum
    possible_values = ZoneLotAgricole
    default_value = ZoneLotAgricole.amo
    label = "Lot agricole sélectionné pour la tarification pour la DAG "


class date_debut_occupation(Variable):
    entity = Personne
    definition_period = DAY
    value_type = date
    default_value = date.today()
    label = "Date de début d'occupation"
