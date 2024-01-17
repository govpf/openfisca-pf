# -*- coding: utf-8 -*-


from openfisca_core.periods import MONTH
from openfisca_core.variables import Variable
from openfisca_pf.constants.units import XPF
from openfisca_pf.entities import Personne


class cps_a_reverser(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = 'Montant de CPS à reverser'
    unit = XPF
    default_value = 0
    end = '2023-09-30'


class cps_en_diminution(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = 'Montant de CPS en diminution'
    unit = XPF
    default_value = 0
    end = '2023-09-30'
