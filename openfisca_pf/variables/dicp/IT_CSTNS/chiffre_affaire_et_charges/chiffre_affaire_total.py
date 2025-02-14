# -*- coding: utf-8 -*-

from openfisca_pf.base import (
    ArrayLike,
    Parameters,
    Period,
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

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        chiffre_affaire_total_ventes = personne('chiffre_affaire_total_ventes', period, parameters)
        chiffre_affaire_total_prestations = personne('chiffre_affaire_total_prestations', period, parameters)
        return chiffre_affaire_total_ventes + chiffre_affaire_total_prestations
