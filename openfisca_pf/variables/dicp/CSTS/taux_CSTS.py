# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.base import *


class nombre_tranches_cst_s(Variable):
    value_type = int
    entity = Pays
    definition_period = MONTH
    label = u"Nombre de tranches de CST-S\n\nAttention, ce paramètre ne DOIT PAS être modifié pour un calcul.\nSa modification n'est possible que pour les simulations, et dans ce cas seule la première valeur de la simulation sera prise en compte. A modifier avec une extrême précaution !"

    def formula(pays, period, parameters):
        return len(parameters(period).dicp.cst_s.taux.rates)


class taux_cst_s_tranche_1(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = u"Taux de la CST-S pour la tranche 1"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source
    unit = '/1'

    # The formula to compute the income tax for a given person at a given period
    def formula(personne, period, parameters):
        return parameters(period).dicp.cst_s.taux.rates[0]


class taux_cst_s_tranche_2(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = u"Taux de la CST-S pour la tranche 2"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source
    unit = '/1'

    # The formula to compute the income tax for a given person at a given period
    def formula(personne, period, parameters):
        return parameters(period).dicp.cst_s.taux.rates[1]


class taux_cst_s_tranche_3(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = u"Taux de la CST-S pour la tranche 3"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source
    unit = '/1'

    # The formula to compute the income tax for a given person at a given period
    def formula(personne, period, parameters):
        return parameters(period).dicp.cst_s.taux.rates[2]


class taux_cst_s_tranche_4(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = u"Taux de la CST-S pour la tranche 4"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source
    unit = '/1'

    # The formula to compute the income tax for a given person at a given period
    def formula(personne, period, parameters):
        return parameters(period).dicp.cst_s.taux.rates[3]


class taux_cst_s_tranche_5(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = u"Taux de la CST-S pour la tranche 5"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source
    unit = '/1'

    # The formula to compute the income tax for a given person at a given period
    def formula(personne, period, parameters):
        return parameters(period).dicp.cst_s.taux.rates[4]


class taux_cst_s_tranche_6(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = u"Taux de la CST-S pour la tranche 6"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source
    unit = '/1'

    # The formula to compute the income tax for a given person at a given period
    def formula(personne, period, parameters):
        return parameters(period).dicp.cst_s.taux.rates[5]


class taux_cst_s_tranche_7(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = u"Taux de la CST-S pour la tranche 7"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source
    unit = '/1'

    # The formula to compute the income tax for a given person at a given period
    def formula(personne, period, parameters):
        return parameters(period).dicp.cst_s.taux.rates[6]


class taux_cst_s_tranche_8(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = u"Taux de la CST-S pour la tranche 8"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source
    unit = '/1'

    # The formula to compute the income tax for a given person at a given period
    def formula(personne, period, parameters):
        return parameters(period).dicp.cst_s.taux.rates[7]


class taux_cst_s_tranche_9(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = u"Taux de la CST-S pour la tranche 9"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source
    unit = '/1'

    # The formula to compute the income tax for a given person at a given period
    def formula(personne, period, parameters):
        return parameters(period).dicp.cst_s.taux.rates[8]


class taux_cst_s_tranche_10(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = u"Taux de la CST-S pour la tranche 10"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source
    unit = '/1'

    # The formula to compute the income tax for a given person at a given period
    def formula(personne, period, parameters):
        return parameters(period).dicp.cst_s.taux.rates[9]


class taux_cst_s_tranche_11(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = u"Taux de la CST-S pour la tranche 11"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source
    unit = '/1'

    # The formula to compute the income tax for a given person at a given period
    def formula(personne, period, parameters):
        return parameters(period).dicp.cst_s.taux.rates[10]


class taux_cst_s_tranche_12(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = u"Taux de la CST-S pour la tranche 12"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source
    unit = '/1'

    # The formula to compute the income tax for a given person at a given period
    def formula(personne, period, parameters):
        return parameters(period).dicp.cst_s.taux.rates[11]
