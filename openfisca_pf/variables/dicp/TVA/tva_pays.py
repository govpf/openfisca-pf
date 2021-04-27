# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.base import *


class tva_nette_due_total_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = u"Montant total de TVA nette due par les entreprises du pays"

    def formula(pays, period, parameters):
        tva_nette_due = pays.members('tva_nette_due', period)
        return pays.sum(tva_nette_due)


class credit_tva_total_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = u"Montant total de crédit de TVA à à rembourser aux entreprises du pays"

    def formula(pays, period, parameters):
        credit_tva = pays.members('credit_tva', period)
        return pays.sum(credit_tva)


class tva_nette_due_total_pays_annee(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Montant total de TVA nette due par les entreprises du pays sur l'année"

    def formula(pays, period, parameters):
        tva_nette_due_total_pays_annee = pays('tva_nette_due_total_pays', period, options = [ADD])
        return tva_nette_due_total_pays_annee


class credit_tva_total_pays_annee(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Montant total de crédit de TVA à à rembourser aux entreprises du pays sur l'année"

    def formula(pays, period, parameters):
        credit_tva_total_pays_annee = pays('credit_tva_total_pays', period, options = [ADD])
        return credit_tva_total_pays_annee
