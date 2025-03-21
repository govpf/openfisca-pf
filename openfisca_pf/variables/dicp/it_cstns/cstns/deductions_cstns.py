# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    ParameterNode,
    Period,
    Population,
    round_,
    Variable,
    YEAR
    )
from openfisca_pf.constants.units import XPF
from openfisca_pf.entities import Personne


class abattement_cstns(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = 'Abattement total de droit applique sur la CST NS'
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        cstns_ventes_abattement_droits = personne('cstns_ventes_abattement_droits', period)
        cstns_prestations_abattement_droits = personne('cstns_prestations_abattement_droits', period)
        return round_(cstns_prestations_abattement_droits + cstns_ventes_abattement_droits)


class montant_total_deductions_cstns(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = 'Montant total des deductions IT à appliquer'
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = XPF
