# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    Parameters,
    Period,
    round_,
    Variable,
    YEAR
    )
from openfisca_pf.constants.units import XPF
from openfisca_pf.entities import Personne


class abattement_it(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Abattement total de droit applique sur l'impôt sur les transactions"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        it_ventes_abattement_droits = personne('it_ventes_abattement_droits', period, parameters)
        it_prestations_abattement_droits = personne('it_prestations_abattement_droits', period, parameters)
        return round_(it_prestations_abattement_droits + it_ventes_abattement_droits)


class montant_total_deductions_it(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant total des deductions impôt sur les transactions à appliquer"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = XPF
