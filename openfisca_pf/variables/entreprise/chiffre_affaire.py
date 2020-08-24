# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
import numpy
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

class chiffre_affaire_total(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant total du chiffre d'affaire"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(entreprise, period, parameters):
        return entreprise('chiffre_affaire_total_ventes', period) + entreprise('chiffre_affaire_total_prestations', period)
 
class charges_total(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant total des charges"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(entreprise, period, parameters):
        return entreprise('charges_total_ventes', period) + entreprise('charges_total_prestations', period)
 
class chiffre_affaire_total_prestations(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant total du chiffre d'affaire concernant des prestations avant abattement"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(entreprise, period, parameters):
        value = 0
        for nom in [*parameters(period).dicp.it.abattements_it.activites_prestations]:
            ca = numpy.floor(entreprise('chiffre_affaire_' + nom, period) / 1000) * 1000
            value += ca
        return value

class charges_total_prestations(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant total des charges concernant des prestations avant abattement"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(entreprise, period, parameters):
        value = 0
        for nom in [*parameters(period).dicp.it.abattements_it.activites_prestations]:
            value += entreprise('charges_' + nom, period)
        return value

class chiffre_affaire_total_ventes(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant total du chiffre d'affaire concernant des ventes avant abattement"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(entreprise, period, parameters):
        value = 0
        for nom in [*parameters(period).dicp.it.abattements_it.activites_ventes]:
            ca = numpy.floor(entreprise('chiffre_affaire_' + nom, period) / 1000) * 1000
            value += ca
        return value

class charges_total_ventes(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant total des charges concernant des ventes avant abattement"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(entreprise, period, parameters):
        value = 0
        for nom in [*parameters(period).dicp.it.abattements_it.activites_ventes]:
            value += entreprise('charges_' + nom, period)
        return value

