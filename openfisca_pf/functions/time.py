# -*- coding: utf-8 -*-

import numpy
from numpy.typing import ArrayLike
from dateutil.relativedelta import relativedelta
from openfisca_pf.constants.time import NOMBRE_DE_JOURS_PAR_MOIS_AU_PRO_RATA_TEMPORIS


def as_date(a: numpy.ndarray, unit: str) -> numpy.ndarray:
    """
    Converti un vercteur de dates en un vecteur de `datetime64[U]` où `U` est l'unité désirée.

    :param a: Array of dates
    :param unit: either `D`, `M` or `
    :return: Vecteur converti
    """
    return a.astype(f'datetime64[{unit}]')


def as_duration(a: numpy.ndarray, unit: str) -> numpy.ndarray:
    """
    Converti un vecteur en un vecteur de durée `timedelta64[U]` où `U` est l'unité désirée, puis en un vecteur d'entiers naturels.

    :param a: Array of dates
    :param unit: either `D`, `M` or `
    :return: Vecteur converti
    """
    # TODO remove as int ?
    return a.astype(f'timedelta64[{unit}]').astype(int)


def annee_de_la_date(d: numpy.ndarray) -> numpy.ndarray:
    """
    Retourne l'annee de la date donnée.

    :param d: Date dont on veut l'année.
    :return: Année de la date donnée.
    """
    return as_date(d, 'Y')


def jour_de_la_date(d: numpy.ndarray) -> numpy.ndarray:
    """
    Retourne le mois de la date donnée.

    :param d: Date dont on veut le mois.
    :return: Mois de la date donnée.
    """
    return as_duration(
        as_date(d, 'D') - as_date(d, 'M'),
        'D'
        ) + 1


def mois_de_la_date(d: numpy.ndarray) -> numpy.ndarray:
    """
    Retourne le jour de la date donnée.

    :param d: Date dont on veut le jour.
    :return: Jour de la date donnée.
    """
    return as_duration(
        as_date(d, 'M') - as_date(d, 'Y'),
        'M'
        ) + 1


def pro_rata_temporis_jours_dans_le_mois(jour: ArrayLike, mois: ArrayLike) -> ArrayLike:
    """
    Retourne le jour au pro rata temporis dans le mois.
    Les mois sont tous ramené à 30 jours, et donc les années à 360 jours.

    :param jour: Jour du mois
    :param mois: Mois
    :return: Jour du mois au pro rata temporis
    """
    return numpy.where(
        (jour == 31) + (((jour == 28) + (jour == 29)) * (mois == 2)),
        NOMBRE_DE_JOURS_PAR_MOIS_AU_PRO_RATA_TEMPORIS,
        jour
        )


@numpy.vectorize
def relative_delta_years(a: numpy.ndarray) -> numpy.ndarray:
    """
    Crée une delta relatif de temps en année qui peut être ajouté à une date pour la modifier.
    Ce delta ajoutéera le nombre d'année spécifiées moins un jour car l'occupation termine à 23:59.

    :param a: Nombre d'année à ajouté à la date.
    :return: Un vecteur de delta relatif de temps.
    """
    return relativedelta(years = a, days = -1)


@numpy.vectorize
def relative_delta_months(a: numpy.ndarray) -> numpy.ndarray:
    """
    Crée une delta relatif de temps en mois qui peut être ajouté à une date pour la modifier.
    Ce delta ajoutéera le nombre de mois spécifiées moins un jour car l'occupation termine à 23:59.

    :param a: Nombre de mois à ajouté à la date.
    :return: Un vecteur de delta relatif de temps.
    """
    return relativedelta(months = a, days = -1)


@numpy.vectorize
def relative_delta_days(a: numpy.ndarray) -> numpy.ndarray:
    """
    Crée une delta relatif de temps en jours qui peut être ajouté à une date pour la modifier.
    Ce delta ajoutéera le nombre de jours spécifiées moins un jour car l'occupation termine à 23:59.

    :param a: Nombre de jours à ajouté à la date.
    :return: Un vecteur de delta relatif de temps.
    """
    return relativedelta(days = a - 1)
