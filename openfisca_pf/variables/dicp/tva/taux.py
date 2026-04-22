# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    Population,
    MONTH,
    ParameterNode,
    Period,
    set_input_divide_by_period,
    YEAR,
    Variable,
    where
)
from openfisca_pf.constants import units
from openfisca_pf.entities import Personne


class taux_tva_reduit(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = "Taux de TVA réduit"
    set_input = set_input_divide_by_period
    unit = units.PER_ONE
    reference = [
        "https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot",
        "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"
    ]

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        taux_annee = personne('taux_tva_reduit_annee', period.this_year)
        return where(taux_annee, taux_annee, parameters(period).dicp.tva.taux.reduit)


class taux_tva_intermediaire(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = "Taux de TVA intermédiaire"
    set_input = set_input_divide_by_period
    unit = units.PER_ONE
    reference = [
        "https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot",
        "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"
    ]

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        taux_annee = personne('taux_tva_intermediaire_annee', period.this_year)
        return where(taux_annee, taux_annee, parameters(period).dicp.tva.taux.intermediaire)


class taux_tva_normal(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = "Taux normal de TVA"
    unit = units.PER_ONE
    set_input = set_input_divide_by_period
    reference = [
        "https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot",
        "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"
    ]

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        taux_annee = personne('taux_tva_normal_annee', period.this_year)
        return where(taux_annee, taux_annee, parameters(period).dicp.tva.taux.normal)


class taux_tva_reduit_annee(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Taux de TVA réduit défini annuellement"
    unit = units.PER_ONE
    set_input = set_input_divide_by_period
    reference = [
        "https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot",
        "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"
    ]

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.tva.taux.reduit


class taux_tva_intermediaire_annee(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Taux de TVA intermédiaire défini annuellement"
    unit = units.PER_ONE
    set_input = set_input_divide_by_period
    reference = [
        "https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot",
        "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"
    ]

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.tva.taux.intermediaire


class taux_tva_normal_annee(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Taux de TVA réduit défini annuellement"
    unit = units.PER_ONE
    set_input = set_input_divide_by_period
    reference = [
        "https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot",
        "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"
    ]

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.tva.taux.normal


class taux_tva_immeubles_hotelleries(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = "Taux de TVA livraisons d'immeubles et cession de parts"
    unit = units.PER_ONE
    set_input = set_input_divide_by_period
    reference = []

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        taux_annee = personne('taux_tva_immeubles_hotelleries_annee', period.this_year)
        return where(taux_annee, taux_annee, parameters(period).dicp.tva.taux.immeubles_hotelleries)


class taux_tva_immeubles_hotelleries_annee(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Taux de TVA livraisons d'immeubles et cession de parts défini annuellement"
    unit = units.PER_ONE
    set_input = set_input_divide_by_period
    reference = []

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.tva.taux.immeubles_hotelleries


class taux_tva_archipels(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = "Taux de TVA archipels"
    unit = units.PER_ONE
    reference = []

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.tva.taux.archipels
