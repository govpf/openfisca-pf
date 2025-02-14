# -*- coding: utf-8 -*-

from openfisca_pf.base import (
    ArrayLike,
    MONTH,
    Parameters,
    Period,
    Variable
    )
from openfisca_pf.constants.dicp.references_csts import (
    REFERENCE_CODE_LP_TAUX_CSTS,
    REFERENCE_LIEN_CODE,
    REFERENCE_LIEN_TAUX
    )
from openfisca_pf.constants.units import XPF
from openfisca_pf.entities import Personne


class cst_s_due_totale_par_employes(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = 'Sum of the taxes paid by a household'
    reference = [
        REFERENCE_CODE_LP_TAUX_CSTS,
        REFERENCE_LIEN_CODE,
        REFERENCE_LIEN_TAUX
    ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        cst_s = personne.members('cst_s', period, parameters)
        return personne.sum(cst_s)


class cst_s_due_totale(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = "CST-S due par l'entreprise sur l'ensemble des salaires déclarés par tranche"
    reference = [
        REFERENCE_CODE_LP_TAUX_CSTS,
        REFERENCE_LIEN_CODE,
        REFERENCE_LIEN_TAUX
    ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        total = 0
        for i, taux in enumerate(parameters(period).dicp.cst_s.taux.rates):
            total += personne(f'cst_s_due_tranche_{i + 1}', period, parameters)
        return total
