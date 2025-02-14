# -*- coding: utf-8 -*-

from openfisca_pf.base import (
    ArrayLike,
    calculer_base_imposable_ventes_tranche,
    Parameters,
    Period,
    Variable,
    YEAR
    )
from openfisca_pf.constants.units import XPF
from openfisca_pf.entities import Personne


CSTNS: str = 'cstns'


class base_imposable_cstns_ventes_tranche_1(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = 'Base imposable de ventes sur la tranche 1 de la CST NS'
    reference = []
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return calculer_base_imposable_ventes_tranche(personne, period, parameters, 1, CSTNS)


class base_imposable_cstns_ventes_tranche_2(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = 'Base imposable de ventes sur la tranche 2 de la CST NS'
    reference = []
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return calculer_base_imposable_ventes_tranche(personne, period, parameters, 2, CSTNS)


class base_imposable_cstns_ventes_tranche_3(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = 'Base imposable de ventes sur la tranche 3 de la CST NS'
    reference = []
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return calculer_base_imposable_ventes_tranche(personne, period, parameters, 3, CSTNS)


class base_imposable_cstns_ventes_tranche_4(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = 'Base imposable de ventes sur la tranche 4 de la CST NS'
    reference = []
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return calculer_base_imposable_ventes_tranche(personne, period, parameters, 4, CSTNS)


class base_imposable_cstns_ventes_tranche_5(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = 'Base imposable de ventes sur la tranche 5 de la CST NS'
    reference = []
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return calculer_base_imposable_ventes_tranche(personne, period, parameters, 5, CSTNS)


class base_imposable_cstns_ventes_tranche_6(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = 'Base imposable de ventes sur la tranche 6 de la CST NS'
    reference = []
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return calculer_base_imposable_ventes_tranche(personne, period, parameters, 6, CSTNS)


class base_imposable_cstns_ventes_tranche_7(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = 'Base imposable de ventes sur la tranche 7 de la CST NS'
    reference = []
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return calculer_base_imposable_ventes_tranche(personne, period, parameters, 7, CSTNS)


class base_imposable_cstns_ventes_tranche_8(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = 'Base imposable de ventes sur la tranche 8 de la CST NS'
    reference = []
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return calculer_base_imposable_ventes_tranche(personne, period, parameters, 8, CSTNS)


class base_imposable_cstns_ventes_tranche_9(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = 'Base imposable de ventes sur la tranche 9 de la CST NS'
    reference = []
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return calculer_base_imposable_ventes_tranche(personne, period, parameters, 9, CSTNS)


class base_imposable_cstns_ventes_tranche_10(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = 'Base imposable de ventes sur la tranche 10 de la CST NS'
    reference = []
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return calculer_base_imposable_ventes_tranche(personne, period, parameters, 10, CSTNS)


class base_imposable_cstns_ventes_tranche_11(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = 'Base imposable de ventes sur la tranche 11 de la CST NS'
    reference = []
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return calculer_base_imposable_ventes_tranche(personne, period, parameters, 11, CSTNS)


class base_imposable_cstns_ventes_tranche_12(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = 'Base imposable de ventes sur la tranche 12 de la CST NS'
    reference = []
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return calculer_base_imposable_ventes_tranche(personne, period, parameters, 12, CSTNS)
