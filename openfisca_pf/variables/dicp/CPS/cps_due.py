# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    MONTH,
    ParameterNode,
    Period,
    Population,
    Variable
    )
from openfisca_pf.constants.units import XPF
from openfisca_pf.entities import Personne
from openfisca_pf.functions.currency import arrondi_superieur


class cps_due(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    default_value = 0
    unit = XPF
    label = 'Montant de CPS dûe'
    reference = [
        'Code des impots : LP. 358-3',
        'https://www.impot-polynesie.gov.pf/code/5-titre-v-contribution-pour-la-solidarite'
        ]
    end = '2023-09-30'

    def formula(personne: Population, period: Period, parameters: ParameterNode):
        base_imposable = personne('base_imposable_cps', period)
        taux = personne.pays('taux_cps', period, parameters)
        return arrondi_superieur(base_imposable * taux)
