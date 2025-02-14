# -*- coding: utf-8 -*-

from openfisca_pf.base import (
    ArrayLike,
    MONTH,
    set_input_divide_by_period,
    Parameters,
    Period,
    Variable
    )
from openfisca_pf.constants.dicp.references_csts import (
    REFERENCE_CODE_LP_BASE_ASSIETTE_CSTS,
    REFERENCE_LIEN_ASSIETTE_COTISATION_CSTS,
    REFERENCE_LIEN_BASE_CSTS,
    REFERENCE_LIEN_CODE
    )
from openfisca_pf.constants.units import XPF
from openfisca_pf.entities import Personne


class revenus_tranche_1(Variable):
    value_type = float
    entity = Personne
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = "Salaires de la tranche 0 de CST"
    reference = [
        REFERENCE_CODE_LP_BASE_ASSIETTE_CSTS,
        REFERENCE_LIEN_ASSIETTE_COTISATION_CSTS,
        REFERENCE_LIEN_BASE_CSTS,
        REFERENCE_LIEN_CODE
        ]
    unit = XPF


class revenus_tranche_2(Variable):
    value_type = float
    entity = Personne
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = "Salaires de la tranche 1 de CST"
    reference = [
        REFERENCE_CODE_LP_BASE_ASSIETTE_CSTS,
        REFERENCE_LIEN_ASSIETTE_COTISATION_CSTS,
        REFERENCE_LIEN_BASE_CSTS,
        REFERENCE_LIEN_CODE
        ]
    unit = XPF


class revenus_tranche_3(Variable):
    value_type = float
    entity = Personne
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = "Salaires de la tranche 2 de CST"
    reference = [
        REFERENCE_CODE_LP_BASE_ASSIETTE_CSTS,
        REFERENCE_LIEN_ASSIETTE_COTISATION_CSTS,
        REFERENCE_LIEN_BASE_CSTS,
        REFERENCE_LIEN_CODE
        ]
    unit = XPF


class revenus_tranche_4(Variable):
    value_type = float
    entity = Personne
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = "Salaires de la tranche 3 de CST"
    reference = [
        REFERENCE_CODE_LP_BASE_ASSIETTE_CSTS,
        REFERENCE_LIEN_ASSIETTE_COTISATION_CSTS,
        REFERENCE_LIEN_BASE_CSTS,
        REFERENCE_LIEN_CODE
        ]
    unit = XPF


class revenus_tranche_5(Variable):
    value_type = float
    entity = Personne
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = "Salaires de la tranche 4 de CST"
    reference = [
        REFERENCE_CODE_LP_BASE_ASSIETTE_CSTS,
        REFERENCE_LIEN_ASSIETTE_COTISATION_CSTS,
        REFERENCE_LIEN_BASE_CSTS,
        REFERENCE_LIEN_CODE
        ]
    unit = XPF


class revenus_tranche_6(Variable):
    value_type = float
    entity = Personne
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = "Salaires de la tranche 5 de CST"
    reference = [
        REFERENCE_CODE_LP_BASE_ASSIETTE_CSTS,
        REFERENCE_LIEN_ASSIETTE_COTISATION_CSTS,
        REFERENCE_LIEN_BASE_CSTS,
        REFERENCE_LIEN_CODE
        ]
    unit = XPF


class revenus_tranche_7(Variable):
    value_type = float
    entity = Personne
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = "Salaires de la tranche 6 de CST"
    reference = [
        REFERENCE_CODE_LP_BASE_ASSIETTE_CSTS,
        REFERENCE_LIEN_ASSIETTE_COTISATION_CSTS,
        REFERENCE_LIEN_BASE_CSTS,
        REFERENCE_LIEN_CODE
        ]
    unit = XPF


class revenus_tranche_8(Variable):
    value_type = float
    entity = Personne
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = "Salaires de la tranche 7 de CST"
    reference = [
        REFERENCE_CODE_LP_BASE_ASSIETTE_CSTS,
        REFERENCE_LIEN_ASSIETTE_COTISATION_CSTS,
        REFERENCE_LIEN_BASE_CSTS,
        REFERENCE_LIEN_CODE
        ]
    unit = XPF


class revenus_tranche_9(Variable):
    value_type = float
    entity = Personne
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = "Salaires de la tranche 8 de CST"
    reference = [
        REFERENCE_CODE_LP_BASE_ASSIETTE_CSTS,
        REFERENCE_LIEN_ASSIETTE_COTISATION_CSTS,
        REFERENCE_LIEN_BASE_CSTS,
        REFERENCE_LIEN_CODE
        ]
    unit = XPF


class revenus_tranche_10(Variable):
    value_type = float
    entity = Personne
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = "Salaires de la tranche 9 de CST"
    reference = [
        REFERENCE_CODE_LP_BASE_ASSIETTE_CSTS,
        REFERENCE_LIEN_ASSIETTE_COTISATION_CSTS,
        REFERENCE_LIEN_BASE_CSTS,
        REFERENCE_LIEN_CODE
        ]
    unit = XPF


class revenus_tranche_11(Variable):
    value_type = float
    entity = Personne
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = "Salaires de la tranche 11 de CST"
    reference = [
        REFERENCE_CODE_LP_BASE_ASSIETTE_CSTS,
        REFERENCE_LIEN_ASSIETTE_COTISATION_CSTS,
        REFERENCE_LIEN_BASE_CSTS,
        REFERENCE_LIEN_CODE
        ]
    unit = XPF


class revenus_tranche_12(Variable):
    value_type = float
    entity = Personne
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = "Salaires de la tranche 12 de CST"
    reference = [
        REFERENCE_CODE_LP_BASE_ASSIETTE_CSTS,
        REFERENCE_LIEN_ASSIETTE_COTISATION_CSTS,
        REFERENCE_LIEN_BASE_CSTS,
        REFERENCE_LIEN_CODE
        ]
    unit = XPF


class salaires_totaux(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = "Somme des salaires versés par l'entreprise"
    reference = [
        REFERENCE_CODE_LP_BASE_ASSIETTE_CSTS,
        REFERENCE_LIEN_ASSIETTE_COTISATION_CSTS,
        REFERENCE_LIEN_BASE_CSTS,
        REFERENCE_LIEN_CODE
        ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        salaires = personne.members('salaire', period, parameters)
        return personne.sum(salaires)
