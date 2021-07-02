# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# # Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.variables.daf.redevance_domaniale.enums import *
from openfisca_pf.base import *


class duree_occupation_redevance_domaniale_annee(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "La durée d'occupation en année"

    def formula(personne, period, parameters):
        duree_occupation_redevance_domaniale = personne('duree_occupation_redevance_domaniale', period)
        unite_duree_occupation_redevance_domaniale = personne('unite_duree_occupation_redevance_domaniale', period)
        value = select(
            [unite_duree_occupation_redevance_domaniale == UnitesDuree.Annees,
            unite_duree_occupation_redevance_domaniale == UnitesDuree.Mois,
            unite_duree_occupation_redevance_domaniale == UnitesDuree.Jours,
            unite_duree_occupation_redevance_domaniale == UnitesDuree.Heures],
            [duree_occupation_redevance_domaniale,
            duree_occupation_redevance_domaniale / 12,
            duree_occupation_redevance_domaniale / 360,
            duree_occupation_redevance_domaniale / (360 * 8)],
            )
        return value


class duree_occupation_redevance_domaniale_jour(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "La durée d'occupation en jour"

    def formula(personne, period, parameters):
        duree_occupation_redevance_domaniale = personne('duree_occupation_redevance_domaniale', period)
        unite_duree_occupation_redevance_domaniale = personne('unite_duree_occupation_redevance_domaniale', period)
        value = select(
            [unite_duree_occupation_redevance_domaniale == UnitesDuree.Annees,
            unite_duree_occupation_redevance_domaniale == UnitesDuree.Mois,
            unite_duree_occupation_redevance_domaniale == UnitesDuree.Jours],
            [duree_occupation_redevance_domaniale*360,
            duree_occupation_redevance_domaniale*30,
            duree_occupation_redevance_domaniale],
            )
        return value


class duree_occupation_redevance_domaniale_mois(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "La durée d'occupation en mois"

    def formula(personne, period, parameters):
        duree_occupation_redevance_domaniale = personne('duree_occupation_redevance_domaniale', period)
        unite_duree_occupation_redevance_domaniale = personne('unite_duree_occupation_redevance_domaniale', period)
        value = select(
            [unite_duree_occupation_redevance_domaniale == UnitesDuree.Annees,
            unite_duree_occupation_redevance_domaniale == UnitesDuree.Mois,
            unite_duree_occupation_redevance_domaniale == UnitesDuree.Jours],
            [duree_occupation_redevance_domaniale/12,
            duree_occupation_redevance_domaniale,
            duree_occupation_redevance_domaniale/30],
            )
        return value


class montant_redevance_domaniale(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de la redevance domaniale dûe"

    def formula(personne, period, parameters):
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        type_calcul = int(parameters(period).daf.redevance_domaniale.type_calcul[nature_emprise_occupation_redevance_domaniale])
        return personne('montant_redevance_domaniale_type_' + str(type_calcul), period)

