# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    MONTH,
    ParameterNode,
    Period,
    Population,
    set_input_divide_by_period,
    Variable
    )
from openfisca_pf.entities import Personne
from openfisca_pf.constants.units import XPF


class base_imposable_cps(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = 'Base imposable de la TVA à taux réduit'
    unit = XPF
    reference = [
        'Code des impots : LP. 358-1 et LP. 358-2',
        'https://www.impot-polynesie.gov.pf/code/5-titre-v-contribution-pour-la-solidarite'
        ]
    default_value = 0
    end = '2023-09-30'

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        base_imposable_tva_taux_reduit = personne('base_imposable_tva_taux_reduit', period)
        base_imposable_tva_taux_intermediaire = personne('base_imposable_tva_taux_intermediaire', period)
        base_imposable_tva_taux_normal = personne('base_imposable_tva_taux_normal', period)
        return base_imposable_tva_taux_reduit + base_imposable_tva_taux_intermediaire + base_imposable_tva_taux_normal
