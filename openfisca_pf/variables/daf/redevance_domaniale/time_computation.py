# -*- coding: utf-8 -*-

import numpy
from dateutil.relativedelta import relativedelta

from openfisca_core.variables import Variable
from openfisca_core.periods import Period, DAY
from openfisca_core.parameters import Parameter
from openfisca_core.model_api import date

from openfisca_pf.entities import Personne
from openfisca_pf.variables.constants import NOMBRE_DE_JOUR_PAR_AN_PRORATA_TEMPORIS, NOMBRE_DE_JOUR_PAR_MOIS_PRORATA_TEMPORIS
from openfisca_pf.variables.daf.redevance_domaniale.enums.enums import *


class duree_occupation_redevance_domaniale_annee(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "La durée d'occupation en année"

    def formula(personne: Personne, period: Period, parameters: Parameter):
        # Variables
        duree_occupation_redevance_domaniale = personne("duree_occupation_redevance_domaniale", period)
        unite_duree_occupation_redevance_domaniale = personne("unite_duree_occupation_redevance_domaniale", period)

        # Constantes
        nombre_jour_par_an = parameters(period).daf.redevance_domaniale.constantes.nombre_jour_par_an_rd
        nombre_mois_par_an = parameters(period).daf.redevance_domaniale.constantes.nombre_mois_par_an_rd
        nombre_heure_par_jour = parameters(period).daf.redevance_domaniale.constantes.nombre_heure_par_jour_rd

        value = numpy.select(
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

    def formula(personne: Personne, period: Period, parameters: Parameter):
        # Variables
        duree_occupation_redevance_domaniale = personne("duree_occupation_redevance_domaniale", period)
        unite_duree_occupation_redevance_domaniale = personne("unite_duree_occupation_redevance_domaniale", period)
        # Constantes
        nombre_jour_par_an = parameters(period).daf.redevance_domaniale.constantes.nombre_jour_par_an_rd
        nombre_jour_par_mois = parameters(period).daf.redevance_domaniale.constantes.nombre_jour_par_mois_rd

        value = numpy.select(
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

    def formula(personne: Personne, period: Period, parameters: Parameter):
        # Variables
        duree_occupation_redevance_domaniale = personne("duree_occupation_redevance_domaniale", period)
        unite_duree_occupation_redevance_domaniale = personne("unite_duree_occupation_redevance_domaniale", period)

        value = numpy.select(
            [unite_duree_occupation_redevance_domaniale == UnitesDuree.Annees,
            unite_duree_occupation_redevance_domaniale == UnitesDuree.Mois,
            unite_duree_occupation_redevance_domaniale == UnitesDuree.Jours],
            [duree_occupation_redevance_domaniale * NOMBRE_DE_JOUR_PAR_MOIS_PRORATA_TEMPORIS / NOMBRE_DE_JOUR_PAR_AN_PRORATA_TEMPORIS,
            duree_occupation_redevance_domaniale,
            duree_occupation_redevance_domaniale / NOMBRE_DE_JOUR_PAR_MOIS_PRORATA_TEMPORIS],
            )
        return value


def dernier_jour_du_mois(mois: numpy.ndarray[int], jours: numpy.ndarray[int]):
    return jours == 31 or ((jours == 28 or jours == 29) and mois == 2)


def fixer_dernier_jour_a_30(mois: numpy.ndarray[int], jours: numpy.ndarray[int]):
    return numpy.where(
        dernier_jour_du_mois(mois, jours),
        30,
        jours)


class duree_comptable_entre_deux_dates(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Calcul d'une durée comptable en jours entre deux dates"

    def formula(personne: Personne, period: Period, parameters: Parameter):
        # Variables
        date_debut_occupation = personne("date_debut_occupation", period).astype('datetime64[D]')
        date_fin_occupation = personne("date_fin_occupation", period).astype('datetime64[D]')

        # Extraction of the month integer
        mois_debut_occupation = (date_debut_occupation.astype('datetime64[M]') - date_debut_occupation.astype('datetime64[Y]')).astype('timedelta64[M]').astype(int) + 1
        mois_fin_occupation = (date_fin_occupation.astype('datetime64[M]') - date_fin_occupation.astype('datetime64[Y]')).astype('timedelta64[M]').astype(int) + 1

        # Extraction of the day integer
        jour_debut_occupation = (date_debut_occupation.astype('datetime64[D]') - date_debut_occupation.astype('datetime64[M]')).astype('timedelta64[D]').astype(int) + 1
        jour_fin_occupation = (date_fin_occupation.astype('datetime64[D]') - date_fin_occupation.astype('datetime64[M]')).astype('timedelta64[D]').astype(int) + 1

        # Dans le contexte comptable, la règle est d'homogénéiser les durées des mois à 30 jours (et donc les années à 360)
        jour_debut = fixer_dernier_jour_a_30(mois_debut_occupation, jour_debut_occupation)
        jour_fin = fixer_dernier_jour_a_30(mois_fin_occupation, jour_fin_occupation)

        # Calcul de la durée en jours
        nombre_annees = date_fin_occupation.astype('datetime64[Y]').astype(int) - date_debut_occupation.astype('datetime64[Y]').astype(int)
        nombre_mois = mois_fin_occupation - mois_debut_occupation
        nombre_jours = jour_fin - jour_debut
        duree_comptable = nombre_annees * NOMBRE_DE_JOUR_PAR_AN_PRORATA_TEMPORIS + nombre_mois * NOMBRE_DE_JOUR_PAR_MOIS_PRORATA_TEMPORIS + nombre_jours + 1

        return duree_comptable


class duree_calendaire_entre_deux_dates(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Calcul d'une durée calendaire en jours entre deux dates"

    def formula(personne: Personne, period: Period, parameters: Parameter):
        # dependance
        date_debut_occupation = personne("date_debut_occupation", period).astype('datetime64[D]')
        date_fin_occupation = personne("date_fin_occupation", period).astype('datetime64[D]')
        return (date_fin_occupation.astype('datetime64[D]') - date_debut_occupation.astype('datetime64[D]')).astype('timedelta64[D]').astype(int) + 1


class date_fin_occupation(Variable):
    value_type = date
    entity = Personne
    definition_period = DAY
    label = "Calcul de la date de fin à partir de la durée"

    def formula(personne: Personne, period: Period, parameters: Parameter):
        # Variables
        date_debut_occupation = personne("date_debut_occupation", period)
        duree_occupation_redevance_domaniale = personne("duree_occupation_redevance_domaniale", period)
        unite_duree_occupation_redevance_domaniale = personne("unite_duree_occupation_redevance_domaniale", period)

        # Adding the duration at the beginning date minus one day (the occupation ended at 23:59)
        tempValue = []
        index = 0
        for item in date_debut_occupation:
            item = item.astype(date)
            value = numpy.select(
                [unite_duree_occupation_redevance_domaniale.decode()[index] == UnitesDuree.Annees,
                unite_duree_occupation_redevance_domaniale.decode()[index] == UnitesDuree.Mois,
                unite_duree_occupation_redevance_domaniale.decode()[index] == UnitesDuree.Jours],
                [item + relativedelta(years = duree_occupation_redevance_domaniale[index].astype(float), days = -1),
                item + relativedelta(months = duree_occupation_redevance_domaniale[index].astype(float), days = -1),
                item + relativedelta(days = duree_occupation_redevance_domaniale[index].astype(float) - 1)],
                )
            index = index + 1
            tempValue.append(numpy.datetime64(str(value)))
        date_fin = numpy.asarray(tempValue, dtype = numpy.datetime64)

        return date_fin
