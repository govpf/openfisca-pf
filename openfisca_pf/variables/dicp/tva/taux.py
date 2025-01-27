# -*- coding: utf-8 -*-

from openfisca_pf.constants import units
from openfisca_pf.entities import *
from openfisca_pf.base import *


class taux_tva_reduit(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = u"Taux de TVA réduit"
    set_input = set_input_divide_by_period
    unit = units.PER_ONE
    reference = [
        "https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot",
        "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"
        ]

    def formula(pays, period, parameters):
        taux_annee = pays('taux_tva_reduit_annee', period.this_year, parameters)
        return where(taux_annee, taux_annee, parameters(period).dicp.tva.taux.reduit)


class taux_tva_intermediaire(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = u"Taux de TVA intermédiaire"
    set_input = set_input_divide_by_period
    unit = units.PER_ONE
    reference = [
        "https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot",
        "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"
        ]

    def formula(pays, period, parameters):
        taux_annee = pays('taux_tva_intermediaire_annee', period.this_year, parameters)
        return where(taux_annee, taux_annee, parameters(period).dicp.tva.taux.intermediaire)


class taux_tva_normal(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = u"Taux de TVA normal"
    unit = units.PER_ONE
    set_input = set_input_divide_by_period
    reference = [
        "https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot",
        "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"
        ]

    def formula(pays, period, parameters):
        taux_annee = pays('taux_tva_normal_annee', period.this_year, parameters)
        return where(taux_annee, taux_annee, parameters(period).dicp.tva.taux.normal)


class taux_tva_reduit_annee(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Taux de TVA réduit défini annuellement"
    unit = units.PER_ONE
    set_input = set_input_divide_by_period
    reference = [
        "https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot",
        "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"
        ]

    def formula(pays, period, parameters):
        return (parameters(period).dicp.tva.taux.reduit)


class taux_tva_intermediaire_annee(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Taux de TVA intermédiaire défini annuellement"
    unit = units.PER_ONE
    set_input = set_input_divide_by_period
    reference = [
        "https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot",
        "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"
        ]

    def formula(pays, period, parameters):
        return (parameters(period).dicp.tva.taux.intermediaire)


class taux_tva_normal_annee(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Taux de TVA normal défini annuellement"
    unit = units.PER_ONE
    set_input = set_input_divide_by_period
    reference = [
        "https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot",
        "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"
        ]

    def formula(pays, period, parameters):
        return (parameters(period).dicp.tva.taux.normal)

class taux_tva_livraisons_immeubles_et_cession_parts(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = u"Taux de TVA livraisons d'immeubles et cession de parts"
    unit = units.PER_ONE
    set_input = set_input_divide_by_period
    reference = []

    def formula(pays, period, parameters):
        taux_annee = pays('taux_tva_livraisons_immeubles_et_cession_parts_annee', period.this_year, parameters)
        return where(taux_annee, taux_annee, parameters(period).dicp.tva.taux.livraisons_immeubles_et_cession_parts)

class taux_tva_livraisons_immeubles_et_cession_parts_annee(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Taux de TVA livraisons d'immeubles et cession de parts défini annuellement"
    unit = units.PER_ONE
    set_input = set_input_divide_by_period
    reference = []

    def formula(pays, period, parameters):
        return (parameters(period).dicp.tva.taux.livraisons_immeubles_et_cession_parts)