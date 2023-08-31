# -*- coding: utf-8 -*-

from openfisca_pf.constants import units
from openfisca_pf.entities import *
from openfisca_pf.base import *


class tva_nette_due(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    unit = units.XPF
    label = u"Montant de TVA nette dûe: \n\n#tva_nette_due = MAX(#tva_exigible - #tva_deductible, 0)"

    def formula(personne, period, parameters):
        tva_deductible = personne('tva_deductible', period)
        tva_exigible = personne('tva_exigible', period)
        tva_nette_due = tva_exigible - tva_deductible
        return max_(tva_nette_due, 0)


class credit_tva(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    unit = units.XPF
    label = u"Montant de crédit de TVA : \n\n#credit_tva = MAX(#tva_deductible - #tva_exigible, 0)"

    def formula(personne, period, parameters):
        tva_deductible = personne('tva_deductible', period)
        tva_exigible = personne('tva_exigible', period)
        credit_tva = tva_deductible - tva_exigible
        return max_(credit_tva, 0)
