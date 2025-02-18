# -*- coding: utf-8 -*-

from openfisca_pf.base import (
    ArrayLike,
    date,
    datetime64,
    ETERNITY,
    Enum,
    MONTH,
    Parameters,
    Period,
    RegimeCPS,
    set_input_dispatch_by_period,
    timedelta64,
    TypeContrat,
    Variable
    )
from openfisca_pf.entities import Personne
from openfisca_pf.constants.time import EPSILON_TIMEDELTA, NOMBRE_DE_MOIS_PAR_AN
from openfisca_pf.constants.units import MONTHS, YEARS


class date_naissance(Variable):
    entity = Personne
    definition_period = ETERNITY
    value_type = date
    default_value = date(1900, 1, 1)
    label = 'Quel est la date de naissance de la personne ?'
    reference = []


class est_demandeur_emploi(Variable):
    entity = Personne
    definition_period = MONTH
    value_type = bool
    default_value = False
    label = "Est-ce que la personne est inscrite au Service de l’emploi, de la formation et de l’insertion professionnelles (SEFI) en tant que demandeur d'emploi ?"
    reference = [
        'https://www.service-public.pf/voir/annuaire/sefi-service-de-lemploi-de-la-formation-et-de-linsertion/'
        ]


class patente(Variable):
    value_type = bool
    default_value = False
    entity = Personne
    definition_period = MONTH
    label = 'Est-ce que la personne à une patente ?'
    reference = []


class regime_cps(Variable):
    value_type = Enum
    possible_values = RegimeCPS
    default_value = RegimeCPS.NonAffilie
    entity = Personne
    definition_period = MONTH
    set_input = set_input_dispatch_by_period
    label = "régime d'affiliation à la Caisse de Prévoyance Sociale (CPS) de la personne"
    reference = []


class type_contrat(Variable):
    entity = Personne
    definition_period = MONTH
    value_type = Enum
    possible_values = TypeContrat
    default_value = TypeContrat.Aucun
    set_input = set_input_dispatch_by_period
    label = "Sous quel type de contrat la personne est-elle salarié de l'entreprise"
    reference = []


class salaire(Variable):
    value_type = float
    default_value = 0.
    entity = Personne
    definition_period = MONTH
    label = "Salaire versé par la société à la personne"
    reference = []


class en_activite_salariee(Variable):
    entity = Personne
    definition_period = MONTH
    value_type = bool
    default_value = False
    label = 'Indique si la personne exerce une activité (stage ou emploi)'
    reference = []

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        type_contrat = personne('type_contrat', period, parameters)
        return type_contrat != TypeContrat.Aucun


class perte_emploi(Variable):
    entity = Personne
    definition_period = MONTH
    value_type = bool
    default_value = False
    set_input = set_input_dispatch_by_period
    label = 'Indique si la personne a perdu son emploi'
    reference = []

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        type_contrat_actuel = personne('type_contrat', period, parameters)
        type_contrat_precedent = personne('type_contrat', period.last_month, parameters)
        return (type_contrat_actuel == TypeContrat.Aucun) \
            * (type_contrat_precedent != TypeContrat.Aucun)


class age(Variable):
    entity = Personne
    definition_period = MONTH
    value_type = int
    default_value = -9999
    unit = YEARS
    label = "Âge de la personne (en années) au premier jour du mois"
    is_period_size_independent = True
    set_input = set_input_dispatch_by_period

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:

        date_de_naissance_connue = personne.get_holder('date_naissance').get_known_periods()

        if date_de_naissance_connue:
            date_naissance = personne('date_naissance', period, parameters)
            return (datetime64(period.start) - date_naissance + EPSILON_TIMEDELTA).astype('timedelta64[Y]')

        else:
            age_en_mois_connue = bool(personne.get_holder('age_en_mois').get_known_periods())
            if age_en_mois_connue:
                return personne('age_en_mois', period, parameters) // NOMBRE_DE_MOIS_PAR_AN

            # Si on connait l'age de la personne lors d'une autre année, on peut le calculer
            age_a_d_autres_periodes = personne.get_holder('age')
            debut_periode_courante = period.start
            periodes_ou_l_age_est_connue = age_a_d_autres_periodes.get_known_periods()
            for periode_ou_l_age_est_connue in sorted(periodes_ou_l_age_est_connue, reverse = True):
                debut_periode_considere = periode_ou_l_age_est_connue.start
                if debut_periode_considere.day == debut_periode_courante.day:
                    age_a_la_period_considere = age_a_d_autres_periodes.get_array(periode_ou_l_age_est_connue)
                    return age_a_la_period_considere + int(
                        debut_periode_courante.year
                        - debut_periode_considere.year
                        + (debut_periode_courante.month - debut_periode_considere.month) / NOMBRE_DE_MOIS_PAR_AN
                        )


class age_en_mois(Variable):
    entity = Personne
    definition_period = MONTH
    value_type = int
    default_value = -9999
    unit = MONTHS
    label = 'Âge de la personne (en mois)'
    is_period_size_independent = True
    reference = []

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        # Si l'age_en_mois de la personne est connu un jour d'un autre mois, on peut calculer l'age en mois ce mois ci
        debut_de_la_periode_courrante = period.start
        age_en_mois_connus = personne.get_holder('age_en_mois')
        periodes_ou_l_age_en_mois_est_connu = age_en_mois_connus.get_known_periods()

        for periode_ou_l_age_est_connu in sorted(periodes_ou_l_age_en_mois_est_connu, reverse = True):
            debut_de_la_periode_ou_l_age_est_connu = periode_ou_l_age_est_connu.start
            if debut_de_la_periode_ou_l_age_est_connu.day == debut_de_la_periode_courrante.day:
                last_array = age_en_mois_connus.get_array(periode_ou_l_age_est_connu)
                return last_array + (
                    (debut_de_la_periode_courrante.year - debut_de_la_periode_ou_l_age_est_connu.year) * NOMBRE_DE_MOIS_PAR_AN
                    + (debut_de_la_periode_courrante.month - debut_de_la_periode_ou_l_age_est_connu.month)
                    )

        has_birth = personne.get_holder('date_naissance').get_known_periods()
        if not has_birth:
            has_age = bool(personne.get_holder('age').get_known_periods())
            if has_age:
                return personne('age', period) * NOMBRE_DE_MOIS_PAR_AN

        date_naissance = personne('date_naissance', period)
        epsilon = timedelta64(1)
        return (datetime64(period.start) - date_naissance + epsilon).astype('timedelta64[M]')
