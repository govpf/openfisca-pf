# -*- coding: utf-8 -*-

from openfisca_pf.base import (
    ArrayLike,
    Parameters,
    Period,
    Variable,
    YEAR
    )
from openfisca_pf.entities import Pays


class nombre_entreprises_redevables_IT_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = "Nombre d'entreprises du pays redevables de l'impôt sur les transactions"

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        redevable_it = pays.members('redevable_it', period, parameters)
        return pays.sum(redevable_it * 1)


class nombre_entreprises_redevables_it_tranche_1_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = "Nombre d'entreprises du pays redevables de l'impôt sur les transactions dont les revenus sont imposables à la tranche 1"

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        montant_du_it_tranche_1 = pays.members('montant_du_it_tranche_1', period, parameters)
        return pays.sum((montant_du_it_tranche_1 > 0) * 1)


class nombre_entreprises_redevables_it_tranche_2_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = "Nombre d'entreprises du pays redevables de l'impôt sur les transactions dont les revenus sont imposables à la tranche 2"

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        montant_du_it_tranche_2 = pays.members('montant_du_it_tranche_2', period, parameters)
        return pays.sum((montant_du_it_tranche_2 > 0) * 1)


class nombre_entreprises_redevables_it_tranche_3_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = "Nombre d'entreprises du pays redevables de l'impôt sur les transactions dont les revenus sont imposables à la tranche 3"

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        montant_du_it_tranche_3 = pays.members('montant_du_it_tranche_3', period, parameters)
        return pays.sum((montant_du_it_tranche_3 > 0) * 1)


class nombre_entreprises_redevables_it_tranche_4_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = "Nombre d'entreprises du pays redevables de l'impôt sur les transactions dont les revenus sont imposables à la tranche 4"

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        montant_du_it_tranche_4 = pays.members('montant_du_it_tranche_4', period, parameters)
        return pays.sum((montant_du_it_tranche_4 > 0) * 1)


class nombre_entreprises_redevables_it_tranche_5_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = "Nombre d'entreprises du pays redevables de l'impôt sur les transactions dont les revenus sont imposables à la tranche 5"

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        montant_du_it_tranche_5 = pays.members('montant_du_it_tranche_5', period, parameters)
        return pays.sum((montant_du_it_tranche_5 > 0) * 1)


class nombre_entreprises_redevables_it_tranche_6_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = "Nombre d'entreprises du pays redevables de l'impôt sur les transactions dont les revenus sont imposables à la tranche 6"

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        montant_du_it_tranche_6 = pays.members('montant_du_it_tranche_6', period, parameters)
        return pays.sum((montant_du_it_tranche_6 > 0) * 1)


class nombre_entreprises_redevables_it_tranche_7_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = "Nombre d'entreprises du pays redevables de l'impôt sur les transactions dont les revenus sont imposables à la tranche 7"

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        montant_du_it_tranche_7 = pays.members('montant_du_it_tranche_7', period, parameters)
        return pays.sum((montant_du_it_tranche_7 > 0) * 1)


class nombre_entreprises_redevables_it_tranche_8_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = "Nombre d'entreprises du pays redevables de l'impôt sur les transactions dont les revenus sont imposables à la tranche 8"

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        montant_du_it_tranche_8 = pays.members('montant_du_it_tranche_8', period, parameters)
        return pays.sum((montant_du_it_tranche_8 > 0) * 1)


class nombre_entreprises_redevables_it_tranche_9_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = "Nombre d'entreprises du pays redevables de l'impôt sur les transactions dont les revenus sont imposables à la tranche 9"

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        montant_du_it_tranche_9 = pays.members('montant_du_it_tranche_9', period, parameters)
        return pays.sum((montant_du_it_tranche_9 > 0) * 1)


class nombre_entreprises_redevables_it_tranche_10_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = "Nombre d'entreprises du pays redevables de l'impôt sur les transactions dont les revenus sont imposables à la tranche 10"

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        montant_du_it_tranche_10 = pays.members('montant_du_it_tranche_10', period, parameters)
        return pays.sum((montant_du_it_tranche_10 > 0) * 1)


class nombre_entreprises_redevables_it_tranche_11_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = "Nombre d'entreprises du pays redevables de l'impôt sur les transactions dont les revenus sont imposables à la tranche 11"

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        montant_du_it_tranche_11 = pays.members('montant_du_it_tranche_11', period, parameters)
        return pays.sum((montant_du_it_tranche_11 > 0) * 1)


class nombre_entreprises_redevables_it_tranche_12_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = "Nombre d'entreprises du pays redevables de l'impôt sur les transactions dont les revenus sont imposables à la tranche 12"

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        montant_du_it_tranche_12 = pays.members('montant_du_it_tranche_12', period, parameters)
        return pays.sum((montant_du_it_tranche_12 > 0) * 1)
