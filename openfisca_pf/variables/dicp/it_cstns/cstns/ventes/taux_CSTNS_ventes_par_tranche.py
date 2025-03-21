# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    GroupPopulation,
    ParameterNode,
    Period,
    Variable,
    YEAR
    )
from openfisca_pf.constants.units import PER_ONE
from openfisca_pf.entities import Pays


class nombre_tranches_cstns_ventes(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = """
    Nombre de tranches applicables sur la CST-NS des ventes.
    Attention, ce paramètre ne doit pas être modifié pour un calcul.
    Sa modification n'est possible que pour les simulations, et dans ce cas seule la première valeur de la simulation sera prise en compte.
    A modifier avec une extrème précaution !
    """
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]

    def formula(pays: GroupPopulation, period: Period, parameters: ParameterNode) -> ArrayLike:
        return len(parameters(period).dicp.cstns.taux_ventes.rates)


class taux_cstns_ventes_tranche_1(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = 'Taux de tranche 1 de la CST-NS sur les ventes'
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = PER_ONE

    def formula(pays: GroupPopulation, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.cstns.taux_ventes.rates[0]


class taux_cstns_ventes_tranche_2(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = 'Taux de tranche 2 de la CST-NS sur les ventes'
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = PER_ONE

    def formula(pays: GroupPopulation, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.cstns.taux_ventes.rates[1]


class taux_cstns_ventes_tranche_3(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = 'Taux de tranche 3 de la CST-NS sur les ventes'
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = PER_ONE

    def formula(pays: GroupPopulation, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.cstns.taux_ventes.rates[2]


class taux_cstns_ventes_tranche_4(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = 'Taux de tranche 4 de la CST-NS sur les ventes'
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = PER_ONE

    def formula(pays: GroupPopulation, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.cstns.taux_ventes.rates[3]


class taux_cstns_ventes_tranche_5(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = 'Taux de tranche 5 de la CST-NS sur les ventes'
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = PER_ONE

    def formula(pays: GroupPopulation, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.cstns.taux_ventes.rates[4]


class taux_cstns_ventes_tranche_6(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = 'Taux de tranche 6 de la CST-NS sur les ventes'
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = PER_ONE

    def formula(pays: GroupPopulation, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.cstns.taux_ventes.rates[5]


class taux_cstns_ventes_tranche_7(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = 'Taux de tranche 7 de la CST-NS sur les ventes'
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = PER_ONE

    def formula(pays: GroupPopulation, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.cstns.taux_ventes.rates[6]


class taux_cstns_ventes_tranche_8(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = 'Taux de tranche 8 de la CST-NS sur les ventes'
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = PER_ONE

    def formula(pays: GroupPopulation, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.cstns.taux_ventes.rates[7]


class taux_cstns_ventes_tranche_9(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = 'Taux de tranche 9 de la CST-NS sur les ventes'
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = PER_ONE

    def formula(pays: GroupPopulation, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.cstns.taux_ventes.rates[8]


class taux_cstns_ventes_tranche_10(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = 'Taux de tranche 10 de la CST-NS sur les ventes'
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = PER_ONE

    def formula(pays: GroupPopulation, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.cstns.taux_ventes.rates[9]


class taux_cstns_ventes_tranche_11(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = 'Taux de tranche 11 de la CST-NS sur les ventes'
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = PER_ONE

    def formula(pays: GroupPopulation, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.cstns.taux_ventes.rates[10]


class taux_cstns_ventes_tranche_12(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = 'Taux de tranche 12 de la CST-NS sur les ventes'
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = PER_ONE

    def formula(pays: GroupPopulation, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.cstns.taux_ventes.rates[11]
