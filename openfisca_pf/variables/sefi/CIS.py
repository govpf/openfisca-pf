# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# # Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.base import *
from numpy import datetime64, timedelta64


class eligible_cis(Variable):
    value_type = bool
    entity = Personne
    default_value = False
    definition_period = MONTH
    # set_input = set_input_divide_by_period  # Optional attribute. Allows user to declare a salary for a year. OpenFisca will spread the yearly amount over the months contained in the year.
    label = "Détermine l'éligibilité au CIS"
    reference = ["https://www.actusefi.org/ie2021", "https://static1.squarespace.com/static/5e975fac2e07f80c8bf30dfb/t/6037ef878dd5025a32e053bc/1614278537716/Loi+du+Pays+n%C2%B0+2021-12+du+24_02_2021.pdf", "https://static1.squarespace.com/static/5e975fac2e07f80c8bf30dfb/t/6039c23be06ce403c29735d2/1614398021087/Arr%C3%AAt%C3%A9+n%C2%B0+210+CM+du+24_02_2021.pdf"]

    def formula_2021_02(personne, period, parameters):

        regime_cps_valide = personne('regime_cps', period) == RegimeCPS.RSPF
        age = personne('age', period)
        age_min = parameters(period).sefi.CIS.age_minimum
        age_max = parameters(period).sefi.CIS.age_maximum
        return regime_cps_valide * (age <= age_max) * (age >= age_min)

    def formula(personne, period, parameters):
        return False


class eligible_cis_annee(Variable):
    value_type = bool
    entity = Personne
    default_value = False
    definition_period = YEAR
    label = "Indique si la personne est éligible à la CIS sur l'année en cours"
    reference = ["https://www.actusefi.org/ie2021", "https://static1.squarespace.com/static/5e975fac2e07f80c8bf30dfb/t/6037ef878dd5025a32e053bc/1614278537716/Loi+du+Pays+n%C2%B0+2021-12+du+24_02_2021.pdf", "https://static1.squarespace.com/static/5e975fac2e07f80c8bf30dfb/t/6039c23be06ce403c29735d2/1614398021087/Arr%C3%AAt%C3%A9+n%C2%B0+210+CM+du+24_02_2021.pdf"]

    def formula_2021_02(personne, period, parameters):
        eligible_cis = personne('eligible_cis', period, options = [ADD])
        return eligible_cis

    def formula(personne, period, parameters):
        return False


class montant_cis(Variable):
    value_type = float
    entity = Personne
    default_value = 0
    definition_period = MONTH
    label = "Montant CIS à verser"

    def formula_2021_02(personne, period, parameters):
        eligible_cis = personne('eligible_cis', period)
        nombre_heures_interet_general = personne('nombre_heures_interet_general', period.last_month)
        montant_cis_maximal = parameters(period).sefi.CIS.montant
        signature_convention_1_mois = personne('convention_cis_signee', period.last_month)
        signature_convention_2_mois = personne('convention_cis_signee', period.last_month.last_month)
        signature_convention_3_mois = personne('convention_cis_signee', period.last_month.last_month.last_month)
        ratio = nombre_heures_interet_general / 20
        return eligible_cis * select([signature_convention_1_mois, (signature_convention_2_mois + signature_convention_3_mois) * (ratio >= 1), (signature_convention_2_mois + signature_convention_3_mois) * (ratio < 1), not_(signature_convention_1_mois + signature_convention_2_mois + signature_convention_3_mois)],
        [montant_cis_maximal, montant_cis_maximal, montant_cis_maximal * ratio, 0])

    def formula(personne, period, parameters):
        return 0


class nombre_heures_interet_general(Variable):
    value_type = int
    entity = Personne
    default_value = 0
    definition_period = MONTH
    label = "Nombre d'heure d'intérêt général effectué"
    set_input = set_input_dispatch_by_period


# class date_convention_cis(Variable):
#     value_type = date
#     entity = Personne
#     label = "Date de signature de la convention CIS"
#     definition_period = ETERNITY


class convention_cis_signee(Variable):
    value_type = bool
    entity = Personne
    default_value = False
    label = "Mois de signature de la convention CIS"
    definition_period = MONTH


# class age_mois_convention_cis(Variable):
#     value_type = int
#     unit = 'months'
#     entity = Personne
#     label = "Âge de la convention CIS"
#     is_period_size_independent = True
#     definition_period = MONTH

#     def formula(personne, period, parameters):
#         # If age_en_mois is known at the same day of another month, compute the new age_en_mois from it.
#         date_convention_cis = personne('date_convention_cis', period)
#         epsilon = timedelta64(1)
#         return (datetime64(period.start) - date_convention_cis + epsilon).astype('timedelta64[M]')
