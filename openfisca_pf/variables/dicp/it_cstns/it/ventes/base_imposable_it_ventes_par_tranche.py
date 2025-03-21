# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    ParameterNode,
    Period,
    Population,
    Variable,
    YEAR
    )
from openfisca_pf.constants.units import XPF
from openfisca_pf.entities import Personne
from openfisca_pf.functions.tranches import calculer_base_imposable_ventes_tranche


class base_imposable_it_ventes_tranche_1(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Base imposable de l'impôt sur les transactions de ventes pour la tranche 1"
    reference = []
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return calculer_base_imposable_ventes_tranche(personne, period, 1, 'it')


class base_imposable_it_ventes_tranche_2(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Base imposable de l'impôt sur les transactions de ventes pour la tranche 2"
    reference = []
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return calculer_base_imposable_ventes_tranche(personne, period, 2, 'it')


class base_imposable_it_ventes_tranche_3(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Base imposable de l'impôt sur les transactions de ventes pour la tranche 3"
    reference = []
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return calculer_base_imposable_ventes_tranche(personne, period, 3, 'it')


class base_imposable_it_ventes_tranche_4(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Base imposable de l'impôt sur les transactions de ventes pour la tranche 4"
    reference = []
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return calculer_base_imposable_ventes_tranche(personne, period, 4, 'it')


class base_imposable_it_ventes_tranche_5(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Base imposable de l'impôt sur les transactions de ventes pour la tranche 5"
    reference = []
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return calculer_base_imposable_ventes_tranche(personne, period, 5, 'it')


class base_imposable_it_ventes_tranche_6(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Base imposable de l'impôt sur les transactions de ventes pour la tranche 6"
    reference = []
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return calculer_base_imposable_ventes_tranche(personne, period, 6, 'it')


class base_imposable_it_ventes_tranche_7(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Base imposable de l'impôt sur les transactions de ventes pour la tranche 7"
    reference = []
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return calculer_base_imposable_ventes_tranche(personne, period, 7, 'it')


class base_imposable_it_ventes_tranche_8(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Base imposable de l'impôt sur les transactions de ventes pour la tranche 8"
    reference = []
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return calculer_base_imposable_ventes_tranche(personne, period, 8, 'it')


class base_imposable_it_ventes_tranche_9(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Base imposable de l'impôt sur les transactions de ventes pour la tranche 9"
    reference = []
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return calculer_base_imposable_ventes_tranche(personne, period, 9, 'it')


class base_imposable_it_ventes_tranche_10(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Base imposable de l'impôt sur les transactions de ventes pour la tranche 10 [simulation]"
    reference = []
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return calculer_base_imposable_ventes_tranche(personne, period, 10, 'it')


class base_imposable_it_ventes_tranche_11(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Base imposable de l'impôt sur les transactions de ventes pour la tranche 11 [simulation]"
    reference = []
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return calculer_base_imposable_ventes_tranche(personne, period, 11, 'it')


class base_imposable_it_ventes_tranche_12(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Base imposable de l'impôt sur les transactions de ventes pour la tranche 12 [simulation]"
    reference = []
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return calculer_base_imposable_ventes_tranche(personne, period, 12, 'it')
