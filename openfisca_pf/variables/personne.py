# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# # Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.base import *
# # This variable is a pure input: it doesn't have a formula
from numpy import datetime64, timedelta64


class en_activite_salariee(Variable):
    value_type = bool
    entity = Personne
    definition_period = MONTH
    # set_input = set_input_divide_by_period  # Optional attribute. Allows user to declare a salary for a year. OpenFisca will spread the yearly amount over the months contained in the year.
    label = "Indique si la personne exerce une activité (stage ou emploi)"
    # reference = "https://law.gov.example/salary"  # Always use the most official source

    def formula(personne, period, parameters):
        type_contrat_actuel = personne('type_contrat', period)
        return type_contrat_actuel != TypeContrat.Aucun


class perte_emploi(Variable):
    value_type = bool
    entity = Personne
    definition_period = MONTH
    set_input = set_input_dispatch_by_period
    label = "Indique si la personne a perdu son emploi"

    def formula(personne, period, parameters):
        type_contrat_actuel = personne('type_contrat', period)
        type_contrat_precedent = personne('type_contrat', period.last_month)

        return (type_contrat_actuel == TypeContrat.Aucun) * (type_contrat_precedent != TypeContrat.Aucun)


class est_demandeur_emploi(Variable):
    value_type = bool
    default_value = False
    entity = Personne
    definition_period = MONTH
    label = "Indique si la personne est inscrite au SEFI en tant que demandeur d'emploi"


class patente(Variable):
    value_type = bool
    default_value = False
    entity = Personne
    definition_period = MONTH
    label = "Indique si la personne a une patente"


class type_contrat(Variable):
    value_type = Enum
    possible_values = TypeContrat
    default_value = TypeContrat.Aucun
    entity = Personne
    definition_period = MONTH
    set_input = set_input_dispatch_by_period
    label = "type de contrat du salarié"
    # reference = "https://law.gov.example/salary"  # Always use the most official source


class regime_cps(Variable):
    value_type = Enum
    possible_values = RegimeCPS
    default_value = RegimeCPS.NonAffilie
    entity = Personne
    definition_period = MONTH
    set_input = set_input_dispatch_by_period
    label = "régime d'affiliation à la CPS de la personne"
    # reference = "https://law.gov.example/salary"  # Always use the most official source


class salaire(Variable):
    value_type = float
    default_value = 0
    entity = Personne
    definition_period = MONTH
    label = "Salaire"
    # reference = "https://law.gov.example/salary"  # Always use the most official source


# From Openfisca France
class age(Variable):
    unit = 'years'
    value_type = int
    default_value = -9999
    entity = Personne
    label = "Âge (en années) au premier jour du mois"
    definition_period = MONTH
    is_period_size_independent = True
    set_input = set_input_dispatch_by_period

    def formula(personne, period, parameters):
        has_birth = personne.get_holder('date_naissance').get_known_periods()
        if not has_birth:
            has_age_en_mois = bool(personne.get_holder('age_en_mois').get_known_periods())
            if has_age_en_mois:
                return personne('age_en_mois', period) // 12

            # If age is known at the same day of another year, compute the new age from it.
            holder = personne.get_holder('age')
            start = period.start
            known_periods = holder.get_known_periods()
            if known_periods:
                for last_period in sorted(known_periods, reverse = True):
                    last_start = last_period.start
                    if last_start.day == start.day:
                        last_array = holder.get_array(last_period)
                        return (
                            last_array
                            + int(
                                start.year
                                - last_start.year
                                + (start.month - last_start.month) / 12
                                )
                            )

        date_naissance = personne('date_naissance', period)
        epsilon = timedelta64(1)
        return (datetime64(period.start) - date_naissance + epsilon).astype('timedelta64[Y]')


# From Openfisca France
class age_en_mois(Variable):
    value_type = int
    default_value = -9999
    unit = 'months'
    entity = Personne
    label = "Âge (en mois)"
    is_period_size_independent = True
    definition_period = MONTH

    def formula(personne, period, parameters):
        # If age_en_mois is known at the same day of another month, compute the new age_en_mois from it.
        holder = personne.get_holder('age_en_mois')
        start = period.start
        known_periods = holder.get_known_periods()

        for last_period in sorted(known_periods, reverse = True):
            last_start = last_period.start
            if last_start.day == start.day:
                last_array = holder.get_array(last_period)
                return last_array + ((start.year - last_start.year) * 12 + (start.month - last_start.month))

        has_birth = personne.get_holder('date_naissance').get_known_periods()
        if not has_birth:
            has_age = bool(personne.get_holder('age').get_known_periods())
            if has_age:
                return personne('age', period) * 12
        date_naissance = personne('date_naissance', period)
        epsilon = timedelta64(1)
        return (datetime64(period.start) - date_naissance + epsilon).astype('timedelta64[M]')


class date_naissance(Variable):
    value_type = date
    default_value = date(1900, 1, 1)
    entity = Personne
    label = "Date de naissance"
    definition_period = ETERNITY
