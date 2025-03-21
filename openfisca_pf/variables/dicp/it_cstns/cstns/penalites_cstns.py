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
from openfisca_pf.constants.units import XPF, PER_CENT
from openfisca_pf.entities import Personne


class montant_amendes_cstns(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant des amendes appliquées a l'avis CST NS"
    unit = XPF


class taux_majoration_cstns(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Taux de majoration appliqué a la CST NS"
    unit = PER_CENT


class montant_majoration_cstns(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = 'Montant de la majoration appliquée a la CST NS'
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        taux_majoration_cstns = personne('taux_majoration_cstns', period)
        it_a_payer = personne('it_a_payer', period)
        return round_(it_a_payer * taux_majoration_cstns / 100.)


class montant_penalites_cstns(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = 'Montant des penalites appliquées a la CST NS'
    unit = XPF


class montant_total_penalites_cstns(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = 'Montant total des penalités CST NS'
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        montant_amendes_cstns = personne('montant_amendes_cstns', period)
        montant_majoration_cstns = personne('montant_majoration_cstns', period)
        montant_penalites_cstns = personne('montant_penalites_cstns', period)
        return round_(montant_amendes_cstns + montant_majoration_cstns + montant_penalites_cstns)
