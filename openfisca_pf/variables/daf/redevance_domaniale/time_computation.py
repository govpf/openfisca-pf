# -*- coding: utf-8 -*-

from openfisca_pf.base import (
    ArrayLike,
    date,
    DAY,
    Parameters,
    Period,
    select,
    Variable
    )
from openfisca_pf.constants.time import (
    NOMBRE_D_HEURES_PAR_JOUR,
    NOMBRE_DE_JOURS_PAR_AN_AU_PRO_RATA_TEMPORIS,
    NOMBRE_DE_JOURS_PAR_MOIS_AU_PRO_RATA_TEMPORIS,
    NOMBRE_DE_MOIS_PAR_AN
    )
from openfisca_pf.constants.units import DAYS, YEARS, MONTHS
from openfisca_pf.enums.domaine import (
    UnitesDuree
    )
from openfisca_pf.entities import Personne
from openfisca_pf.functions.time import (
    annee_de_la_date,
    as_date,
    as_duration,
    jour_de_la_date,
    mois_de_la_date,
    pro_rata_temporis_jours_dans_le_mois,
    relative_delta_days,
    relative_delta_months,
    relative_delta_years
    )


class duree_occupation_redevance_domaniale_annee(Variable):
    entity = Personne
    definition_period = DAY
    value_type = float
    default_value = 0.
    unit = YEARS
    label = "La durée d'occupation en année"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        duree_occupation_redevance_domaniale = personne('duree_occupation_redevance_domaniale', period, parameters)
        unite_duree_occupation_redevance_domaniale = personne('unite_duree_occupation_redevance_domaniale', period, parameters)

        return select(
            [
                unite_duree_occupation_redevance_domaniale == UnitesDuree.Annees,
                unite_duree_occupation_redevance_domaniale == UnitesDuree.Mois,
                unite_duree_occupation_redevance_domaniale == UnitesDuree.Jours,
                unite_duree_occupation_redevance_domaniale == UnitesDuree.Heures
                ],
            [
                duree_occupation_redevance_domaniale,
                duree_occupation_redevance_domaniale / NOMBRE_DE_MOIS_PAR_AN,
                duree_occupation_redevance_domaniale / NOMBRE_DE_JOURS_PAR_AN_AU_PRO_RATA_TEMPORIS,
                duree_occupation_redevance_domaniale / (NOMBRE_DE_JOURS_PAR_AN_AU_PRO_RATA_TEMPORIS * NOMBRE_D_HEURES_PAR_JOUR)
                ],
            )


class duree_occupation_redevance_domaniale_jour(Variable):
    entity = Personne
    definition_period = DAY
    value_type = float
    default_value = 0.
    unit = DAYS
    label = "La durée d'occupation en jour"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        duree_occupation_redevance_domaniale = personne('duree_occupation_redevance_domaniale', period, parameters)
        unite_duree_occupation_redevance_domaniale = personne('unite_duree_occupation_redevance_domaniale', period, parameters)

        return select(
            [
                unite_duree_occupation_redevance_domaniale == UnitesDuree.Annees,
                unite_duree_occupation_redevance_domaniale == UnitesDuree.Mois,
                unite_duree_occupation_redevance_domaniale == UnitesDuree.Jours
                ],
            [
                duree_occupation_redevance_domaniale * NOMBRE_DE_JOURS_PAR_AN_AU_PRO_RATA_TEMPORIS,
                duree_occupation_redevance_domaniale * NOMBRE_DE_JOURS_PAR_MOIS_AU_PRO_RATA_TEMPORIS,
                duree_occupation_redevance_domaniale
                ]
            )


