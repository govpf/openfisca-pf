# -*- coding: utf-8 -*-

from openfisca_pf.base import (
    ArrayLike,
    floor,
    max_,
    MONTH,
    Parameters,
    Period,
    Variable
    )
from openfisca_pf.constants.dicp.references_csts import (
    REFERENCE_CODE_LP_TAUX_CSTS,
    REFERENCE_LIEN_CODE,
    REFERENCE_LIEN_TAUX
    )
from openfisca_pf.constants.units import XPF
from openfisca_pf.entities import Personne


class cst_s_due_tranche_1(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = "CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 1"
    reference = [
        REFERENCE_CODE_LP_TAUX_CSTS,
        REFERENCE_LIEN_CODE,
        REFERENCE_LIEN_TAUX
        ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        revenus_tranche_1 = personne('revenus_tranche_1', period, parameters)
        taux_tranche_1 = personne.pays('taux_cst_s_tranche_1', period, parameters)
        cst_s_tranche_1 = taux_tranche_1 * max_(revenus_tranche_1, 0)
        return floor(cst_s_tranche_1)


class cst_s_due_tranche_2(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = "CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 2"
    reference = [
        REFERENCE_CODE_LP_TAUX_CSTS,
        REFERENCE_LIEN_CODE,
        REFERENCE_LIEN_TAUX
        ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        revenus_tranche_2 = personne('revenus_tranche_2', period, parameters)
        taux_tranche_2 = personne.pays('taux_cst_s_tranche_2', period, parameters)
        cst_s_tranche_2 = taux_tranche_2 * max_(revenus_tranche_2, 0)
        return floor(cst_s_tranche_2)


class cst_s_due_tranche_3(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = "CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 3"
    reference = [
        REFERENCE_CODE_LP_TAUX_CSTS,
        REFERENCE_LIEN_CODE,
        REFERENCE_LIEN_TAUX
        ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        revenus_tranche_3 = personne('revenus_tranche_3', period, parameters)
        taux_tranche_3 = personne.pays('taux_cst_s_tranche_3', period, parameters)
        cst_s_tranche_3 = taux_tranche_3 * max_(revenus_tranche_3, 0)
        return floor(cst_s_tranche_3)


class cst_s_due_tranche_4(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = "CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 4"
    reference = [
        REFERENCE_CODE_LP_TAUX_CSTS,
        REFERENCE_LIEN_CODE,
        REFERENCE_LIEN_TAUX
        ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        revenus_tranche_4 = personne('revenus_tranche_4', period, parameters)
        taux_tranche_4 = personne.pays('taux_cst_s_tranche_4', period, parameters)
        cst_s_tranche_4 = taux_tranche_4 * max_(revenus_tranche_4, 0)
        return floor(cst_s_tranche_4)


class cst_s_due_tranche_5(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = "CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 5"
    reference = [
        REFERENCE_CODE_LP_TAUX_CSTS,
        REFERENCE_LIEN_CODE,
        REFERENCE_LIEN_TAUX
        ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        revenus_tranche_5 = personne('revenus_tranche_5', period, parameters)
        taux_tranche_5 = personne.pays('taux_cst_s_tranche_5', period, parameters)
        cst_s_tranche_5 = taux_tranche_5 * max_(revenus_tranche_5, 0)
        return floor(cst_s_tranche_5)


class cst_s_due_tranche_6(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = "CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 6"
    reference = [
        REFERENCE_CODE_LP_TAUX_CSTS,
        REFERENCE_LIEN_CODE,
        REFERENCE_LIEN_TAUX
        ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        revenus_tranche_6 = personne('revenus_tranche_6', period, parameters)
        taux_tranche_6 = personne.pays('taux_cst_s_tranche_6', period, parameters)
        cst_s_tranche_6 = taux_tranche_6 * max_(revenus_tranche_6, 0)
        return floor(cst_s_tranche_6)


class cst_s_due_tranche_7(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = "CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 7"
    reference = [
        REFERENCE_CODE_LP_TAUX_CSTS,
        REFERENCE_LIEN_CODE,
        REFERENCE_LIEN_TAUX
        ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        revenus_tranche_7 = personne('revenus_tranche_7', period, parameters)
        taux_tranche_7 = personne.pays('taux_cst_s_tranche_7', period, parameters)
        cst_s_tranche_7 = taux_tranche_7 * max_(revenus_tranche_7, 0)
        return floor(cst_s_tranche_7)


class cst_s_due_tranche_8(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = "CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 8"
    reference = [
        REFERENCE_CODE_LP_TAUX_CSTS,
        REFERENCE_LIEN_CODE,
        REFERENCE_LIEN_TAUX
        ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        revenus_tranche_8 = personne('revenus_tranche_8', period, parameters)
        taux_tranche_8 = personne.pays('taux_cst_s_tranche_8', period, parameters)
        cst_s_tranche_8 = taux_tranche_8 * max_(revenus_tranche_8, 0)
        return floor(cst_s_tranche_8)


class cst_s_due_tranche_9(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = "CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 9"
    reference = [
        REFERENCE_CODE_LP_TAUX_CSTS,
        REFERENCE_LIEN_CODE,
        REFERENCE_LIEN_TAUX
        ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        revenus_tranche_9 = personne('revenus_tranche_9', period, parameters)
        taux_tranche_9 = personne.pays('taux_cst_s_tranche_9', period, parameters)
        cst_s_tranche_9 = taux_tranche_9 * max_(revenus_tranche_9, 0)
        return floor(cst_s_tranche_9)


class cst_s_due_tranche_10(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = "CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 10"
    reference = [
        REFERENCE_CODE_LP_TAUX_CSTS,
        REFERENCE_LIEN_CODE,
        REFERENCE_LIEN_TAUX
        ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        revenus_tranche_10 = personne('revenus_tranche_10', period, parameters)
        taux_tranche_10 = personne.pays('taux_cst_s_tranche_10', period, parameters)
        cst_s_tranche_10 = taux_tranche_10 * max_(revenus_tranche_10, 0)
        return floor(cst_s_tranche_10)


class cst_s_due_tranche_11(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = "CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 11"
    reference = [
        REFERENCE_CODE_LP_TAUX_CSTS,
        REFERENCE_LIEN_CODE,
        REFERENCE_LIEN_TAUX
        ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        revenus_tranche_11 = personne('revenus_tranche_11', period, parameters)
        taux_tranche_11 = personne.pays('taux_cst_s_tranche_11', period, parameters)
        cst_s_tranche_11 = taux_tranche_11 * max_(revenus_tranche_11, 0)
        return floor(cst_s_tranche_11)


class cst_s_due_tranche_12(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = "CST-S due par l'entreprise sur l'ensemble des salaires déclarés sur la tranche 12"
    reference = [
        REFERENCE_CODE_LP_TAUX_CSTS,
        REFERENCE_LIEN_CODE,
        REFERENCE_LIEN_TAUX
        ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        revenus_tranche_12 = personne('revenus_tranche_12', period, parameters)
        taux_tranche_12 = personne.pays('taux_cst_s_tranche_12', period, parameters)
        cst_s_tranche_12 = taux_tranche_12 * max_(revenus_tranche_12, 0)
        return floor(cst_s_tranche_12)
