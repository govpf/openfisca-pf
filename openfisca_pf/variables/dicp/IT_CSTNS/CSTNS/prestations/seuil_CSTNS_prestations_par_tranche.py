# -*- coding: utf-8 -*-

from openfisca_pf.base import (
    ArrayLike,
    Parameters,
    Period,
    Variable,
    YEAR
    )
from openfisca_pf.entities import Pays


class seuil_cstns_prestations_tranche_1(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = "Seuil de tranche 1 de la CST-NS sur les ventes"
    reference = [
        "https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot",
        "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"
        ]

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.cstns.taux_prestations.thresholds[0]


class seuil_cstns_prestations_tranche_2(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = "Seuil de tranche 2 de la CST-NS sur les ventes"
    reference = [
        "https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot",
        "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"
        ]

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.cstns.taux_prestations.thresholds[1]


class seuil_cstns_prestations_tranche_3(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = "Seuil de tranche 3 de la CST-NS sur les ventes"
    reference = [
        "https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot",
        "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"
        ]

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.cstns.taux_prestations.thresholds[2]


class seuil_cstns_prestations_tranche_4(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = "Seuil de tranche 4 de la CST-NS sur les ventes"
    reference = [
        "https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot",
        "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"
        ]

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.cstns.taux_prestations.thresholds[3]


class seuil_cstns_prestations_tranche_5(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = "Seuil de tranche 5 de la CST-NS sur les ventes"
    reference = [
        "https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot",
        "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"
        ]

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.cstns.taux_prestations.thresholds[4]


class seuil_cstns_prestations_tranche_6(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = "Seuil de tranche 6 de la CST-NS sur les ventes"
    reference = [
        "https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot",
        "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"
        ]

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.cstns.taux_prestations.thresholds[5]


class seuil_cstns_prestations_tranche_7(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = "Seuil de tranche 7 de la CST-NS sur les ventes"
    reference = [
        "https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot",
        "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"
        ]

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.cstns.taux_prestations.thresholds[6]


class seuil_cstns_prestations_tranche_8(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = "Seuil de tranche 8 de la CST-NS sur les ventes"
    reference = [
        "https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot",
        "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"
        ]

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.cstns.taux_prestations.thresholds[8]


class seuil_cstns_prestations_tranche_9(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = "Seuil de tranche 9 de la CST-NS sur les ventes"
    reference = [
        "https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot",
        "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"
        ]

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.cstns.taux_prestations.thresholds[8]


class seuil_cstns_prestations_tranche_10(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = "Seuil de tranche 10 de la CST-NS sur les ventes"
    reference = [
        "https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot",
        "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"
        ]

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.cstns.taux_prestations.thresholds[9]


class seuil_cstns_prestations_tranche_11(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = "Seuil de tranche 11 de la CST-NS sur les ventes"
    reference = [
        "https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot",
        "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"
        ]

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.cstns.taux_prestations.thresholds[10]


class seuil_cstns_prestations_tranche_12(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = "Seuil de tranche 12 de la CST-NS sur les ventes"
    reference = [
        "https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot",
        "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"
        ]

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.cstns.taux_prestations.thresholds[11]
