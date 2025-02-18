# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    max_,
    MONTH,
    Parameters,
    Period,
    Variable
    )
from openfisca_pf.constants import units
from openfisca_pf.entities import Personne


class tva_nette_due(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    unit = units.XPF
    label = "Montant de TVA nette dûe"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        tva_deductible = personne('tva_deductible', period, parameters)
        tva_exigible = personne('tva_exigible', period, parameters)
        tva_nette_due = tva_exigible - tva_deductible
        return max_(tva_nette_due, 0)


class credit_tva(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    unit = units.XPF
    label = "Montant de crédit de TVA"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        tva_deductible = personne('tva_deductible', period, parameters)
        tva_exigible = personne('tva_exigible', period, parameters)
        credit_tva = tva_deductible - tva_exigible
        return max_(credit_tva, 0)
