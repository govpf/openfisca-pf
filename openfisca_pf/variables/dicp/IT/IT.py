# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
import numpy


class montant_it_du(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT total calculé"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        it_ventes = entreprise('it_ventes', period)
        it_prestations = entreprise('it_prestations', period)
        it_total = it_ventes + it_prestations
        it = select(
            [entreprise('eligible_tpe_1', period), entreprise('eligible_tpe_2', period), not_(entreprise('eligible_tpe_1', period)) * not_(entreprise('eligible_tpe_1', period))],
            [25000, 45000, it_total],
            )
        return numpy.floor(it)


class it_a_payer(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT à payer"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        montant_it_du = numpy.floor(entreprise('montant_it_du', period))
        return where(montant_it_du < 6000, 0, montant_it_du)


class abattement_it(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Abattement de droit applique sur l'IT des ventes"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        abattement_it_ventes = entreprise('abattement_it_ventes', period)
        abattement_it_prestations = entreprise('abattement_it_prestations', period)
        return round_(abattement_it_prestations + abattement_it_ventes)


class montant_acompte_it_1(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant du 1er acompte IT verse"


class montant_acompte_it_2(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant du 2eme acompte IT verse"


class montant_declaration_provisoire_it(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant de l'IT calcule sur une declaration provisoire"


class montant_credit_impot_it_1(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant de credit d'impot IT 1"


class montant_credit_impot_it_2(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant de credit d'impot IT 2"


class montant_credit_impot_it_3(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant de credit d'impot IT 3"


class montant_credit_impot_it_4(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant de credit d'impot IT 4"


class montant_it_total_a_payer(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT total à payer"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        montant_it_du = entreprise('montant_it_du', period)
        montant_acompte_it_1 = entreprise('montant_acompte_it_1', period)
        montant_acompte_it_2 = entreprise('montant_acompte_it_2', period)
        montant_declaration_provisoire_it = entreprise('montant_declaration_provisoire_it', period)
        montant_credit_impot_it_1 = entreprise('montant_credit_impot_it_1', period)
        montant_credit_impot_it_2 = entreprise('montant_credit_impot_it_2', period)
        montant_credit_impot_it_3 = entreprise('montant_credit_impot_it_3', period)
        montant_credit_impot_it_4 = entreprise('montant_credit_impot_it_4', period)
        montant_it_total = montant_it_du - montant_acompte_it_1 - montant_acompte_it_2 - montant_declaration_provisoire_it - montant_credit_impot_it_1 - montant_credit_impot_it_2 - montant_credit_impot_it_3 - montant_credit_impot_it_4
        return montant_it_total
