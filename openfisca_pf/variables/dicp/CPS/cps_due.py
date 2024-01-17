# -*- coding: utf-8 -*-


from openfisca_core.periods import Period, MONTH
from openfisca_core.variables import Variable
from openfisca_pf.constants.units import XPF
from openfisca_pf.entities import Personne
from openfisca_pf.base import arrondiSup


class cps_due(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    default_value = 0
    unit = XPF
    label = 'Montant de CPS dûe: cps_due := base_imposable_cps * taux_cps'
    reference = [
        'Code des impots : LP. 358-3',
        'https://www.impot-polynesie.gov.pf/code/5-titre-v-contribution-pour-la-solidarite'
        ]
    end = '2023-09-30'

    def formula(personne: Personne, period: Period):
        base_imposable = personne('base_imposable_cps', period)
        taux = personne.pays('taux_cps', period)
        return arrondiSup(base_imposable * taux)
