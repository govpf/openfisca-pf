# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    ParameterNode,
    Period,
    Population,
    Variable,
    YEAR
    )
from openfisca_pf.entities import Personne


class chiffre_affaire_total(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant total du chiffre d'affaire"
    reference = []

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        chiffre_affaire_total_ventes = personne('chiffre_affaire_total_ventes', period)
        chiffre_affaire_total_prestations = personne('chiffre_affaire_total_prestations', period)
        return chiffre_affaire_total_ventes + chiffre_affaire_total_prestations
