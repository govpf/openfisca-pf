# -*- coding: utf-8 -*-

import numpy
from openfisca_core.periods import Period, MONTH
from openfisca_core.parameters import Parameter
from openfisca_core.variables import Variable
from openfisca_pf.constants.units import XPF
from openfisca_pf.entities import Personne


class cps_nette(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    unit = XPF
    label = 'Montant de CPS nette: cps_nette := cps_due - cps_en_diminution + cps_a_reverser'
    reference = [
        'Code des impots : LP. 358-4',
        'https://www.impot-polynesie.gov.pf/code/5-titre-v-contribution-pour-la-solidarite'
        ]
    default_value = 0
    end = '2023-09-30'

    def formula(personne: Personne, period: Period, parameters: Parameter):
        cps_due = personne('cps_due', period, parameters)
        cps_en_diminution = personne('cps_en_diminution', period, parameters)
        cps_a_reverser = personne('cps_a_reverser', period, parameters)
        return cps_due - cps_en_diminution + cps_a_reverser


class cps_nette_due(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    unit = XPF
    label = 'Montant de CPS nette dûe: cps_nette_due := max(cps_nette, 0)'
    reference = [
        'Code des impots : LP. 358-4',
        'https://www.impot-polynesie.gov.pf/code/5-titre-v-contribution-pour-la-solidarite'
        ]
    default_value = 0
    end = '2023-09-30'

    def formula(personne: Personne, period: Period, parameters: Parameter):
        cps_nette = personne('cps_nette', period, parameters)
        return numpy.maximum(cps_nette, 0)


class cps_a_reporter(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    unit = XPF
    label = 'Montant de CPS à reporter: cps_a_reporter := max(-cps_nette, 0)'
    reference = [
        'Code des impots : LP. 358-4',
        'https://www.impot-polynesie.gov.pf/code/5-titre-v-contribution-pour-la-solidarite'
        ]
    default_value = 0
    end = '2023-09-30'

    def formula(personne: Personne, period: Period, parameters: Parameter):
        cps_nette = personne('cps_nette', period, parameters)
        return numpy.maximum(-cps_nette, 0)


class tva_plus_cps_nette_due(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    unit = XPF
    label = 'Montant de CPS et de TVA nette dûe: tva_plus_cps_nette_due := cps_nette_due + tva_nette_due'
    default_value = 0
    end = '2023-09-30'

    def formula(personne: Personne, period: Period, parameters: Parameter):
        cps_nette_due = personne('cps_nette_due', period, parameters)
        tva_nette_due = personne('tva_nette_due', period, parameters)
        return cps_nette_due + tva_nette_due
