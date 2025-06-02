# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    GroupPopulation,
    ParameterNode,
    Period,
    Variable,
    YEAR
    )
from openfisca_pf.entities import Pays


class nombre_entreprises_redevables_cstns_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = "Nombre d'entreprises du pays redevables de la CST-NS"

    def formula(pays: GroupPopulation, period: Period, parameters: ParameterNode) -> ArrayLike:
        redevables = pays.members('redevable_cstns', period)
        return pays.sum(redevables * 1)


class nombre_entreprises_redevables_cstns_tranche_1_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = "Nombre d'entreprises du pays redevables de la CST-NS dont les revenus sont imposables à la tranche 1"

    def formula(pays: GroupPopulation, period: Period, parameters: ParameterNode) -> ArrayLike:
        redevables = pays.members('montant_du_cstns_tranche_1', period)
        return pays.sum((redevables > 0) * 1)


class nombre_entreprises_redevables_cstns_tranche_2_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = "Nombre d'entreprises du pays redevables de la CST-NS dont les revenus sont imposables à la tranche 2"

    def formula(pays: GroupPopulation, period: Period, parameters: ParameterNode) -> ArrayLike:
        redevables = pays.members('montant_du_cstns_tranche_2', period)
        return pays.sum((redevables > 0) * 1)


class nombre_entreprises_redevables_cstns_tranche_3_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = "Nombre d'entreprises du pays redevables de la CST-NS dont les revenus sont imposables à la tranche 3"

    def formula(pays: GroupPopulation, period: Period, parameters: ParameterNode) -> ArrayLike:
        redevables = pays.members('montant_du_cstns_tranche_3', period)
        return pays.sum((redevables > 0) * 1)


class nombre_entreprises_redevables_cstns_tranche_4_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = "Nombre d'entreprises du pays redevables de la CST-NS dont les revenus sont imposables à la tranche 4"

    def formula(pays: GroupPopulation, period: Period, parameters: ParameterNode) -> ArrayLike:
        redevables = pays.members('montant_du_cstns_tranche_4', period)
        return pays.sum((redevables > 0) * 1)


class nombre_entreprises_redevables_cstns_tranche_5_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = "Nombre d'entreprises du pays redevables de la CST-NS dont les revenus sont imposables à la tranche 5"

    def formula(pays: GroupPopulation, period: Period, parameters: ParameterNode) -> ArrayLike:
        redevables = pays.members('montant_du_cstns_tranche_5', period)
        return pays.sum((redevables > 0) * 1)


class nombre_entreprises_redevables_cstns_tranche_6_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = "Nombre d'entreprises du pays redevables de la CST-NS dont les revenus sont imposables à la tranche 6"

    def formula(pays: GroupPopulation, period: Period, parameters: ParameterNode) -> ArrayLike:
        redevables = pays.members('montant_du_cstns_tranche_6', period)
        return pays.sum((redevables > 0) * 1)


class nombre_entreprises_redevables_cstns_tranche_7_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = "Nombre d'entreprises du pays redevables de la CST-NS dont les revenus sont imposables à la tranche 7"

    def formula(pays: GroupPopulation, period: Period, parameters: ParameterNode) -> ArrayLike:
        redevables = pays.members('montant_du_cstns_tranche_7', period)
        return pays.sum((redevables > 0) * 1)


class nombre_entreprises_redevables_cstns_tranche_8_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = "Nombre d'entreprises du pays redevables de la CST-NS dont les revenus sont imposables à la tranche 8"

    def formula(pays: GroupPopulation, period: Period, parameters: ParameterNode) -> ArrayLike:
        redevables = pays.members('montant_du_cstns_tranche_8', period)
        return pays.sum((redevables > 0) * 1)


class nombre_entreprises_redevables_cstns_tranche_9_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = "Nombre d'entreprises du pays redevables de la CST-NS dont les revenus sont imposables à la tranche 9"

    def formula(pays: GroupPopulation, period: Period, parameters: ParameterNode) -> ArrayLike:
        redevables = pays.members('montant_du_cstns_tranche_9', period)
        return pays.sum((redevables > 0) * 1)


class nombre_entreprises_redevables_cstns_tranche_10_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = "Nombre d'entreprises du pays redevables de la CST-NS dont les revenus sont imposables à la tranche 10"

    def formula(pays: GroupPopulation, period: Period, parameters: ParameterNode) -> ArrayLike:
        redevables = pays.members('montant_du_cstns_tranche_10', period)
        return pays.sum((redevables > 0) * 1)


class nombre_entreprises_redevables_cstns_tranche_11_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = "Nombre d'entreprises du pays redevables de la CST-NS dont les revenus sont imposables à la tranche 11"

    def formula(pays: GroupPopulation, period: Period, parameters: ParameterNode) -> ArrayLike:
        redevables = pays.members('montant_du_cstns_tranche_11', period)
        return pays.sum((redevables > 0) * 1)


class nombre_entreprises_redevables_cstns_tranche_12_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = "Nombre d'entreprises du pays redevables de la CST-NS dont les revenus sont imposables à la tranche 12"

    def formula(pays: GroupPopulation, period: Period, parameters: ParameterNode) -> ArrayLike:
        redevables = pays.members('montant_du_cstns_tranche_12', period)
        return pays.sum((redevables > 0) * 1)


class montant_cstns_total_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = 'Montant total de CST-NS du par les entreprises du pays'

    def formula(pays: GroupPopulation, period: Period, parameters: ParameterNode) -> ArrayLike:
        it_du = pays.members('montant_cstns_du', period)
        return pays.sum(it_du)
