# -*- coding: utf-8 -*-


from openfisca_core.populations import ADD
from openfisca_pf.base import (
    ArrayLike,
    MONTH,
    Parameters,
    Period,
    YEAR,
    Variable
    )
from openfisca_pf.constants import units
from openfisca_pf.entities import Pays


class tva_nette_due_total_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = "Montant total de TVA nette due par les entreprises du pays"
    unit = units.XPF

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        tva_nette_due = pays.members('tva_nette_due', period, parameters)
        return pays.sum(tva_nette_due)


class credit_tva_total_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = "Montant total de crédit de TVA à à rembourser aux entreprises du pays"
    unit = units.XPF

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        credit_tva = pays.members('credit_tva', period, parameters)
        return pays.sum(credit_tva)


class tva_due_taux_reduit_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = "Montant total de TVA due en taux réduit par les entreprises du pays"
    unit = units.XPF

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        tva_due_taux_reduit_pays = pays.members('tva_due_taux_reduit', period, parameters)
        return pays.sum(tva_due_taux_reduit_pays)


class tva_due_taux_intermediaire_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = "Montant total de TVA due en taux intermediaire par les entreprises du pays"
    unit = units.XPF

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        tva_due_taux_intermediaire_pays = pays.members('tva_due_taux_intermediaire', period, parameters)
        return pays.sum(tva_due_taux_intermediaire_pays)


class tva_due_taux_livraisons_immeubles_et_cession_parts_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = u"Montant total de TVA due en taux livraisons d'immeubles et cession de parts par les entreprises du pays"
    unit = units.XPF

    def formula(pays, period, parameters):
        tva_due_taux_livraisons_immeubles_et_cession_parts_pays = pays.members('tva_due_taux_livraisons_immeubles_et_cession_parts', period)
        return pays.sum(tva_due_taux_livraisons_immeubles_et_cession_parts_pays)


class tva_due_taux_normal_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = "Montant total de TVA due en taux normal par les entreprises du pays"
    unit = units.XPF

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        tva_due_taux_normal_pays = pays.members('tva_due_taux_normal', period, parameters)
        return pays.sum(tva_due_taux_normal_pays)


class tva_nette_due_total_pays_annee(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = "Montant total de TVA nette due par les entreprises du pays sur l'année"
    unit = units.XPF

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return pays('tva_nette_due_total_pays', period, parameters, options = [ADD])


class credit_tva_total_pays_annee(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = "Montant total de crédit de TVA à à rembourser aux entreprises du pays sur l'année"
    unit = units.XPF

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return pays('credit_tva_total_pays', period, parameters, options = [ADD])


class tva_due_taux_reduit_pays_annee(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = "Montant total de TVA due en taux réduit par les entreprises du pays sur l'année"
    unit = units.XPF

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return pays('tva_due_taux_reduit_pays', period, parameters, options = [ADD])


class tva_due_taux_intermediaire_pays_annee(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = "Montant total de TVA due en taux intermediaire par les entreprises du pays sur l'année"
    unit = units.XPF

    def formula(pays: Pays, period, parameters: Parameters) -> ArrayLike:
        return pays('tva_due_taux_intermediaire_pays', period, parameters, options = [ADD])


class tva_due_taux_normal_pays_annee(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = "Montant total de TVA due en taux normal par les entreprises du pays sur l'année"
    unit = units.XPF

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return pays('tva_due_taux_normal_pays', period, parameters, options = [ADD])


class tva_due_taux_livraisons_immeubles_et_cession_parts_pays_annee(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Montant total de TVA due en taux livraisons d'immeubles et cession de parts par les entreprises du pays sur l'année"
    unit = units.XPF

    def formula(pays, period, parameters):
        tva_due_taux_livraisons_immeubles_et_cession_parts_pays_annee = pays('tva_due_taux_livraisons_immeubles_et_cession_parts_pays', period, options = [ADD])
        return tva_due_taux_livraisons_immeubles_et_cession_parts_pays_annee
