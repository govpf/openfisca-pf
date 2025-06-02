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


class nombre_tranches_it_prestations(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = """
    Nombre de tranches applicables à l'impôt sur les transactions de prestations.
    Attention, ce paramètre ne doit pas être modifié pour un calcul.
    Sa modification n'est possible que pour les simulations, et dans ce cas seule la première valeur de la simulation sera prise en compte.
    A modifier avec une extrème précaution !
    """
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return len(parameters(period).dicp.it.taux_prestations.rates)


class taux_it_prestations_tranche_1(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = "Taux de tranche 1 de l'impôt sur les transactions de prestations"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = PER_ONE

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        nombre_tranches_it_prestations = pays('nombre_tranches_it_prestations', period, parameters)
        tranche = 0
        rate = parameters(period).dicp.it.taux_prestations.rates[tranche] if len(parameters(period).dicp.it.taux_prestations.rates) > tranche else 0.
        return where(tranche < nombre_tranches_it_prestations, rate, 0.)


class taux_it_prestations_tranche_2(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = "Taux de tranche 2 de l'impôt sur les transactions de prestations"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = PER_ONE

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        nombre_tranches_it_prestations = pays('nombre_tranches_it_prestations', period, parameters)
        tranche = 1
        rate = parameters(period).dicp.it.taux_prestations.rates[tranche] if len(parameters(period).dicp.it.taux_prestations.rates) > tranche else 0.
        return where(tranche < nombre_tranches_it_prestations, rate, 0.)


class taux_it_prestations_tranche_3(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = "Taux de tranche 3 de l'impôt sur les transactions de prestations"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = PER_ONE

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        nombre_tranches_it_prestations = pays('nombre_tranches_it_prestations', period, parameters)
        tranche = 2
        rate = parameters(period).dicp.it.taux_prestations.rates[tranche] if len(parameters(period).dicp.it.taux_prestations.rates) > tranche else 0.
        return where(tranche < nombre_tranches_it_prestations, rate, 0.)


class taux_it_prestations_tranche_4(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = "Taux de tranche 4 de l'impôt sur les transactions de prestations"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = PER_ONE

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        nombre_tranches_it_prestations = pays('nombre_tranches_it_prestations', period, parameters)
        tranche = 3
        rate = parameters(period).dicp.it.taux_prestations.rates[tranche] if len(parameters(period).dicp.it.taux_prestations.rates) > tranche else 0.
        return where(tranche < nombre_tranches_it_prestations, rate, 0.)


class taux_it_prestations_tranche_5(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = "Taux de tranche 5 de l'impôt sur les transactions de prestations"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = PER_ONE

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        nombre_tranches_it_prestations = pays('nombre_tranches_it_prestations', period, parameters)
        tranche = 4
        rate = parameters(period).dicp.it.taux_prestations.rates[tranche] if len(parameters(period).dicp.it.taux_prestations.rates) > tranche else 0.
        return where(tranche < nombre_tranches_it_prestations, rate, 0.)


class taux_it_prestations_tranche_6(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = "Taux de tranche 6 de l'impôt sur les transactions de prestations"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = PER_ONE

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        nombre_tranches_it_prestations = pays('nombre_tranches_it_prestations', period, parameters)
        tranche = 5
        rate = parameters(period).dicp.it.taux_prestations.rates[tranche] if len(parameters(period).dicp.it.taux_prestations.rates) > tranche else 0.
        return where(tranche < nombre_tranches_it_prestations, rate, 0.)


class taux_it_prestations_tranche_7(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = "Taux de tranche 7 de l'impôt sur les transactions de prestations"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = PER_ONE

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        nombre_tranches_it_prestations = pays('nombre_tranches_it_prestations', period, parameters)
        tranche = 6
        rate = parameters(period).dicp.it.taux_prestations.rates[tranche] if len(parameters(period).dicp.it.taux_prestations.rates) > tranche else 0.
        return where(tranche < nombre_tranches_it_prestations, rate, 0.)


class taux_it_prestations_tranche_8(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = "Taux de tranche 8 de l'impôt sur les transactions de prestations"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = PER_ONE

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        nombre_tranches_it_prestations = pays('nombre_tranches_it_prestations', period, parameters)
        tranche = 7
        rate = parameters(period).dicp.it.taux_prestations.rates[tranche] if len(parameters(period).dicp.it.taux_prestations.rates) > tranche else 0.
        return where(tranche < nombre_tranches_it_prestations, rate, 0.)


class taux_it_prestations_tranche_9(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = "Taux de tranche 9 de l'impôt sur les transactions de prestations"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = PER_ONE

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        nombre_tranches_it_prestations = pays('nombre_tranches_it_prestations', period, parameters)
        tranche = 8
        rate = parameters(period).dicp.it.taux_prestations.rates[tranche] if len(parameters(period).dicp.it.taux_prestations.rates) > tranche else 0.
        return where(tranche < nombre_tranches_it_prestations, rate, 0.)


class taux_it_prestations_tranche_10(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = "Taux de tranche 10 de l'impôt sur les transactions de prestations"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = PER_ONE

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        nombre_tranches_it_prestations = pays('nombre_tranches_it_prestations', period, parameters)
        tranche = 9
        rate = parameters(period).dicp.it.taux_prestations.rates[tranche] if len(parameters(period).dicp.it.taux_prestations.rates) > tranche else 0.
        return where(tranche < nombre_tranches_it_prestations, rate, 0.)


class taux_it_prestations_tranche_11(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = "Taux de tranche 11 de l'impôt sur les transactions de prestations"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = PER_ONE

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        nombre_tranches_it_prestations = pays('nombre_tranches_it_prestations', period, parameters)
        tranche = 10
        rate = parameters(period).dicp.it.taux_prestations.rates[tranche] if len(parameters(period).dicp.it.taux_prestations.rates) > tranche else 0.
        return where(tranche < nombre_tranches_it_prestations, rate, 0.)


class taux_it_prestations_tranche_12(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = "Taux de tranche 12 de l'impôt sur les transactions de prestations"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = PER_ONE

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        nombre_tranches_it_prestations = pays('nombre_tranches_it_prestations', period, parameters)
        tranche = 11
        rate = parameters(period).dicp.it.taux_prestations.rates[tranche] if len(parameters(period).dicp.it.taux_prestations.rates) > tranche else 0.
        return where(tranche < nombre_tranches_it_prestations, rate, 0.)
