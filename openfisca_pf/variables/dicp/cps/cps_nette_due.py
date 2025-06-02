# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    max_,
    MONTH,
    Parameters,
    Period,
    Variable
    )
from openfisca_pf.constants.units import XPF
from openfisca_pf.entities import Personne


class cps_nette(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    unit = XPF
    label = 'Montant de CPS nette'
    reference = [
        'Code des impots : LP. 358-4',
        'https://www.impot-polynesie.gov.pf/code/5-titre-v-contribution-pour-la-solidarite'
        ]
    default_value = 0
    end = '2023-09-30'

    def formula(personne: Personne, period: Period, parameters: Parameters):
        cps_due = personne('cps_due', period, parameters)
        cps_en_diminution = personne('cps_en_diminution', period, parameters)
        cps_a_reverser = personne('cps_a_reverser', period, parameters)
        return cps_due - cps_en_diminution + cps_a_reverser


class cps_nette_due(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    unit = XPF
    label = 'Montant de CPS nette dûe'
    reference = [
        'Code des impots : LP. 358-4',
        'https://www.impot-polynesie.gov.pf/code/5-titre-v-contribution-pour-la-solidarite'
        ]
    default_value = 0
    end = '2023-09-30'

    def formula(personne: Personne, period: Period, parameters: Parameters):
        cps_nette = personne('cps_nette', period, parameters)
        return max_(cps_nette, 0)


class cps_a_reporter(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    unit = XPF
    label = 'Montant de CPS à reporter'
    reference = [
        'Code des impots : LP. 358-4',
        'https://www.impot-polynesie.gov.pf/code/5-titre-v-contribution-pour-la-solidarite'
        ]
    default_value = 0
    end = '2023-09-30'

    def formula(personne: Personne, period: Period, parameters: Parameters):
        cps_nette = personne('cps_nette', period, parameters)
        return max_(-cps_nette, 0)


class tva_plus_cps_nette_due(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    unit = XPF
    label = 'Montant de CPS et de TVA nette dûe'
    default_value = 0
    end = '2023-09-30'

    def formula(personne: Personne, period: Period, parameters: Parameters):
        cps_nette_due = personne('cps_nette_due', period, parameters)
        tva_nette_due = personne('tva_nette_due', period, parameters)
        return cps_nette_due + tva_nette_due
