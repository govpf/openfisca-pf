# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.base import *


class nombre_entreprises_redevables_IT_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = u"Nombre d'entreprises du pays redevables de la IT"

    def formula(pays, period, parameters):
        redevable_it = pays.members('redevable_it', period)
        return pays.sum(redevable_it * 1)


class nombre_entreprises_redevables_it_tranche_1_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = u"Nombre d'entreprises du pays redevables de l'IT dont les revenus sont imposables à la tranche 1"

    def formula(pays, period, parameters):
        redevables = pays.members('montant_du_it_tranche_1', period)
        return pays.sum((redevables > 0) * 1)


class nombre_entreprises_redevables_it_tranche_2_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = u"Nombre d'entreprises du pays redevables de l'IT dont les revenus sont imposables à la tranche 2"

    def formula(pays, period, parameters):
        redevables = pays.members('montant_du_it_tranche_2', period)
        return pays.sum((redevables > 0) * 1)


class nombre_entreprises_redevables_it_tranche_3_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = u"Nombre d'entreprises du pays redevables de l'IT dont les revenus sont imposables à la tranche 3"

    def formula(pays, period, parameters):
        redevables = pays.members('montant_du_it_tranche_3', period)
        return pays.sum((redevables > 0) * 1)


class nombre_entreprises_redevables_it_tranche_4_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = u"Nombre d'entreprises du pays redevables de l'IT dont les revenus sont imposables à la tranche 4"

    def formula(pays, period, parameters):
        redevables = pays.members('montant_du_it_tranche_4', period)
        return pays.sum((redevables > 0) * 1)


class nombre_entreprises_redevables_it_tranche_5_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = u"Nombre d'entreprises du pays redevables de l'IT dont les revenus sont imposables à la tranche 5"

    def formula(pays, period, parameters):
        redevables = pays.members('montant_du_it_tranche_5', period)
        return pays.sum((redevables > 0) * 1)


class nombre_entreprises_redevables_it_tranche_6_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = u"Nombre d'entreprises du pays redevables de l'IT dont les revenus sont imposables à la tranche 6"

    def formula(pays, period, parameters):
        redevables = pays.members('montant_du_it_tranche_6', period)
        return pays.sum((redevables > 0) * 1)


class nombre_entreprises_redevables_it_tranche_7_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = u"Nombre d'entreprises du pays redevables de l'IT dont les revenus sont imposables à la tranche 7"

    def formula(pays, period, parameters):
        redevables = pays.members('montant_du_it_tranche_7', period)
        return pays.sum((redevables > 0) * 1)


class nombre_entreprises_redevables_it_tranche_8_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = u"Nombre d'entreprises du pays redevables de l'IT dont les revenus sont imposables à la tranche 8"

    def formula(pays, period, parameters):
        redevables = pays.members('montant_du_it_tranche_8', period)
        return pays.sum((redevables > 0) * 1)


class nombre_entreprises_redevables_it_tranche_9_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = u"Nombre d'entreprises du pays redevables de l'IT dont les revenus sont imposables à la tranche 9"

    def formula(pays, period, parameters):
        redevables = pays.members('montant_du_it_tranche_9', period)
        return pays.sum((redevables > 0) * 1)


class nombre_entreprises_redevables_it_tranche_10_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = u"Nombre d'entreprises du pays redevables de l'IT dont les revenus sont imposables à la tranche 10"

    def formula(pays, period, parameters):
        redevables = pays.members('montant_du_it_tranche_10', period)
        return pays.sum((redevables > 0) * 1)


class nombre_entreprises_redevables_it_tranche_11_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = u"Nombre d'entreprises du pays redevables de l'IT dont les revenus sont imposables à la tranche 11"

    def formula(pays, period, parameters):
        redevables = pays.members('montant_du_it_tranche_11', period)
        return pays.sum((redevables > 0) * 1)


class nombre_entreprises_redevables_it_tranche_12_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = u"Nombre d'entreprises du pays redevables de l'IT dont les revenus sont imposables à la tranche 12"

    def formula(pays, period, parameters):
        redevables = pays.members('montant_du_it_tranche_12', period)
        return pays.sum((redevables > 0) * 1)
