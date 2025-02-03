# -*- coding: utf-8 -*-

from openfisca_pf.base import *
from openfisca_pf.constants import units
from openfisca_pf.entities import *


class tva_nette_due_total_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = u"Montant total de TVA nette due par les entreprises du pays"
    unit = units.XPF

    def formula(pays, period, parameters):
        tva_nette_due = pays.members('tva_nette_due', period)
        return pays.sum(tva_nette_due)


class credit_tva_total_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = u"Montant total de crédit de TVA à à rembourser aux entreprises du pays"
    unit = units.XPF

    def formula(pays, period, parameters):
        credit_tva = pays.members('credit_tva', period)
        return pays.sum(credit_tva)


class tva_due_taux_reduit_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = u"Montant total de TVA due en taux réduit par les entreprises du pays"
    unit = units.XPF

    def formula(pays, period, parameters):
        tva_due_taux_reduit_pays = pays.members('tva_due_taux_reduit', period)
        return pays.sum(tva_due_taux_reduit_pays)


class tva_due_taux_intermediaire_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = u"Montant total de TVA due en taux intermediaire par les entreprises du pays"
    unit = units.XPF

    def formula(pays, period, parameters):
        tva_due_taux_intermediaire_pays = pays.members('tva_due_taux_intermediaire', period)
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
    label = u"Montant total de TVA due en taux normal par les entreprises du pays"
    unit = units.XPF

    def formula(pays, period, parameters):
        tva_due_taux_normal_pays = pays.members('tva_due_taux_normal', period)
        return pays.sum(tva_due_taux_normal_pays)


class tva_nette_due_total_pays_annee(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Montant total de TVA nette due par les entreprises du pays sur l'année"
    unit = units.XPF

    def formula(pays, period, parameters):
        tva_nette_due_total_pays_annee = pays('tva_nette_due_total_pays', period, options = [ADD])
        return tva_nette_due_total_pays_annee


class credit_tva_total_pays_annee(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Montant total de crédit de TVA à à rembourser aux entreprises du pays sur l'année"
    unit = units.XPF

    def formula(pays, period, parameters):
        credit_tva_total_pays_annee = pays('credit_tva_total_pays', period, options = [ADD])
        return credit_tva_total_pays_annee


class tva_due_taux_reduit_pays_annee(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Montant total de TVA due en taux réduit par les entreprises du pays sur l'année"
    unit = units.XPF

    def formula(pays, period, parameters):
        tva_due_taux_reduit_pays_annee = pays('tva_due_taux_reduit_pays', period, options = [ADD])
        return tva_due_taux_reduit_pays_annee


class tva_due_taux_intermediaire_pays_annee(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Montant total de TVA due en taux intermediaire par les entreprises du pays sur l'année"
    unit = units.XPF

    def formula(pays, period, parameters):
        tva_due_taux_intermediaire_pays_annee = pays('tva_due_taux_intermediaire_pays', period, options = [ADD])
        return tva_due_taux_intermediaire_pays_annee


class tva_due_taux_normal_pays_annee(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Montant total de TVA due en taux normal par les entreprises du pays sur l'année"
    unit = units.XPF

    def formula(pays, period, parameters):
        tva_due_taux_normal_pays_annee = pays('tva_due_taux_normal_pays', period, options = [ADD])
        return tva_due_taux_normal_pays_annee


class tva_due_taux_livraisons_immeubles_et_cession_parts_pays_annee(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Montant total de TVA due en taux livraisons d'immeubles et cession de parts par les entreprises du pays sur l'année"
    unit = units.XPF

    def formula(pays, period, parameters):
        tva_due_taux_livraisons_immeubles_et_cession_parts_pays_annee = pays('tva_due_taux_livraisons_immeubles_et_cession_parts_pays', period, options = [ADD])
        return tva_due_taux_livraisons_immeubles_et_cession_parts_pays_annee
