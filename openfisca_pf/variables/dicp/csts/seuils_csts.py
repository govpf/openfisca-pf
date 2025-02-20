# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
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
from openfisca_pf.entities import Pays


class seuil_cst_s_tranche_1(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = 'Seuil de la CST-S pour la tranche 1'
    reference = [
        REFERENCE_CODE_LP_TAUX_CSTS,
        REFERENCE_LIEN_CODE,
        REFERENCE_LIEN_TAUX
        ]
    unit = XPF

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.cst_s.taux.thresholds[0]


class seuil_cst_s_tranche_2(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = 'Seuil de la CST-S pour la tranche 2'
    reference = [
        REFERENCE_CODE_LP_TAUX_CSTS,
        REFERENCE_LIEN_CODE,
        REFERENCE_LIEN_TAUX
        ]
    unit = XPF

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.cst_s.taux.thresholds[1]


class seuil_cst_s_tranche_3(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = 'Seuil de la CST-S pour la tranche 3'
    reference = [
        REFERENCE_CODE_LP_TAUX_CSTS,
        REFERENCE_LIEN_CODE,
        REFERENCE_LIEN_TAUX
        ]
    unit = XPF

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.cst_s.taux.thresholds[2]


class seuil_cst_s_tranche_4(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = 'Seuil de la CST-S pour la tranche 4'
    reference = [
        REFERENCE_CODE_LP_TAUX_CSTS,
        REFERENCE_LIEN_CODE,
        REFERENCE_LIEN_TAUX
        ]
    unit = XPF

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.cst_s.taux.thresholds[3]


class seuil_cst_s_tranche_5(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = 'Seuil de la CST-S pour la tranche 5'
    reference = [
        REFERENCE_CODE_LP_TAUX_CSTS,
        REFERENCE_LIEN_CODE,
        REFERENCE_LIEN_TAUX
        ]
    unit = XPF

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.cst_s.taux.thresholds[4]


class seuil_cst_s_tranche_6(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = 'Seuil de la CST-S pour la tranche 6'
    reference = [
        REFERENCE_CODE_LP_TAUX_CSTS,
        REFERENCE_LIEN_CODE,
        REFERENCE_LIEN_TAUX
        ]
    unit = XPF

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.cst_s.taux.thresholds[5]


class seuil_cst_s_tranche_7(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = 'Seuil de la CST-S pour la tranche 7'
    reference = [
        REFERENCE_CODE_LP_TAUX_CSTS,
        REFERENCE_LIEN_CODE,
        REFERENCE_LIEN_TAUX
        ]
    unit = XPF

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.cst_s.taux.thresholds[6]


class seuil_cst_s_tranche_8(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = 'Seuil de la CST-S pour la tranche 8'
    reference = [
        REFERENCE_CODE_LP_TAUX_CSTS,
        REFERENCE_LIEN_CODE,
        REFERENCE_LIEN_TAUX
        ]
    unit = XPF

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.cst_s.taux.thresholds[7]


class seuil_cst_s_tranche_9(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = 'Seuil de la CST-S pour la tranche 9'
    reference = [
        REFERENCE_CODE_LP_TAUX_CSTS,
        REFERENCE_LIEN_CODE,
        REFERENCE_LIEN_TAUX
        ]
    unit = XPF

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.cst_s.taux.thresholds[8]


class seuil_cst_s_tranche_10(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = 'Seuil de la CST-S pour la tranche 10'
    reference = [
        REFERENCE_CODE_LP_TAUX_CSTS,
        REFERENCE_LIEN_CODE,
        REFERENCE_LIEN_TAUX
        ]
    unit = XPF

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.cst_s.taux.thresholds[9]


class seuil_cst_s_tranche_11(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = 'Seuil de la CST-S pour la tranche 11'
    reference = [
        REFERENCE_CODE_LP_TAUX_CSTS,
        REFERENCE_LIEN_CODE,
        REFERENCE_LIEN_TAUX
        ]
    unit = XPF

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.cst_s.taux.thresholds[10]


class seuil_cst_s_tranche_12(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = 'Seuil de la CST-S pour la tranche 12'
    reference = [
        REFERENCE_CODE_LP_TAUX_CSTS,
        REFERENCE_LIEN_CODE,
        REFERENCE_LIEN_TAUX
        ]
    unit = XPF

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.cst_s.taux.thresholds[11]
