# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    Parameters,
    Period,
    Variable,
    YEAR
    )
from openfisca_pf.constants.units import XPF
from openfisca_pf.entities import Personne
from openfisca_pf.functions.tranches import calculer_base_imposable_prestations_tranche


class base_imposable_it_prestations_tranche_1(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Base imposable de l'impôt sur les transactions de prestations pour la tranche 1"
    reference = []
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return calculer_base_imposable_prestations_tranche(personne, period, parameters, 1, 'it')


class base_imposable_it_prestations_tranche_2(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Base imposable de l'impôt sur les transactions de prestations pour la tranche 2"
    reference = []
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return calculer_base_imposable_prestations_tranche(personne, period, parameters, 2, 'it')


class base_imposable_it_prestations_tranche_3(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Base imposable de l'impôt sur les transactions de prestations pour la tranche 3"
    reference = []
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return calculer_base_imposable_prestations_tranche(personne, period, parameters, 3, 'it')


class base_imposable_it_prestations_tranche_4(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Base imposable de l'impôt sur les transactions de prestations pour la tranche 4"
    reference = []
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return calculer_base_imposable_prestations_tranche(personne, period, parameters, 4, 'it')


class base_imposable_it_prestations_tranche_5(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Base imposable de l'impôt sur les transactions de prestations pour la tranche 5"
    reference = []
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return calculer_base_imposable_prestations_tranche(personne, period, parameters, 5, 'it')


class base_imposable_it_prestations_tranche_6(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Base imposable de l'impôt sur les transactions de prestations pour la tranche 6"
    reference = []
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return calculer_base_imposable_prestations_tranche(personne, period, parameters, 6, 'it')


class base_imposable_it_prestations_tranche_7(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Base imposable de l'impôt sur les transactions de prestations pour la tranche 7"
    reference = []
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return calculer_base_imposable_prestations_tranche(personne, period, parameters, 7, 'it')


class base_imposable_it_prestations_tranche_8(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Base imposable de l'impôt sur les transactions de prestations pour la tranche 8"
    reference = []
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return calculer_base_imposable_prestations_tranche(personne, period, parameters, 8, 'it')


class base_imposable_it_prestations_tranche_9(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Base imposable de l'impôt sur les transactions de prestations pour la tranche 9"
    reference = []
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return calculer_base_imposable_prestations_tranche(personne, period, parameters, 9, 'it')


class base_imposable_it_prestations_tranche_10(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Base imposable de l'impôt sur les transactions de prestations pour la tranche 10"
    reference = []
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return calculer_base_imposable_prestations_tranche(personne, period, parameters, 10, 'it')


class base_imposable_it_prestations_tranche_11(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Base imposable de l'impôt sur les transactions de prestations pour la tranche 11"
    reference = []
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return calculer_base_imposable_prestations_tranche(personne, period, parameters, 11, 'it')


class base_imposable_it_prestations_tranche_12(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Base imposable de l'impôt sur les transactions de prestations pour la tranche 12"
    reference = []
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return calculer_base_imposable_prestations_tranche(personne, period, parameters, 12, 'it')
