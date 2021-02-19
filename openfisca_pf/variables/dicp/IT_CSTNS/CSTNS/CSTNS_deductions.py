# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *


class abattement_cstns(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Abattement total de droit applique sur la CST NS :\n\n#abattement_cstns = #cstns_prestations_abattement_droits + #cstns_ventes_abattement_droits"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(entreprise, period, parameters):
        cstns_ventes_abattement_droits = entreprise('cstns_ventes_abattement_droits', period)
        cstns_prestations_abattement_droits = entreprise('cstns_prestations_abattement_droits', period)
        return round_(cstns_prestations_abattement_droits + cstns_ventes_abattement_droits)


# class montant_acompte_cstns_1(Variable):
#     value_type = float
#     entity = Entreprise
#     definition_period = YEAR
#     label = u"Montant du 1er acompte IT verse"


# class montant_acompte_cstns_2(Variable):
#     value_type = float
#     entity = Entreprise
#     definition_period = YEAR
#     label = u"Montant du 2eme acompte IT verse"


# class montant_declaration_provisoire_cstns(Variable):
#     value_type = float
#     entity = Entreprise
#     definition_period = YEAR
#     label = u"Montant de la CST NS calcule sur une declaration provisoire"


# class montant_credcstns_impot_cstns_1(Variable):
#     value_type = float
#     entity = Entreprise
#     definition_period = YEAR
#     label = u"Montant de credit d'impot IT 1"


# class montant_credcstns_impot_cstns_2(Variable):
#     value_type = float
#     entity = Entreprise
#     definition_period = YEAR
#     label = u"Montant de credit d'impot IT 2"


# class montant_credcstns_impot_cstns_3(Variable):
#     value_type = float
#     entity = Entreprise
#     definition_period = YEAR
#     label = u"Montant de credit d'impot IT 3"


# class montant_credcstns_impot_cstns_4(Variable):
#     value_type = float
#     entity = Entreprise
#     definition_period = YEAR
#     label = u"Montant de credit d'impot IT 4"


class montant_total_deductions_cstns(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant total des deductions IT à appliquer"

    # def formula(entreprise, period, parameters):
    #     montant_acompte_cstns_1 = entreprise('montant_acompte_cstns_1', period)
    #     montant_acompte_cstns_2 = entreprise('montant_acompte_cstns_2', period)
    #     montant_declaration_provisoire_cstns = entreprise('montant_declaration_provisoire_cstns', period)
    #     montant_credcstns_impot_cstns_1 = entreprise('montant_credcstns_impot_cstns_1', period)
    #     montant_credcstns_impot_cstns_2 = entreprise('montant_credcstns_impot_cstns_2', period)
    #     montant_credcstns_impot_cstns_3 = entreprise('montant_credcstns_impot_cstns_3', period)
    #     montant_credcstns_impot_cstns_4 = entreprise('montant_credcstns_impot_cstns_4', period)
    #     montant_deductions = montant_acompte_cstns_1 + montant_acompte_cstns_2 + montant_declaration_provisoire_cstns + montant_credcstns_impot_cstns_1 + montant_credcstns_impot_cstns_2 + montant_credcstns_impot_cstns_3 + montant_credcstns_impot_cstns_4
    #     return montant_deductions
