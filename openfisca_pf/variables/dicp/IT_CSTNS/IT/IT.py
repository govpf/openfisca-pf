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
    entity = Personne
    definition_period = YEAR
    label = u"Montant IT total calculé.\n\n#montant_it_du = #it_ventes + #it_prestations"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(personne, period, parameters):
        it_ventes = personne('it_ventes', period)
        it_prestations = personne('it_prestations', period)
        it_total = it_ventes + it_prestations
        # it = select(
        #     [personne('redevable_tpe_1', period), personne('redevable_tpe_2', period), not_(personne('redevable_tpe_1', period)) * not_(personne('redevable_tpe_1', period))],
        #     [25000, 45000, it_total],
        #     )
        return arrondiInf(it_total)


class it_a_payer(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant IT à payer.\n\nSi #montant_it_du < 6000\n    alors #it_a_payer = 0,\n    sinon #it_a_payer = #montant_it_du"
    # reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(personne, period, parameters):
        montant_it_du = personne('montant_it_du', period)
        return where(montant_it_du < 6000, 0, montant_it_du)


class montant_it_total_a_payer(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant IT total à payer, en prenant compte des déductions et des pénalités :\n\n#montant_it_total_a_payer = #montant_it_du - #montant_total_deductions_it + montant_total_penalites_it"
    # reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(personne, period, parameters):
        montant_it_du = personne('montant_it_du', period)
        montant_total_deductions_it = personne('montant_total_deductions_it', period)
        montant_total_penalites_it = personne('montant_total_penalites_it', period)
        return montant_it_du - montant_total_deductions_it + montant_total_penalites_it


class montant_it_total_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Montant total d'IT du par les entreprises du pays"

    def formula(pays, period, parameters):
        it_du = pays.members('montant_it_du', period)
        return pays.sum(it_du)


class redevable_it(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    label = u"Défini si l'entreprise est éligible à l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(personne, period, parameters):
        redevable_tpe = personne('redevable_tpe', period)
        type_societe = personne('type_societe', period)
        option_is = personne('option_is', period) == OuiNon.O
        option_it = personne('option_it', period) == OuiNon.O
        SNC_sans_option_IS = (type_societe == TypeSociete.SNC) * not_(option_is)
        EI_non_redevable_tpe = not_(redevable_tpe) * (type_societe == TypeSociete.EI)
        EURL_avec_option_IT = (type_societe == TypeSociete.EURL) * option_it
        return SNC_sans_option_IS + EI_non_redevable_tpe + EURL_avec_option_IT


class option_it(Variable):
    value_type = Enum
    entity = Personne
    possible_values = OuiNon
    default_value = OuiNon.N
    definition_period = YEAR
    label = u"Défini si l'entreprise à opté pour l'IT plutot que l'IS (applicable aux EURL)"
    # reference = "https://law.gov.example/income_tax"  # Always use the most official source


class option_it_possible(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    label = u"Indique que l'entreprise peut opter pour l'IT plutot que l'IT"
    # reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(personne, period, parameters):
        type_societe = personne('type_societe', period)
        return type_societe == TypeSociete.EURL
