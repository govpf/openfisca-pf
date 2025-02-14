# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import Personne
import openfisca_pf.constants.DICP.references_csts as references


class revenus_tranche_1(Variable):
    value_type = float
    entity = Personne
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = "Salaires de la tranche 0 de CST"
    reference = [references.REFERENCE_CODE_LP_BASE_ASSIETTE_CSTS, references.REFERENCE_LIEN_CODE, references.REFERENCE_LIEN_BASE_CSTS, references.REFERENCE_LIEN_ASSIETTE_COTISATION_CSTS]
    unit = 'currency-XPF'


class revenus_tranche_2(Variable):
    value_type = float
    entity = Personne
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = "Salaires de la tranche 1 de CST"
    reference = [references.REFERENCE_CODE_LP_BASE_ASSIETTE_CSTS, references.REFERENCE_LIEN_CODE, references.REFERENCE_LIEN_BASE_CSTS, references.REFERENCE_LIEN_ASSIETTE_COTISATION_CSTS]
    unit = 'currency-XPF'


class revenus_tranche_3(Variable):
    value_type = float
    entity = Personne
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = "Salaires de la tranche 2 de CST"
    reference = [references.REFERENCE_CODE_LP_BASE_ASSIETTE_CSTS, references.REFERENCE_LIEN_CODE, references.REFERENCE_LIEN_BASE_CSTS, references.REFERENCE_LIEN_ASSIETTE_COTISATION_CSTS]
    unit = 'currency-XPF'


class revenus_tranche_4(Variable):
    value_type = float
    entity = Personne
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = "Salaires de la tranche 3 de CST"
    reference = [references.REFERENCE_CODE_LP_BASE_ASSIETTE_CSTS, references.REFERENCE_LIEN_CODE, references.REFERENCE_LIEN_BASE_CSTS, references.REFERENCE_LIEN_ASSIETTE_COTISATION_CSTS]
    unit = 'currency-XPF'


class revenus_tranche_5(Variable):
    value_type = float
    entity = Personne
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = "Salaires de la tranche 4 de CST"
    reference = [references.REFERENCE_CODE_LP_BASE_ASSIETTE_CSTS, references.REFERENCE_LIEN_CODE, references.REFERENCE_LIEN_BASE_CSTS, references.REFERENCE_LIEN_ASSIETTE_COTISATION_CSTS]
    unit = 'currency-XPF'


class revenus_tranche_6(Variable):
    value_type = float
    entity = Personne
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = "Salaires de la tranche 5 de CST"
    reference = [references.REFERENCE_CODE_LP_BASE_ASSIETTE_CSTS, references.REFERENCE_LIEN_CODE, references.REFERENCE_LIEN_BASE_CSTS, references.REFERENCE_LIEN_ASSIETTE_COTISATION_CSTS]
    unit = 'currency-XPF'


class revenus_tranche_7(Variable):
    value_type = float
    entity = Personne
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = "Salaires de la tranche 6 de CST"
    reference = [references.REFERENCE_CODE_LP_BASE_ASSIETTE_CSTS, references.REFERENCE_LIEN_CODE, references.REFERENCE_LIEN_BASE_CSTS, references.REFERENCE_LIEN_ASSIETTE_COTISATION_CSTS]
    unit = 'currency-XPF'


class revenus_tranche_8(Variable):
    value_type = float
    entity = Personne
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = "Salaires de la tranche 7 de CST"
    reference = [references.REFERENCE_CODE_LP_BASE_ASSIETTE_CSTS, references.REFERENCE_LIEN_CODE, references.REFERENCE_LIEN_BASE_CSTS, references.REFERENCE_LIEN_ASSIETTE_COTISATION_CSTS]
    unit = 'currency-XPF'


class revenus_tranche_9(Variable):
    value_type = float
    entity = Personne
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = "Salaires de la tranche 8 de CST"
    reference = [references.REFERENCE_CODE_LP_BASE_ASSIETTE_CSTS, references.REFERENCE_LIEN_CODE, references.REFERENCE_LIEN_BASE_CSTS, references.REFERENCE_LIEN_ASSIETTE_COTISATION_CSTS]
    unit = 'currency-XPF'


class revenus_tranche_10(Variable):
    value_type = float
    entity = Personne
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = "Salaires de la tranche 9 de CST"
    reference = [references.REFERENCE_CODE_LP_BASE_ASSIETTE_CSTS, references.REFERENCE_LIEN_CODE, references.REFERENCE_LIEN_BASE_CSTS, references.REFERENCE_LIEN_ASSIETTE_COTISATION_CSTS]
    unit = 'currency-XPF'


class revenus_tranche_11(Variable):
    value_type = float
    entity = Personne
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = "Salaires de la tranche 11 de CST"
    reference = [references.REFERENCE_CODE_LP_BASE_ASSIETTE_CSTS, references.REFERENCE_LIEN_CODE, references.REFERENCE_LIEN_BASE_CSTS, references.REFERENCE_LIEN_ASSIETTE_COTISATION_CSTS]
    unit = 'currency-XPF'


class revenus_tranche_12(Variable):
    value_type = float
    entity = Personne
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = "Salaires de la tranche 12 de CST"
    reference = [references.REFERENCE_CODE_LP_BASE_ASSIETTE_CSTS, references.REFERENCE_LIEN_CODE, references.REFERENCE_LIEN_BASE_CSTS, references.REFERENCE_LIEN_ASSIETTE_COTISATION_CSTS]
    unit = 'currency-XPF'


class salaires_totaux(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"Somme des salaires versés par l'entreprise"
    reference = [references.REFERENCE_CODE_LP_BASE_ASSIETTE_CSTS, references.REFERENCE_LIEN_CODE, references.REFERENCE_LIEN_BASE_CSTS, references.REFERENCE_LIEN_ASSIETTE_COTISATION_CSTS]
    unit = 'currency-XPF'

    def formula(personne, period, parameters):
        salaires_i = personne.members('salaire', period)
        return personne.sum(salaires_i)
