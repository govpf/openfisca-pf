# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.base import *


class montant_it_du(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT total calculé.\n\n#montant_it_du = #it_ventes + #it_prestations"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(entreprise, period, parameters):
        it_ventes = entreprise('it_ventes', period)
        it_prestations = entreprise('it_prestations', period)
        it_total = it_ventes + it_prestations
        # it = select(
        #     [entreprise('eligible_tpe_1', period), entreprise('eligible_tpe_2', period), not_(entreprise('eligible_tpe_1', period)) * not_(entreprise('eligible_tpe_1', period))],
        #     [25000, 45000, it_total],
        #     )
        return arrondiInf(it_total)


class it_a_payer(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT à payer.\n\nSi #montant_it_du < 6000\n    alors #it_a_payer = 0,\n    sinon #it_a_payer = #montant_it_du"
    # reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        montant_it_du = entreprise('montant_it_du', period)
        return where(montant_it_du < 6000, 0, montant_it_du)


class montant_it_total_a_payer(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT total à payer, en prenant compte des déductions et des pénalités :\n\n#montant_it_total_a_payer = #montant_it_du - #montant_total_deductions_it + montant_total_penalites_it"
    # reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        montant_it_du = entreprise('montant_it_du', period)
        montant_total_deductions_it = entreprise('montant_total_deductions_it', period)
        montant_total_penalites_it = entreprise('montant_total_penalites_it', period)
        return montant_it_du - montant_total_deductions_it + montant_total_penalites_it


class montant_it_total_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Montant total d'IT du par les entreprises du pays"

    def formula(pays, period, parameters):
        it_du = pays.members('montant_it_du', period)
        return pays.sum(it_du)
