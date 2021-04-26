# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.base import *


# CSTS par tranche
class cst_s_due_tranche_1(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 1"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(personne, period, parameters):
        salaires_tranche = personne('revenus_tranche_1', period)
        revenus_tranche_inf_0 = salaires_tranche < 0
        taux = personne.pays('taux_cst_s_tranche_1', period)
        cst_s_tranche = taux * where(revenus_tranche_inf_0, 0, salaires_tranche)
        return arrondiSup(cst_s_tranche)


class cst_s_due_tranche_2(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 1"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(personne, period, parameters):
        salaires_tranche = personne('revenus_tranche_2', period)
        revenus_tranche_inf_0 = salaires_tranche < 0
        taux = personne.pays('taux_cst_s_tranche_2', period)
        cst_s_tranche = taux * where(revenus_tranche_inf_0, 0, salaires_tranche)
        return arrondiSup(cst_s_tranche)


class cst_s_due_tranche_3(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 2"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(personne, period, parameters):
        salaires_tranche = personne('revenus_tranche_3', period)
        revenus_tranche_inf_0 = salaires_tranche < 0
        taux = personne.pays('taux_cst_s_tranche_3', period)
        cst_s_tranche = taux * where(revenus_tranche_inf_0, 0, salaires_tranche)
        return arrondiSup(cst_s_tranche)


class cst_s_due_tranche_4(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 3"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(personne, period, parameters):
        salaires_tranche = personne('revenus_tranche_4', period)
        revenus_tranche_inf_0 = salaires_tranche < 0
        taux = personne.pays('taux_cst_s_tranche_4', period)
        cst_s_tranche = taux * where(revenus_tranche_inf_0, 0, salaires_tranche)
        return arrondiSup(cst_s_tranche)


class cst_s_due_tranche_5(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 4"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(personne, period, parameters):
        salaires_tranche = personne('revenus_tranche_5', period)
        revenus_tranche_inf_0 = salaires_tranche < 0
        taux = personne.pays('taux_cst_s_tranche_5', period)
        cst_s_tranche = taux * where(revenus_tranche_inf_0, 0, salaires_tranche)
        return arrondiSup(cst_s_tranche)


class cst_s_due_tranche_6(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 5"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(personne, period, parameters):
        salaires_tranche = personne('revenus_tranche_6', period)
        revenus_tranche_inf_0 = salaires_tranche < 0
        taux = personne.pays('taux_cst_s_tranche_6', period)
        cst_s_tranche = taux * where(revenus_tranche_inf_0, 0, salaires_tranche)
        return arrondiSup(cst_s_tranche)


class cst_s_due_tranche_7(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 6"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(personne, period, parameters):
        salaires_tranche = personne('revenus_tranche_7', period)
        revenus_tranche_inf_0 = salaires_tranche < 0
        taux = personne.pays('taux_cst_s_tranche_7', period)
        cst_s_tranche = taux * where(revenus_tranche_inf_0, 0, salaires_tranche)
        return arrondiSup(cst_s_tranche)


class cst_s_due_tranche_8(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 7"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(personne, period, parameters):
        salaires_tranche = personne('revenus_tranche_8', period)
        revenus_tranche_inf_0 = salaires_tranche < 0
        taux = personne.pays('taux_cst_s_tranche_8', period)
        cst_s_tranche = taux * where(revenus_tranche_inf_0, 0, salaires_tranche)
        return arrondiSup(cst_s_tranche)


class cst_s_due_tranche_9(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 8"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(personne, period, parameters):
        salaires_tranche = personne('revenus_tranche_9', period)
        revenus_tranche_inf_0 = salaires_tranche < 0
        taux = personne.pays('taux_cst_s_tranche_9', period)
        cst_s_tranche = taux * where(revenus_tranche_inf_0, 0, salaires_tranche)
        return arrondiSup(cst_s_tranche)


class cst_s_due_tranche_10(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 9"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(personne, period, parameters):
        salaires_tranche = personne('revenus_tranche_10', period)
        revenus_tranche_inf_0 = salaires_tranche < 0
        taux = personne.pays('taux_cst_s_tranche_10', period)
        cst_s_tranche = taux * where(revenus_tranche_inf_0, 0, salaires_tranche)
        return arrondiSup(cst_s_tranche)


class cst_s_due_tranche_11(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 11"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(personne, period, parameters):
        salaires_tranche = personne('revenus_tranche_11', period)
        revenus_tranche_inf_0 = salaires_tranche < 0
        taux = personne.pays('taux_cst_s_tranche_11', period)
        cst_s_tranche = taux * where(revenus_tranche_inf_0, 0, salaires_tranche)
        return arrondiSup(cst_s_tranche)


class cst_s_due_tranche_12(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 12"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(personne, period, parameters):
        salaires_tranche = personne('revenus_tranche_12', period)
        revenus_tranche_inf_0 = salaires_tranche < 0
        taux = personne.pays('taux_cst_s_tranche_12', period)
        cst_s_tranche = taux * where(revenus_tranche_inf_0, 0, salaires_tranche)
        return arrondiSup(cst_s_tranche)
