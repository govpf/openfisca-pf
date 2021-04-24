# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.base import *


class seuil_cst_s_tranche_1(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = u"Seuil de la CST-S pour la tranche 1"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(personne, period, parameters):
        return parameters(period).dicp.cst_s.taux.thresholds[0]


class seuil_cst_s_tranche_2(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = u"Seuil de la CST-S pour la tranche 2"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(personne, period, parameters):
        return parameters(period).dicp.cst_s.taux.thresholds[1]


class seuil_cst_s_tranche_3(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = u"Seuil de la CST-S pour la tranche 3"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(personne, period, parameters):
        return parameters(period).dicp.cst_s.taux.thresholds[2]


class seuil_cst_s_tranche_4(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = u"Seuil de la CST-S pour la tranche 4"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(personne, period, parameters):
        return parameters(period).dicp.cst_s.taux.thresholds[3]


class seuil_cst_s_tranche_5(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = u"Seuil de la CST-S pour la tranche 5"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(personne, period, parameters):
        return parameters(period).dicp.cst_s.taux.thresholds[4]


class seuil_cst_s_tranche_6(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = u"Seuil de la CST-S pour la tranche 6"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(personne, period, parameters):
        return parameters(period).dicp.cst_s.taux.thresholds[5]


class seuil_cst_s_tranche_7(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = u"Seuil de la CST-S pour la tranche 7"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(personne, period, parameters):
        return parameters(period).dicp.cst_s.taux.thresholds[6]


class seuil_cst_s_tranche_8(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = u"Seuil de la CST-S pour la tranche 8"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(personne, period, parameters):
        return parameters(period).dicp.cst_s.taux.thresholds[7]


class seuil_cst_s_tranche_9(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = u"Seuil de la CST-S pour la tranche 9"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(personne, period, parameters):
        return parameters(period).dicp.cst_s.taux.thresholds[8]


class seuil_cst_s_tranche_10(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = u"Seuil de la CST-S pour la tranche 10"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(personne, period, parameters):
        return parameters(period).dicp.cst_s.taux.thresholds[9]


class seuil_cst_s_tranche_11(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = u"Seuil de la CST-S pour la tranche 11"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(personne, period, parameters):
        return parameters(period).dicp.cst_s.taux.thresholds[10]
