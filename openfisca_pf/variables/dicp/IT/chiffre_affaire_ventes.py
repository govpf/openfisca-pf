# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *

# class activitesVentes(Enum):
#     __order__ = "apport_en_societe bagettes_revente_au_detail ventes_sans_abattement"
#     apport_en_societe = u'APPORT EN SOCIÉTÉ'
#     bagettes_revente_au_detail = u'BAGUETTES (REVENTE AU DETAIL)'
#     ventes_sans_abattement = u'VENTES SANS ABATTEMENT'

# class activitesPrestations(Enum):
#     __order__ = "acconage_de_coprah armateurs boulangeries_autres"
#     acconage_de_coprah = u'ACCONAGE DE COPRAH'
#     armateurs = u'ARMATEURS'
#     boulangeries_autres = u'BOULANGERIE - AUTRES'

class chiffre_affaire_total_ventes(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant total du chiffre d'affaire concernant des ventes avant abattement"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(entreprise, period, parameters):
        value = 0
        for nom in [*parameters(period).dicp.it.abattements_it.ventes]:
            value += entreprise('chiffre_affaire_' + nom, period)
        return value

class chiffre_affaire_total_ventes_apres_abattement_assiette(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant total du chiffre d'affaire concernant des ventes après abattement"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(entreprise, period, parameters):
        value = 0
        for nom in [*parameters(period).dicp.it.abattements_it.ventes]:
            value += entreprise('chiffre_affaire_' + nom, period) * (1 - parameters(period).dicp.it.abattements_it.ventes[nom].coeff_assiette)
        return value

class chiffre_affaire_apport_en_societe(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie apport en société"

class chiffre_affaire_bagettes_revente_au_detail(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie revente au étail"

class chiffre_affaire_ventes_sans_abattement(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie ventes sans abattement"
