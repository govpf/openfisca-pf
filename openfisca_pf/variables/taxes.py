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
        # print(parameters(period).taxes.taux_cst_s.rates[0])
        value = 0
        for i, taux in enumerate(parameters(period).taxes.taux_cst_s.rates):
            # value += taux * entreprise('salaires_tranche_' + str(i), period)
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
        salaire_sup_150000 = person('salaire', period) >= 150000
        echelle = parameters(period).taxes.taux_cst_s
        # Si le salaire est < 150000 alors retourne 0
        return echelle.calc(where(salaire_sup_150000, salaire, 0))

# CSTS par tranche

class cst_s_tranche_0(Variable):
    value_type = float
    entity = Entreprise
    definition_period = MONTH
    label = u"CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 1"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(entreprise, period, parameters):
        return numpy.floor(parameters(period).taxes.taux_cst_s.rates[0] * entreprise('salaires_tranche_0', period))

class cst_s_tranche_1(Variable):
    value_type = float
    entity = Entreprise
    definition_period = MONTH
    label = u"CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 1"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(entreprise, period, parameters):
        return numpy.floor(parameters(period).taxes.taux_cst_s.rates[1] * entreprise('salaires_tranche_1', period))

class cst_s_tranche_2(Variable):
    value_type = float
    entity = Entreprise
    definition_period = MONTH
    label = u"CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 2"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(entreprise, period, parameters):
        return numpy.floor(parameters(period).taxes.taux_cst_s.rates[2] * entreprise('salaires_tranche_2', period))

class cst_s_tranche_3(Variable):
    value_type = float
    entity = Entreprise
    definition_period = MONTH
    label = u"CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 3"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(entreprise, period, parameters):
        return numpy.floor(parameters(period).taxes.taux_cst_s.rates[3] * entreprise('salaires_tranche_3', period))

class cst_s_tranche_4(Variable):
    value_type = float
    entity = Entreprise
    definition_period = MONTH
    label = u"CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 4"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(entreprise, period, parameters):
        return numpy.floor(parameters(period).taxes.taux_cst_s.rates[4] * entreprise('salaires_tranche_4', period))

class cst_s_tranche_5(Variable):
    value_type = float
    entity = Entreprise
    definition_period = MONTH
    label = u"CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 5"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(entreprise, period, parameters):
        return numpy.floor(parameters(period).taxes.taux_cst_s.rates[5] * entreprise('salaires_tranche_5', period))

class cst_s_tranche_6(Variable):
    value_type = float
    entity = Entreprise
    definition_period = MONTH
    label = u"CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 6"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(entreprise, period, parameters):
        return numpy.floor(parameters(period).taxes.taux_cst_s.rates[6] * entreprise('salaires_tranche_6', period))

class cst_s_tranche_7(Variable):
    value_type = float
    entity = Entreprise
    definition_period = MONTH
    label = u"CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 7"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(entreprise, period, parameters):
        return numpy.floor(parameters(period).taxes.taux_cst_s.rates[7] * entreprise('salaires_tranche_7', period))

class cst_s_tranche_8(Variable):
    value_type = float
    entity = Entreprise
    definition_period = MONTH
    label = u"CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 8"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(entreprise, period, parameters):
        return numpy.floor(parameters(period).taxes.taux_cst_s.rates[8] * entreprise('salaires_tranche_8', period))

class cst_s_tranche_9(Variable):
    value_type = float
    entity = Entreprise
    definition_period = MONTH
    label = u"CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 9"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(entreprise, period, parameters):
        return numpy.floor(parameters(period).taxes.taux_cst_s.rates[9] * entreprise('salaires_tranche_9', period))

class cst_s_tranche_10(Variable):
    value_type = float
    entity = Entreprise
    definition_period = MONTH
    label = u"CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 10"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(entreprise, period, parameters):
        return numpy.floor(parameters(period).taxes.taux_cst_s.rates[10] * entreprise('salaires_tranche_10', period))

class income_tax(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = u"Income tax"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(person, period, parameters):
        return person('salary', period) * parameters(period).taxes.income_tax_rate

class social_security_contribution(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = u"Progressive contribution paid on salaries to finance social security"
    reference = "https://law.gov.example/social_security_contribution"  # Always use the most official source

    def formula(person, period, parameters):
        salary = person('salary', period)

        # The social_security_contribution is computed according to a marginal scale.
        scale = parameters(period).taxes.social_security_contribution

        return scale.calc(salary)


class housing_tax(Variable):
    value_type = float
    entity = Household
    definition_period = YEAR  # This housing tax is defined for a year.
    label = u"Tax paid by each household proportionally to the size of its accommodation"
    reference = "https://law.gov.example/housing_tax"  # Always use the most official source

    def formula(household, period, parameters):
        # The housing tax is defined for a year, but depends on the `accommodation_size` and `housing_occupancy_status` on the first month of the year.
        # Here period is a year. We can get the first month of a year with the following shortcut.
        # To build different periods, see https://openfisca.org/doc/coding-the-legislation/35_periods.html#calculate-dependencies-for-a-specific-period
        january = period.first_month
        accommodation_size = household('accommodation_size', january)

        tax_params = parameters(period).taxes.housing_tax
        tax_amount = max_(accommodation_size * tax_params.rate, tax_params.minimal_amount)

        # `housing_occupancy_status` is an Enum variable
        occupancy_status = household('housing_occupancy_status', january)
        HousingOccupancyStatus = occupancy_status.possible_values  # Get the enum associated with the variable
        # To access an enum element, we use the `.` notation.
        tenant = (occupancy_status == HousingOccupancyStatus.tenant)
        owner = (occupancy_status == HousingOccupancyStatus.owner)

        # The tax is applied only if the household owns or rents its main residency
        return (owner + tenant) * tax_amount
