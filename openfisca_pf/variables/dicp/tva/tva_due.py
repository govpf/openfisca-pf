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
        taux = personne.pays('taux_tva_reduit', period)
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
        taux = personne.pays('taux_tva_intermediaire', period)
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
        taux = personne.pays('taux_tva_normal', period)
        return arrondi_superieur(base_imposable * taux)


class tva_due_taux_livraisons_immeubles_et_cession_parts(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = "Montant de TVA dûe au taux livraisons d'immeubles et cession de parts"
    set_input = set_input_dispatch_by_period
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        base_imposable = personne('base_imposable_tva_taux_livraisons_immeubles_et_cession_parts', period)
        taux = personne.pays('taux_tva_livraisons_immeubles_et_cession_parts', period)
        return arrondi_superieur(base_imposable * taux)
