# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.base import *


class tva_due_taux_reduit(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"Montant de TVA dûe au taux réduit"
    set_input = set_input_dispatch_by_period

    def formula(personne, period, parameters):
        base_imposable = personne(f'base_imposable_tva_taux_reduit', period)
        taux = personne.pays(f'taux_tva_reduit', period)
        return arrondiSup(base_imposable * taux)


class tva_due_taux_intermediaire(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"Montant de TVA dûe au taux intermédiaire"
    set_input = set_input_dispatch_by_period

    def formula(personne, period, parameters):
        base_imposable = personne(f'base_imposable_tva_taux_intermediaire', period)
        taux = personne.pays(f'taux_tva_intermediaire', period)
        return arrondiSup(base_imposable * taux)


class tva_due_taux_normal(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"Montant de TVA dûe au taux normal"
    set_input = set_input_dispatch_by_period

    def formula(personne, period, parameters):
        base_imposable = personne(f'base_imposable_tva_taux_normal', period)
        taux = personne.pays(f'taux_tva_normal', period)
        return arrondiSup(base_imposable * taux)


class montant_tva_total_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = u"Montant total de TVA due par les entreprises du pays"

    def formula(pays, period, parameters):
        tva_reduite = pays(f'montant_tva_reduite_total_pays', period)
        tva_intermediaire = pays(f'montant_tva_intermediaire_total_pays', period)
        tva_normale = pays(f'montant_tva_normale_total_pays', period)
        return tva_reduite + tva_intermediaire + tva_normale


class montant_tva_reduite_total_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = u"Montant total de TVA à taux réduit due par les entreprises du pays"

    def formula(pays, period, parameters):
        tva_due = pays.members('tva_due_taux_reduit', period)
        return pays.sum(tva_due)


class montant_tva_intermediaire_total_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = u"Montant total de TVA à taux intermédiare due par les entreprises du pays"

    def formula(pays, period, parameters):
        tva_due = pays.members('tva_due_taux_intermediaire', period)
        return pays.sum(tva_due)


class montant_tva_normale_total_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = u"Montant total de TVA à taux normal due par les entreprises du pays"

    def formula(pays, period, parameters):
        tva_due = pays.members('tva_due_taux_normal', period)
        return pays.sum(tva_due)
