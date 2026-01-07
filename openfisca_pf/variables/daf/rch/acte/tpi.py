# -*- coding: utf-8 -*-


from fractions import Fraction
from openfisca_pf.base import (
    ArrayLike,
    DAY,
    Enum,
    ParameterNode,
    Period,
    Population,
    select,
    Variable
    )
from openfisca_pf.entities import Personne
from openfisca_pf.enums.rch import (
    NatureActe,
    TypeAcheteur,
    TypeBien,
    TypeDemarche,
    TypeParente
    )
from openfisca_pf.functions.currency import arrondi_superieur
import numpy


class nature_acte(Variable):
    value_type = Enum
    possible_values = NatureActe
    default_value = NatureActe.Vente
    entity = Personne
    definition_period = DAY
    label = "Nature de l'acte"


class montant_total_acte(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Montant total d'un acte"


class montant_tpi_acte(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Montant de la taxe de publicité immobilière selon la nature de l'acte"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        nature_acte = personne('nature_acte', period)
        montant_total_acte = personne('montant_total_acte', period)
        taux = parameters(period).daf.rch.taxe_publicite_immobiliere.acte.rate

        return select(
            [
                nature_acte == NatureActe.Vente,
                nature_acte == NatureActe.Donation
                ],
            [
                montant_total_acte * taux,
                montant_total_acte / 2
                ]
            )