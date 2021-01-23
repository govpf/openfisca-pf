# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
import numpy


class cst_s_totale_par_employes(Variable):
    value_type = float
    entity = Entreprise
    definition_period = MONTH
    label = "Sum of the taxes paid by a household"
    reference = "https://stats.gov.example/taxes"

    def formula(entreprise, period, parameters):
        cst_s_i = entreprise.members('cst_s', period)
        return entreprise.sum(cst_s_i)


class cst_s_totale(Variable):
    value_type = float
    entity = Entreprise
    definition_period = MONTH
    label = u"CST-S due par l'entreprise sur l'ensemble des salaires déclarés par tranche"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(entreprise, period, parameters):
        # print(parameters(period).dicp.cst_s.taux.rates[0])
        value = 0
        for i, taux in enumerate(parameters(period).dicp.cst_s.taux.rates):
            value += entreprise('cst_s_tranche_' + str(i), period)
        return value


class cst_s(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = u"CST-S due par l'employé sur son salaire mensuel"
    reference = "https://law.gov.example/social_security_contribution"  # Always use the most official source

    def formula_1950_01_01(person, period, parameters):
        salaire = person('salaire', period)
        # Quels sont les salaires >= 150000
        salaire_sup_150000 = salaire >= 150000
        echelle = parameters(period).dicp.cst_s.taux
        # Si le salaire est < 150000 alors retourne 0
        return round_(echelle.calc(where(salaire_sup_150000, salaire, 0)))


# CSTS par tranche
class cst_s_tranche_0(Variable):
    value_type = float
    entity = Entreprise
    definition_period = MONTH
    label = u"CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 1"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(entreprise, period, parameters):
        salaires_tranche = entreprise('salaires_tranche_0', period)
        salaires_tranche_inf_0 = salaires_tranche < 0
        return numpy.floor(parameters(period).dicp.cst_s.taux.rates[0] * where(salaires_tranche_inf_0, 0, salaires_tranche))


class cst_s_tranche_1(Variable):
    value_type = float
    entity = Entreprise
    definition_period = MONTH
    label = u"CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 1"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(entreprise, period, parameters):
        salaires_tranche = entreprise('salaires_tranche_1', period)
        salaires_tranche_inf_0 = salaires_tranche < 0
        return numpy.floor(parameters(period).dicp.cst_s.taux.rates[1] * where(salaires_tranche_inf_0, 0, salaires_tranche))


class cst_s_tranche_2(Variable):
    value_type = float
    entity = Entreprise
    definition_period = MONTH
    label = u"CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 2"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(entreprise, period, parameters):
        salaires_tranche = entreprise('salaires_tranche_2', period)
        salaires_tranche_inf_0 = salaires_tranche < 0
        return numpy.floor(parameters(period).dicp.cst_s.taux.rates[2] * where(salaires_tranche_inf_0, 0, salaires_tranche))


class cst_s_tranche_3(Variable):
    value_type = float
    entity = Entreprise
    definition_period = MONTH
    label = u"CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 3"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(entreprise, period, parameters):
        salaires_tranche = entreprise('salaires_tranche_3', period)
        salaires_tranche_inf_0 = salaires_tranche < 0
        return numpy.floor(parameters(period).dicp.cst_s.taux.rates[3] * where(salaires_tranche_inf_0, 0, salaires_tranche))


class cst_s_tranche_4(Variable):
    value_type = float
    entity = Entreprise
    definition_period = MONTH
    label = u"CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 4"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(entreprise, period, parameters):
        salaires_tranche = entreprise('salaires_tranche_4', period)
        salaires_tranche_inf_0 = salaires_tranche < 0
        return numpy.floor(parameters(period).dicp.cst_s.taux.rates[4] * where(salaires_tranche_inf_0, 0, salaires_tranche))


class cst_s_tranche_5(Variable):
    value_type = float
    entity = Entreprise
    definition_period = MONTH
    label = u"CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 5"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(entreprise, period, parameters):
        salaires_tranche = entreprise('salaires_tranche_5', period)
        salaires_tranche_inf_0 = salaires_tranche < 0
        return numpy.floor(parameters(period).dicp.cst_s.taux.rates[5] * where(salaires_tranche_inf_0, 0, salaires_tranche))


class cst_s_tranche_6(Variable):
    value_type = float
    entity = Entreprise
    definition_period = MONTH
    label = u"CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 6"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(entreprise, period, parameters):
        salaires_tranche = entreprise('salaires_tranche_6', period)
        salaires_tranche_inf_0 = salaires_tranche < 0
        return numpy.floor(parameters(period).dicp.cst_s.taux.rates[6] * where(salaires_tranche_inf_0, 0, salaires_tranche))


class cst_s_tranche_7(Variable):
    value_type = float
    entity = Entreprise
    definition_period = MONTH
    label = u"CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 7"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(entreprise, period, parameters):
        salaires_tranche = entreprise('salaires_tranche_7', period)
        salaires_tranche_inf_0 = salaires_tranche < 0
        return numpy.floor(parameters(period).dicp.cst_s.taux.rates[7] * where(salaires_tranche_inf_0, 0, salaires_tranche))


class cst_s_tranche_8(Variable):
    value_type = float
    entity = Entreprise
    definition_period = MONTH
    label = u"CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 8"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(entreprise, period, parameters):
        salaires_tranche = entreprise('salaires_tranche_8', period)
        salaires_tranche_inf_0 = salaires_tranche < 0
        return numpy.floor(parameters(period).dicp.cst_s.taux.rates[8] * where(salaires_tranche_inf_0, 0, salaires_tranche))


class cst_s_tranche_9(Variable):
    value_type = float
    entity = Entreprise
    definition_period = MONTH
    label = u"CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 9"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(entreprise, period, parameters):
        salaires_tranche = entreprise('salaires_tranche_9', period)
        salaires_tranche_inf_0 = salaires_tranche < 0
        return numpy.floor(parameters(period).dicp.cst_s.taux.rates[9] * where(salaires_tranche_inf_0, 0, salaires_tranche))


class cst_s_tranche_10(Variable):
    value_type = float
    entity = Entreprise
    definition_period = MONTH
    label = u"CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 10"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(entreprise, period, parameters):
        salaires_tranche = entreprise('salaires_tranche_10', period)
        salaires_tranche_inf_0 = salaires_tranche < 0
        return numpy.floor(parameters(period).dicp.cst_s.taux.rates[10] * where(salaires_tranche_inf_0, 0, salaires_tranche))
