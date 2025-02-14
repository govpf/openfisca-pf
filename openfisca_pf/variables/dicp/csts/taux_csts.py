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
from openfisca_pf.constants.units import PER_ONE
from openfisca_pf.entities import Pays


class nombre_tranches_cst_s(Variable):
    value_type = int
    entity = Pays
    definition_period = MONTH
    reference = [
        REFERENCE_CODE_LP_TAUX_CSTS,
        REFERENCE_LIEN_CODE,
        REFERENCE_LIEN_TAUX
        ]
    label = """
    Nombre de tranches de CST-S.
    Attention, ce paramètre ne DOIT PAS être modifié pour un calcul.
    Sa modification n'est possible que pour les simulations, et dans ce cas seule la première valeur de la simulation sera prise en compte.
    A modifier avec une extrême précaution !
    """

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return len(parameters(period).dicp.cst_s.taux.rates)


class taux_cst_s_tranche_1(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = 'Taux de la CST-S pour la tranche 1'
    reference = [
        REFERENCE_CODE_LP_TAUX_CSTS,
        REFERENCE_LIEN_CODE,
        REFERENCE_LIEN_TAUX
    ]
    unit = PER_ONE

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.cst_s.taux.rates[0]


class taux_cst_s_tranche_2(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = 'Taux de la CST-S pour la tranche 2'
    reference = [
        REFERENCE_CODE_LP_TAUX_CSTS,
        REFERENCE_LIEN_CODE,
        REFERENCE_LIEN_TAUX
    ]
    unit = PER_ONE

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.cst_s.taux.rates[1]


class taux_cst_s_tranche_3(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = 'Taux de la CST-S pour la tranche 3'
    reference = [
        REFERENCE_CODE_LP_TAUX_CSTS,
        REFERENCE_LIEN_CODE,
        REFERENCE_LIEN_TAUX
    ]
    unit = PER_ONE

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.cst_s.taux.rates[2]


class taux_cst_s_tranche_4(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = 'Taux de la CST-S pour la tranche 4'
    reference = [
        REFERENCE_CODE_LP_TAUX_CSTS,
        REFERENCE_LIEN_CODE,
        REFERENCE_LIEN_TAUX
    ]
    unit = PER_ONE

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.cst_s.taux.rates[3]


class taux_cst_s_tranche_5(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = 'Taux de la CST-S pour la tranche 5'
    reference = [
        REFERENCE_CODE_LP_TAUX_CSTS,
        REFERENCE_LIEN_CODE,
        REFERENCE_LIEN_TAUX
    ]
    unit = PER_ONE

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.cst_s.taux.rates[4]


class taux_cst_s_tranche_6(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = 'Taux de la CST-S pour la tranche 6'
    reference = [
        REFERENCE_CODE_LP_TAUX_CSTS,
        REFERENCE_LIEN_CODE,
        REFERENCE_LIEN_TAUX
    ]
    unit = PER_ONE

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.cst_s.taux.rates[5]


class taux_cst_s_tranche_7(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = 'Taux de la CST-S pour la tranche 7'
    reference = [
        REFERENCE_CODE_LP_TAUX_CSTS,
        REFERENCE_LIEN_CODE,
        REFERENCE_LIEN_TAUX
    ]
    unit = PER_ONE

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.cst_s.taux.rates[6]


class taux_cst_s_tranche_8(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = 'Taux de la CST-S pour la tranche 8'
    reference = [
        REFERENCE_CODE_LP_TAUX_CSTS,
        REFERENCE_LIEN_CODE,
        REFERENCE_LIEN_TAUX
    ]
    unit = PER_ONE

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.cst_s.taux.rates[7]


class taux_cst_s_tranche_9(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = 'Taux de la CST-S pour la tranche 9'
    reference = [
        REFERENCE_CODE_LP_TAUX_CSTS,
        REFERENCE_LIEN_CODE,
        REFERENCE_LIEN_TAUX
    ]
    unit = PER_ONE

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.cst_s.taux.rates[8]


class taux_cst_s_tranche_10(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = 'Taux de la CST-S pour la tranche 10'
    reference = [
        REFERENCE_CODE_LP_TAUX_CSTS,
        REFERENCE_LIEN_CODE,
        REFERENCE_LIEN_TAUX
    ]
    unit = PER_ONE

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.cst_s.taux.rates[9]


class taux_cst_s_tranche_11(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = 'Taux de la CST-S pour la tranche 11'
    reference = [
        REFERENCE_CODE_LP_TAUX_CSTS,
        REFERENCE_LIEN_CODE,
        REFERENCE_LIEN_TAUX
    ]
    unit = PER_ONE

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.cst_s.taux.rates[10]


class taux_cst_s_tranche_12(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = 'Taux de la CST-S pour la tranche 12'
    reference = [
        REFERENCE_CODE_LP_TAUX_CSTS,
        REFERENCE_LIEN_CODE,
        REFERENCE_LIEN_TAUX
    ]
    unit = PER_ONE

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.cst_s.taux.rates[11]
