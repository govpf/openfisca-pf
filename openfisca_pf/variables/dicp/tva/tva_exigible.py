# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    MONTH,
    Parameters,
    Period,
    Variable
    )
from openfisca_pf.constants import units
from openfisca_pf.entities import Personne


class regularisation_autre_tva_exigible(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = "Montant à appliquer pour régulariser le montant de TVA exigible"
    unit = units.XPF
    default_value = 0


class sous_total_tva_exigible(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    unit = units.XPF
    label = "Montant de TVA exigible"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        tva_due_taux_reduit = personne('tva_due_taux_reduit', period, parameters)
        tva_due_taux_intermediaire = personne('tva_due_taux_intermediaire', period, parameters)
        tva_due_taux_normal = personne('tva_due_taux_normal', period, parameters)
        return tva_due_taux_reduit + tva_due_taux_intermediaire + tva_due_taux_normal

    def formula_2025(personne, period, parameters):
        tva_due_taux_reduit = personne('tva_due_taux_reduit', period)
        tva_due_taux_intermediaire = personne('tva_due_taux_intermediaire', period)
        tva_due_taux_normal = personne('tva_due_taux_normal', period)
        tva_due_taux_livraisons_immeubles_et_cession_parts = personne('tva_due_taux_livraisons_immeubles_et_cession_parts', period)
        return tva_due_taux_reduit + tva_due_taux_intermediaire + tva_due_taux_normal + tva_due_taux_livraisons_immeubles_et_cession_parts


class tva_exigible(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    unit = units.XPF
    label = "Montant de TVA exigible"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        sous_total_tva_exigible = personne('sous_total_tva_exigible', period, parameters)
        regularisation_autre_tva_exigible = personne('regularisation_autre_tva_exigible', period, parameters)
        return sous_total_tva_exigible + regularisation_autre_tva_exigible
