# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *


class revenus_tranche_1(Variable):
    value_type = float
    entity = Personne
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period  # Optional attribute. Allows user to declare a salary for a year. OpenFisca will spread the yearly amount over the months contained in the year.
    label = "Salaires de la tranche 0 de CST"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source
    unit = 'currency-XPF'

    # def formula(personne, period, parameters):
    #     seuil = parameters(period).dicp.cst_s.taux.thresholds[1]
    #     salaires_i = personne.members('salaire', period)
    #     salaire_sup_150000 = salaires_i >= 150000
    #     # Les salaires < 150000 ne sont pas comptabilisés
    #     return personne.sum(where(salaire_sup_150000, salaires_i, 0))

# class salaires_inferieurs_150000(Variable):
#     value_type = float
#     entity = Personne
#     default_value = 0
#     definition_period = MONTH
#     set_input = set_input_divide_by_period  # Optional attribute. Allows user to declare a salary for a year. OpenFisca will spread the yearly amount over the months contained in the year.
#     label = "Salaires de la tranche 0 de CST"
#     reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

#     def formula(personne, period, parameters):
#         seuil = parameters(period).dicp.cst_s.taux.thresholds[1]
#         salaires_i = personne.members('salaire', period)
#         salaire_sup_150000 = salaires_i >= 150000
#         # Les salaires < 150000 ne sont pas comptabilisés
#         return personne.sum(where(salaire_sup_150000, 0, salaires_i))


class revenus_tranche_2(Variable):
    value_type = float
    entity = Personne
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period  # Optional attribute. Allows user to declare a salary for a year. OpenFisca will spread the yearly amount over the months contained in the year.
    label = "Salaires de la tranche 1 de CST"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source
    unit = 'currency-XPF'

    # def formula(personne, period, parameters):
    #     index_tranche = 1
    #     seuil = parameters(period).dicp.cst_s.taux.thresholds[index_tranche + 1]
    #     salaires_i = personne.members('salaire', period)
    #     print(salaires_i)
    #     tranche = min_(salaires_i, seuil)
    #     valeur = personne.sum(tranche)
    #     for i in range(0, index_tranche):
    #         valeur = valeur - personne('revenus_tranche_' + str(i), period)
    #     return valeur


# This variable is a pure input: it doesn't have a formula
class revenus_tranche_3(Variable):
    value_type = float
    entity = Personne
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period  # Optional attribute. Allows user to declare a salary for a year. OpenFisca will spread the yearly amount over the months contained in the year.
    label = "Salaires de la tranche 2 de CST"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source
    unit = 'currency-XPF'

    # def formula(personne, period, parameters):
    #     index_tranche = 2
    #     seuil = parameters(period).dicp.cst_s.taux.thresholds[index_tranche + 1]
    #     salaires_i = personne.members('salaire', period)
    #     tranche = min_(salaires_i, seuil)
    #     valeur = personne.sum(tranche)
    #     for i in range(0, index_tranche):
    #         valeur = valeur - personne('revenus_tranche_' + str(i), period)
    #     return valeur


# This variable is a pure input: it doesn't have a formula
class revenus_tranche_4(Variable):
    value_type = float
    entity = Personne
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period  # Optional attribute. Allows user to declare a salary for a year. OpenFisca will spread the yearly amount over the months contained in the year.
    label = "Salaires de la tranche 3 de CST"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source
    unit = 'currency-XPF'

    # def formula(personne, period, parameters):
    #     index_tranche = 3
    #     seuil = parameters(period).dicp.cst_s.taux.thresholds[index_tranche + 1]
    #     salaires_i = personne.members('salaire', period)
    #     tranche = min_(salaires_i, seuil)
    #     valeur = personne.sum(tranche)
    #     for i in range(0, index_tranche):
    #         valeur = valeur - personne('revenus_tranche_' + str(i), period)
    #     return valeur


# This variable is a pure input: it doesn't have a formula
class revenus_tranche_5(Variable):
    value_type = float
    entity = Personne
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period  # Optional attribute. Allows user to declare a salary for a year. OpenFisca will spread the yearly amount over the months contained in the year.
    label = "Salaires de la tranche 4 de CST"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source
    unit = 'currency-XPF'

    # def formula(personne, period, parameters):
    #     index_tranche = 4
    #     seuil = parameters(period).dicp.cst_s.taux.thresholds[index_tranche + 1]
    #     salaires_i = personne.members('salaire', period)
    #     tranche = min_(salaires_i, seuil)
    #     valeur = personne.sum(tranche)
    #     for i in range(0, index_tranche):
    #         valeur = valeur - personne('revenus_tranche_' + str(i), period)
    #     return valeur


# This variable is a pure input: it doesn't have a formula
class revenus_tranche_6(Variable):
    value_type = float
    entity = Personne
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period  # Optional attribute. Allows user to declare a salary for a year. OpenFisca will spread the yearly amount over the months contained in the year.
    label = "Salaires de la tranche 5 de CST"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source
    unit = 'currency-XPF'

    # def formula(personne, period, parameters):
    #     index_tranche = 5
    #     seuil = parameters(period).dicp.cst_s.taux.thresholds[index_tranche + 1]
    #     salaires_i = personne.members('salaire', period)
    #     tranche = min_(salaires_i, seuil)
    #     valeur = personne.sum(tranche)
    #     for i in range(0, index_tranche):
    #         valeur = valeur - personne('revenus_tranche_' + str(i), period)
    #     return valeur


