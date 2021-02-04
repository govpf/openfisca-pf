# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *


class cst_s_due_totale_par_employes(Variable):
    value_type = float
    entity = Entreprise
    definition_period = MONTH
    label = "Sum of the taxes paid by a household"
    reference = "https://stats.gov.example/taxes"

    def formula(entreprise, period, parameters):
        cst_s_i = entreprise.members('cst_s', period)
        return entreprise.sum(cst_s_i)


class cst_s_due_totale(Variable):
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
            value += entreprise('cst_s_due_tranche_' + str(i + 1), period)
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
