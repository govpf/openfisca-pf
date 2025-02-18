# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    Parameters,
    Period,
    Variable,
    where,
    YEAR
    )
from openfisca_pf.constants.units import PER_ONE
from openfisca_pf.entities import Pays


class nombre_tranches_it_ventes(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = """
    Nombre de tranches applicables à l'impôt sur les transactions de ventes.
    Attention, ce paramètre ne doit pas être modifié pour un calcul.
    Sa modification n'est possible que pour les simulations, et dans ce cas seule la première valeur de la simulation sera prise en compte.
    A modifier avec une extrème précaution !
    """
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return len(parameters(period).dicp.it.taux_ventes.rates)


class taux_it_ventes_tranche_1(Variable):
    entity = Pays
    definition_period = YEAR
    value_type = float
    label = "Taux de tranche 1 de l'impôt sur les transactions de ventes"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = PER_ONE

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        tranche = 0
        nombre_tranches_it_ventes = pays(f'nombre_tranches_it_ventes', period)
        rate = parameters(period).dicp.it.taux_ventes.rates[tranche] if len(parameters(period).dicp.it.taux_ventes.rates) > tranche else 0
        return where(nombre_tranches_it_ventes > tranche, rate, 0)


class taux_it_ventes_tranche_2(Variable):
    entity = Pays
    definition_period = YEAR
    value_type = float
    label = "Taux de tranche 2 de l'impôt sur les transactions de ventes"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = PER_ONE

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        tranche = 1
        nombre_tranches_it_ventes = pays(f'nombre_tranches_it_ventes', period)
        rate = parameters(period).dicp.it.taux_ventes.rates[tranche] if len(parameters(period).dicp.it.taux_ventes.rates) > tranche else 0
        return where(nombre_tranches_it_ventes > tranche, rate, 0)


class taux_it_ventes_tranche_3(Variable):
    entity = Pays
    definition_period = YEAR
    value_type = float
    label = "Taux de tranche 3 de l'impôt sur les transactions de ventes"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = PER_ONE

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        tranche = 2
        nombre_tranches_it_ventes = pays(f'nombre_tranches_it_ventes', period)
        rate = parameters(period).dicp.it.taux_ventes.rates[tranche] if len(parameters(period).dicp.it.taux_ventes.rates) > tranche else 0
        return where(nombre_tranches_it_ventes > tranche, rate, 0)


class taux_it_ventes_tranche_4(Variable):
    entity = Pays
    definition_period = YEAR
    value_type = float
    label = "Taux de tranche 4 de l'impôt sur les transactions de ventes"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = PER_ONE

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        tranche = 3
        nombre_tranches_it_ventes = pays(f'nombre_tranches_it_ventes', period)
        rate = parameters(period).dicp.it.taux_ventes.rates[tranche] if len(parameters(period).dicp.it.taux_ventes.rates) > tranche else 0
        return where(nombre_tranches_it_ventes > tranche, rate, 0)


class taux_it_ventes_tranche_5(Variable):
    entity = Pays
    definition_period = YEAR
    value_type = float
    label = "Taux de tranche 5 de l'impôt sur les transactions de ventes"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = PER_ONE

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        tranche = 4
        nombre_tranches_it_ventes = pays(f'nombre_tranches_it_ventes', period)
        rate = parameters(period).dicp.it.taux_ventes.rates[tranche] if len(parameters(period).dicp.it.taux_ventes.rates) > tranche else 0
        return where(nombre_tranches_it_ventes > tranche, rate, 0)


class taux_it_ventes_tranche_6(Variable):
    entity = Pays
    definition_period = YEAR
    value_type = float
    label = "Taux de tranche 6 de l'impôt sur les transactions de ventes"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = PER_ONE

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        tranche = 5
        nombre_tranches_it_ventes = pays(f'nombre_tranches_it_ventes', period)
        rate = parameters(period).dicp.it.taux_ventes.rates[tranche] if len(parameters(period).dicp.it.taux_ventes.rates) > tranche else 0
        return where(nombre_tranches_it_ventes > tranche, rate, 0)


class taux_it_ventes_tranche_7(Variable):
    entity = Pays
    definition_period = YEAR
    value_type = float
    label = "Taux de tranche 7 de l'impôt sur les transactions de ventes"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = PER_ONE

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        tranche = 6
        nombre_tranches_it_ventes = pays(f'nombre_tranches_it_ventes', period)
        rate = parameters(period).dicp.it.taux_ventes.rates[tranche] if len(parameters(period).dicp.it.taux_ventes.rates) > tranche else 0
        return where(nombre_tranches_it_ventes > tranche, rate, 0)


class taux_it_ventes_tranche_8(Variable):
    entity = Pays
    definition_period = YEAR
    value_type = float
    label = "Taux de tranche 8 de l'impôt sur les transactions de ventes"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = PER_ONE

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        tranche = 7
        nombre_tranches_it_ventes = pays(f'nombre_tranches_it_ventes', period)
        rate = parameters(period).dicp.it.taux_ventes.rates[tranche] if len(parameters(period).dicp.it.taux_ventes.rates) > tranche else 0
        return where(nombre_tranches_it_ventes > tranche, rate, 0)


class taux_it_ventes_tranche_9(Variable):
    entity = Pays
    definition_period = YEAR
    value_type = float
    label = "Taux de tranche 9 de l'impôt sur les transactions de ventes"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = PER_ONE

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        tranche = 8
        nombre_tranches_it_ventes = pays(f'nombre_tranches_it_ventes', period)
        rate = parameters(period).dicp.it.taux_ventes.rates[tranche] if len(parameters(period).dicp.it.taux_ventes.rates) > tranche else 0
        return where(nombre_tranches_it_ventes > tranche, rate, 0)


class taux_it_ventes_tranche_10(Variable):
    entity = Pays
    definition_period = YEAR
    value_type = float
    default_value = 0.
    label = "Taux de tranche 10 de l'impôt sur les transactions de ventes [simulation]"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = PER_ONE

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        tranche = 9
        nombre_tranches_it_ventes = pays(f'nombre_tranches_it_ventes', period)
        rate = parameters(period).dicp.it.taux_ventes.rates[tranche] if len(parameters(period).dicp.it.taux_ventes.rates) > tranche else 0
        return where(nombre_tranches_it_ventes > tranche, rate, 0)


class taux_it_ventes_tranche_11(Variable):
    entity = Pays
    definition_period = YEAR
    value_type = float
    default_value = 0.
    label = "Taux de tranche 11 de l'impôt sur les transactions de ventes [simulation]"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = PER_ONE

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        tranche = 10
        nombre_tranches_it_ventes = pays(f'nombre_tranches_it_ventes', period)
        rate = parameters(period).dicp.it.taux_ventes.rates[tranche] if len(parameters(period).dicp.it.taux_ventes.rates) > tranche else 0
        return where(nombre_tranches_it_ventes > tranche, rate, 0)


class taux_it_ventes_tranche_12(Variable):
    entity = Pays
    definition_period = YEAR
    value_type = float
    default_value = 0.
    label = "Taux de tranche 12 de l'impôt sur les transactions de ventes [simulation]"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = PER_ONE

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        tranche = 11
        nombre_tranches_it_ventes = pays(f'nombre_tranches_it_ventes', period)
        rate = parameters(period).dicp.it.taux_ventes.rates[tranche] if len(parameters(period).dicp.it.taux_ventes.rates) > tranche else 0
        return where(nombre_tranches_it_ventes > tranche, rate, 0)