# This variable is a pure input: it doesn't have a formula
class revenus_tranche_7(Variable):
    value_type = float
    entity = Personne
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period  # Optional attribute. Allows user to declare a salary for a year. OpenFisca will spread the yearly amount over the months contained in the year.
    label = "Salaires de la tranche 6 de CST"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source
    unit = 'currency-XPF'

    # def formula(personne, period, parameters):
    #     index_tranche = 6
    #     seuil = parameters(period).dicp.cst_s.taux.thresholds[index_tranche + 1]
    #     salaires_i = personne.members('salaire', period)
    #     tranche = min_(salaires_i, seuil)
    #     valeur = personne.sum(tranche)
    #     for i in range(0, index_tranche):
    #         valeur = valeur - personne('revenus_tranche_' + str(i), period)
    #     return valeur


# This variable is a pure input: it doesn't have a formula
class revenus_tranche_8(Variable):
    value_type = float
    entity = Personne
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period  # Optional attribute. Allows user to declare a salary for a year. OpenFisca will spread the yearly amount over the months contained in the year.
    label = "Salaires de la tranche 7 de CST"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source
    unit = 'currency-XPF'

    # def formula(personne, period, parameters):
    #     index_tranche = 7
    #     seuil = parameters(period).dicp.cst_s.taux.thresholds[index_tranche + 1]
    #     salaires_i = personne.members('salaire', period)
    #     tranche = min_(salaires_i, seuil)
    #     valeur = personne.sum(tranche)
    #     for i in range(0, index_tranche):
    #         valeur = valeur - personne('revenus_tranche_' + str(i), period)
    #     return valeur


# This variable is a pure input: it doesn't have a formula
class revenus_tranche_9(Variable):
    value_type = float
    entity = Personne
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period  # Optional attribute. Allows user to declare a salary for a year. OpenFisca will spread the yearly amount over the months contained in the year.
    label = "Salaires de la tranche 8 de CST"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source
    unit = 'currency-XPF'

    # def formula(personne, period, parameters):
    #     index_tranche = 8
    #     seuil = parameters(period).dicp.cst_s.taux.thresholds[index_tranche + 1]
    #     salaires_i = personne.members('salaire', period)
    #     tranche = min_(salaires_i, seuil)
    #     valeur = personne.sum(tranche)
    #     for i in range(0, index_tranche):
    #         valeur = valeur - personne('revenus_tranche_' + str(i), period)
    #     return valeur


# This variable is a pure input: it doesn't have a formula
class revenus_tranche_10(Variable):
    value_type = float
    entity = Personne
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period  # Optional attribute. Allows user to declare a salary for a year. OpenFisca will spread the yearly amount over the months contained in the year.
    label = "Salaires de la tranche 9 de CST"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source
    unit = 'currency-XPF'

    # def formula(personne, period, parameters):
    #     index_tranche = 9
    #     seuil = parameters(period).dicp.cst_s.taux.thresholds[index_tranche + 1]
    #     salaires_i = personne.members('salaire', period)
    #     tranche = min_(salaires_i, seuil)
    #     valeur = personne.sum(tranche)
    #     for i in range(0, index_tranche):
    #         valeur = valeur - personne('revenus_tranche_' + str(i), period)
    #     return valeur


# This variable is a pure input: it doesn't have a formula
class revenus_tranche_11(Variable):
    value_type = float
    entity = Personne
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period  # Optional attribute. Allows user to declare a salary for a year. OpenFisca will spread the yearly amount over the months contained in the year.
    label = "Salaires de la tranche 11 de CST"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source
    unit = 'currency-XPF'

    # def formula(personne, period, parameters):
    #     index_tranche = 10
    #     salaires_i = personne.members('salaire', period)
    #     valeur = personne.sum(salaires_i)
    #     for i in range(0, index_tranche - 1):
    #         valeur = valeur - personne('revenus_tranche_' + str(i), period)
    #     return valeur


# This variable is a pure input: it doesn't have a formula
class revenus_tranche_12(Variable):
    value_type = float
    entity = Personne
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period  # Optional attribute. Allows user to declare a salary for a year. OpenFisca will spread the yearly amount over the months contained in the year.
    label = "Salaires de la tranche 12 de CST"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source
    unit = 'currency-XPF'

    # def formula(personne, period, parameters):
    #     index_tranche = 10
    #     salaires_i = personne.members('salaire', period)
    #     valeur = personne.sum(salaires_i)
    #     for i in range(0, index_tranche - 1):
    #         valeur = valeur - personne('revenus_tranche_' + str(i), period)
    #     return valeur


class salaires_totaux(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"Somme des salaires versés par l'entreprise"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source
    unit = 'currency-XPF'

    def formula(personne, period, parameters):
        salaires_i = personne.members('salaire', period)
        return personne.sum(salaires_i)