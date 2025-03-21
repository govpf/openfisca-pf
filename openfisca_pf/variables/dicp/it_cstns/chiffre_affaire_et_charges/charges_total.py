# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    ParameterNode,
    Period,
    Population,
    Variable,
    YEAR
    )
from openfisca_pf.constants.units import XPF
from openfisca_pf.entities import Personne


class charges_total(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant total des charges"
    reference = []
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        charges_total_ventes = personne('charges_total_ventes', period)
        charges_total_prestations = personne('charges_total_prestations', period)
        return charges_total_ventes + charges_total_prestations


class total_charges_releve_detaille(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant total des charges déclaré dans le relevé détaillé"
    reference = []
    unit = XPF
