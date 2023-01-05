# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# # Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.variables.daf.redevance_domaniale.enums.enums import *
from openfisca_pf.base import *
from numpy import logical_or, logical_and


class duree_occupation_redevance_domaniale_annee(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "La durée d'occupation en année"

    def formula(personne, period, parameters):
        # Variables
        duree_occupation_redevance_domaniale = personne('duree_occupation_redevance_domaniale', period)
        unite_duree_occupation_redevance_domaniale = personne('unite_duree_occupation_redevance_domaniale', period)

        # Constantes
        nombre_jour_par_an = parameters(period).daf.redevance_domaniale.constantes.nombre_jour_par_an_rd
        nombre_mois_par_an = parameters(period).daf.redevance_domaniale.constantes.nombre_mois_par_an_rd
        nombre_heure_par_jour = parameters(period).daf.redevance_domaniale.constantes.nombre_heure_par_jour_rd

        value = select(
            [unite_duree_occupation_redevance_domaniale == UnitesDuree.Annees,
            unite_duree_occupation_redevance_domaniale == UnitesDuree.Mois,
            unite_duree_occupation_redevance_domaniale == UnitesDuree.Jours,
            unite_duree_occupation_redevance_domaniale == UnitesDuree.Heures],
            [duree_occupation_redevance_domaniale,
            duree_occupation_redevance_domaniale / nombre_mois_par_an,
            duree_occupation_redevance_domaniale / nombre_jour_par_an,
            duree_occupation_redevance_domaniale / (nombre_jour_par_an * nombre_heure_par_jour)],
            )
        return value


class duree_occupation_redevance_domaniale_jour(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "La durée d'occupation en jour"

    def formula(personne, period, parameters):
        # Variables
        duree_occupation_redevance_domaniale = personne('duree_occupation_redevance_domaniale', period)
        unite_duree_occupation_redevance_domaniale = personne('unite_duree_occupation_redevance_domaniale', period)
        # Constantes
        nombre_jour_par_an = parameters(period).daf.redevance_domaniale.constantes.nombre_jour_par_an_rd
        nombre_jour_par_mois = parameters(period).daf.redevance_domaniale.constantes.nombre_jour_par_mois_rd

        value = select(
            [unite_duree_occupation_redevance_domaniale == UnitesDuree.Annees,
            unite_duree_occupation_redevance_domaniale == UnitesDuree.Mois,
            unite_duree_occupation_redevance_domaniale == UnitesDuree.Jours],
            [duree_occupation_redevance_domaniale * nombre_jour_par_an,
            duree_occupation_redevance_domaniale * nombre_jour_par_mois,
            duree_occupation_redevance_domaniale],
            )
        return value


class duree_occupation_redevance_domaniale_mois(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "La durée d'occupation en mois"

    def formula(personne, period, parameters):
        # Variables
        duree_occupation_redevance_domaniale = personne('duree_occupation_redevance_domaniale', period)
        unite_duree_occupation_redevance_domaniale = personne('unite_duree_occupation_redevance_domaniale', period)
        # Constantes
        nombre_jour_par_an = parameters(period).daf.redevance_domaniale.constantes.nombre_jour_par_an_rd
        nombre_jour_par_mois = parameters(period).daf.redevance_domaniale.constantes.nombre_jour_par_mois_rd

        value = select(
            [unite_duree_occupation_redevance_domaniale == UnitesDuree.Annees,
            unite_duree_occupation_redevance_domaniale == UnitesDuree.Mois,
            unite_duree_occupation_redevance_domaniale == UnitesDuree.Jours],
            [duree_occupation_redevance_domaniale * nombre_jour_par_mois / nombre_jour_par_an,
            duree_occupation_redevance_domaniale,
            duree_occupation_redevance_domaniale / nombre_jour_par_mois],
            )
        return value


class duree_comptable_entre_deux_dates(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Calcul d'une durée comptable en jours entre deux dates"

    def formula(personne, period, parameters):
        # Variables
        date_debut_occupation = personne('date_debut_occupation', period).astype('datetime64[D]')
        date_fin_occupation = personne('date_fin_occupation', period).astype('datetime64[D]')
        # Constantes
        nombre_jour_par_an = parameters(period).daf.redevance_domaniale.constantes.nombre_jour_par_an_rd
        nombre_jour_par_mois = parameters(period).daf.redevance_domaniale.constantes.nombre_jour_par_mois_rd

        # Extraction of the month integer
        mois_debut_occupation = (date_debut_occupation.astype('datetime64[M]') - date_debut_occupation.astype('datetime64[Y]')).astype('timedelta64[M]').astype(int) + 1
        mois_fin_occupation = (date_fin_occupation.astype('datetime64[M]') - date_fin_occupation.astype('datetime64[Y]')).astype('timedelta64[M]').astype(int) + 1

        # Extraction of the day integer
        jour_debut_occupation = (date_debut_occupation.astype('datetime64[D]') - date_debut_occupation.astype('datetime64[M]')).astype('timedelta64[D]').astype(int) + 1
        jour_fin_occupation = (date_fin_occupation.astype('datetime64[D]') - date_fin_occupation.astype('datetime64[M]')).astype('timedelta64[D]').astype(int) + 1

        # Dans le contexte comptable, la règle est d'homogénéiser les durées des mois à 30 jours (et donc les années à 360)
        jour_debut = where(logical_or(jour_debut_occupation == 31, logical_and(logical_or(jour_debut_occupation == 28, jour_debut_occupation == 29), mois_debut_occupation == 2)), 30, jour_debut_occupation)
        jour_fin = where(logical_or(jour_fin_occupation == 31, logical_and(logical_or(jour_fin_occupation == 28, jour_fin_occupation == 29), mois_fin_occupation == 2)), 30, jour_fin_occupation)

        # Calcul de la durée en jours
        nombre_annees = date_fin_occupation.astype('datetime64[Y]').astype(int) - date_debut_occupation.astype('datetime64[Y]').astype(int)
        nombre_mois = mois_fin_occupation - mois_debut_occupation
        nombre_jours = jour_fin - jour_debut
        duree_comptable = nombre_annees * nombre_jour_par_an + nombre_mois * nombre_jour_par_mois + nombre_jours + 1

        return duree_comptable


class duree_calendaire_entre_deux_dates(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Calcul d'une durée calendaire en jours entre deux dates"

    def formula(personne, period, parameters):
        # Variables
        date_debut_occupation = personne('date_debut_occupation', period).astype('datetime64[D]')
        date_fin_occupation = personne('date_fin_occupation', period).astype('datetime64[D]')

        duree_calendaire = (date_fin_occupation.astype('datetime64[D]') - date_debut_occupation.astype('datetime64[D]')).astype('timedelta64[D]').astype(int) + 1

        return duree_calendaire
