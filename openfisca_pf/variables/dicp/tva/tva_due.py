# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    MONTH,
    set_input_dispatch_by_period,
    ParameterNode,
    Period,
    Population,
    Variable
    )
from openfisca_pf.constants.units import XPF
from openfisca_pf.entities import Personne
from openfisca_pf.functions.currency import arrondi_superieur


class tva_due_taux_reduit(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = 'Montant de TVA dûe au taux réduit'
    set_input = set_input_dispatch_by_period
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        base_imposable = personne('base_imposable_tva_taux_reduit', period)
        taux = parameters(period).dicp.tva.taux.reduit
        return arrondi_superieur(base_imposable * taux)


class tva_due_taux_intermediaire(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = 'Montant de TVA dûe au taux intermédiaire'
    set_input = set_input_dispatch_by_period
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        base_imposable = personne('base_imposable_tva_taux_intermediaire', period)
        taux = parameters(period).dicp.tva.taux.intermediaire
        return arrondi_superieur(base_imposable * taux)


class tva_due_taux_normal(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = 'Montant de TVA dûe au taux normal'
    set_input = set_input_dispatch_by_period
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        base_imposable = personne('base_imposable_tva_taux_normal', period)
        taux = parameters(period).dicp.tva.taux.normal
        return arrondi_superieur(base_imposable * taux)


class tva_due_taux_immeubles_hotelleries(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = "Montant de TVA dûe au taux livraisons d'immeubles et cession de parts"
    set_input = set_input_dispatch_by_period
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        base_imposable = personne('base_imposable_tva_taux_immeubles_hotelleries', period)
        taux = parameters(period).dicp.tva.taux.immeubles_hotelleries
        return arrondi_superieur(base_imposable * taux)


class tva_due_taux_archipels(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = "Montant de TVA dûe au taux archipels"
    set_input = set_input_dispatch_by_period
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        base_imposable = personne('base_imposable_tva_taux_archipels', period)
        taux = personne.pays('taux_tva_archipels', period)
        return arrondi_superieur(base_imposable * taux)
