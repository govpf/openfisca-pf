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


class montant_amendes_it(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant des amendes appliquées a l'avis d'impôt sur les transactions"
    unit = XPF


class taux_majoration_it(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Taux de majoration appliqué a l'impôt sur les transactions"
    unit = PER_CENT


class montant_penalites_it(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant des penalites appliquées a l'impôt sur les transactions"
    unit = XPF


class montant_majoration_it(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant de la majoration appliquée a l'impôt sur les transactions"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        taux_majoration_it = personne('taux_majoration_it', period)
        it_a_payer = personne('it_a_payer', period)
        return round_(it_a_payer * taux_majoration_it / 100.)


class montant_total_penalites_it(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant total des penalités impôt sur les transactions"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        montant_amendes_it = personne('montant_amendes_it', period)
        montant_majoration_it = personne('montant_majoration_it', period)
        montant_penalites_it = personne('montant_penalites_it', period)
        return round_(montant_amendes_it + montant_majoration_it + montant_penalites_it)
