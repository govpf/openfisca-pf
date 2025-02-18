# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# # Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.variables.daf.rch.enums.enums import *


class type_demarche_rch(Variable):
    value_type = Enum
    possible_values = TypeDemarche
    default_value = TypeDemarche.Acquisition
    entity = Personne
    definition_period = DAY
    label = "Type de démarche auprès de la RCH"


class type_acheteur_rch(Variable):
    value_type = Enum
    possible_values = TypeAcheteur
    default_value = TypeAcheteur.DroitCommun
    entity = Personne
    definition_period = DAY
    label = "Type d'acheteur"


class type_parente_rch(Variable):
    value_type = Enum
    possible_values = TypeParente
    default_value = TypeParente.NonParent
    entity = Personne
    definition_period = DAY
    label = "Type d'acheteur"


class type_bien_rch(Variable):
    value_type = Enum
    possible_values = TypeBien
    default_value = TypeBien.TerrainNu
    entity = Personne
    definition_period = DAY
    label = "Type de bien"


class valeur_totale_bien_achat(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Valeur totale du bien à l'achat"


class valeur_totale_bien_vente(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Valeur totale du bien à la revente"


class valeur_locative_bien(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Valeur totale de location par mois"


class duree_bail_mois(Variable):
    value_type = int
    entity = Personne
    default_value = 3
    definition_period = DAY
    label = "Durée du bail en mois"


class valeur_plus_value_net(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Valeur de la plus-value immobilière nette"


class duree_possession_annee(Variable):
    value_type = int
    entity = Personne
    default_value = 3
    definition_period = DAY
    label = "Durée de possession en année"
