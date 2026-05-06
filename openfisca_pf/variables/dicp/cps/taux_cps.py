# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    GroupPopulation,
    MONTH,
    ParameterNode,
    Period,
    set_input_divide_by_period,
    Variable
    )
from openfisca_pf.constants.units import PER_ONE
from openfisca_pf.entities import Pays


class taux_cps(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = 'Taux de CPS'
    set_input = set_input_divide_by_period
    unit = PER_ONE
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    default_value = 0
    end = '2023-09-30'

    def formula(pays: GroupPopulation, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.cps.taux
