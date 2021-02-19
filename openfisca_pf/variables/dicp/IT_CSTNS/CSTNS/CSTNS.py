# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefcstns system
from openfisca_pf.entities import *
from openfisca_pf.base import *


class montant_cstns_du(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant CST-NS total calculé.\n\n#montant_cstns_du = #cstns_ventes + #cstns_prestations"
    reference = "https://www.impot-polynesie.gov.pf/essentiel/la-contribution-de-solidarite-territoriale-sur-les-professions-et-activites-non-salariees"  # Always use the most official source

    def formula(entreprise, period, parameters):
        cstns_ventes = entreprise('cstns_ventes', period)
        cstns_prestations = entreprise('cstns_prestations', period)
        cstns_total = cstns_ventes + cstns_prestations
        return arrondiInf(cstns_total)


class cstns_a_payer(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant cstns total à payer.\n\nSi #montant_cstns_du < 6000\n    alors #cstns_a_payer = 0,\n    sinon #cstns_a_payer = #montant_it_du"
    # reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        montant_cstns_du = entreprise('montant_cstns_du', period)
        return where(montant_cstns_du < 6000, 0, montant_cstns_du)


class montant_cstns_total_a_payer(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT total à payer, en prenant compte des déductions et des pénalités :\n\n#montant_it_total_a_payer = #montant_it_du - #montant_total_deductions_it + montant_total_penalites_it"
    # reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        montant_cstns_du = entreprise('montant_cstns_du', period)
        # montant_total_deductions_cstns = entreprise('montant_total_deductions_cstns', period)
        # montant_total_penalites_cstns = entreprise('montant_total_penalites_cstns', period)
        return montant_cstns_du
        # - montant_total_deductions_cstns + montant_total_penalites_cstns


class redevable_cstns(Variable):
    value_type = bool
    entity = Entreprise
    definition_period = YEAR
    label = u"Défini si l'entreprise est éligible à la CST-NS.\nL'entreprise est redevable à la CST-NS si elle est redevable à l'IT"
    reference = "https://www.impot-polynesie.gov.pf/code/section-i-bases-et-personnes-imposables"

    def formula(entreprise, period, parameters):
        redevable_it = entreprise('redevable_it', period)
        return redevable_it


class nombre_entreprises_redevables_cstns_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = u"Nombre d'entreprises du pays redevables de la CST-NS"

    def formula(pays, period, parameters):
        redevables = pays.members('redevable_cst_ns', period)
        return pays.sum(redevables * 1)


class montant_cstns_total_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Montant total de CST-NS du par les entreprises du pays"

    def formula(pays, period, parameters):
        it_du = pays.members('montant_cst_ns_du', period)
        return pays.sum(it_du)