class duree_occupation_redevance_domaniale_mois(Variable):
    entity = Personne
    definition_period = DAY
    value_type = float
    default_value = 0.
    unit = MONTHS
    label = "La durée d'occupation en mois"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        duree_occupation_redevance_domaniale = personne('duree_occupation_redevance_domaniale', period, parameters)
        unite_duree_occupation_redevance_domaniale = personne('unite_duree_occupation_redevance_domaniale', period, parameters)

        return select(
            [
                unite_duree_occupation_redevance_domaniale == UnitesDuree.Annees,
                unite_duree_occupation_redevance_domaniale == UnitesDuree.Mois,
                unite_duree_occupation_redevance_domaniale == UnitesDuree.Jours
                ],
            [
                duree_occupation_redevance_domaniale * NOMBRE_DE_JOURS_PAR_MOIS_AU_PRO_RATA_TEMPORIS / NOMBRE_DE_JOURS_PAR_AN_AU_PRO_RATA_TEMPORIS,
                duree_occupation_redevance_domaniale,
                duree_occupation_redevance_domaniale / NOMBRE_DE_JOURS_PAR_MOIS_AU_PRO_RATA_TEMPORIS
                ],
            )


class duree_comptable_entre_deux_dates(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Calcul d'une durée comptable en jours entre deux dates"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        date_debut_occupation = personne('date_debut_occupation', period, parameters)
        date_fin_occupation = personne('date_fin_occupation', period, parameters)

        # On converti les dates en nombres de jours
        date_debut_occupation = as_date(date_debut_occupation, 'D')
        date_fin_occupation = as_date(date_fin_occupation, 'D')

        # Calculs des mois de debut et mois de fin d'occupation
        mois_debut_occupation = mois_de_la_date(date_debut_occupation)
        mois_fin_occupation = mois_de_la_date(date_fin_occupation)

        # Calculs des jours de debut et jours de fin d'occupation
        jour_debut_occupation = jour_de_la_date(date_debut_occupation)
        jour_fin_occupation = jour_de_la_date(date_fin_occupation)

        # Dans le contexte comptable, la règle est d'homogénéiser les durées des mois à 30 jours (et donc les années à 360)
        jour_debut = pro_rata_temporis_jours_dans_le_mois(jour_debut_occupation, mois_debut_occupation)
        jour_fin = pro_rata_temporis_jours_dans_le_mois(jour_fin_occupation, mois_fin_occupation)
        nombre_jours = jour_fin - jour_debut

        # Calcul de la durée en jours
        nombre_d_annees = annee_de_la_date(date_fin_occupation) - annee_de_la_date(date_debut_occupation)
        nombre_de_mois = mois_fin_occupation - mois_debut_occupation

        return nombre_d_annees * NOMBRE_DE_JOURS_PAR_AN_AU_PRO_RATA_TEMPORIS \
            + nombre_de_mois * NOMBRE_DE_JOURS_PAR_MOIS_AU_PRO_RATA_TEMPORIS \
            + nombre_jours + 1


class duree_calendaire_entre_deux_dates(Variable):
    entity = Personne
    definition_period = DAY
    value_type = int
    default_value = 0
    unit = DAYS
    label = "Calcul d'une durée calendaire en jours entre deux dates"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        date_debut_occupation = personne('date_debut_occupation', period, parameters)
        date_fin_occupation = personne('date_fin_occupation', period, parameters)

        return as_duration(
            as_date(date_fin_occupation, 'D') - as_date(date_debut_occupation, 'D'),
            'D'
            ) + 1


class date_fin_occupation(Variable):
    value_type = date
    entity = Personne
    definition_period = DAY
    label = "Calcul de la date de fin d'occupation en jours à partir de la date de début en jours, de la durée et de l'unité de durée"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        debut = personne('date_debut_occupation', period, parameters).astype(date)
        duree = personne('duree_occupation_redevance_domaniale', period, parameters).astype(float)
        unite = personne('unite_duree_occupation_redevance_domaniale', period, parameters)

        return as_date(select(
            [
                unite == UnitesDuree.Annees,
                unite == UnitesDuree.Mois,
                unite == UnitesDuree.Jours
                ],
            [
                debut + relative_delta_years(duree),
                debut + relative_delta_months(duree),
                debut + relative_delta_days(duree)
                ],
            ), 'D')
