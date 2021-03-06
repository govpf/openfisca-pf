# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
import numpy


class chiffre_affaire_total_ventes(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant total du chiffre d'affaire concernant des ventes avant abattement"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(entreprise, period, parameters):
        value = 0
        for nom in [*parameters(period).dicp.abattements_it_cstns.activites_ventes]:
            ca = numpy.floor(entreprise('chiffre_affaire_' + nom, period) / 1000) * 1000
            value += ca
        return value


class chiffre_affaire_apport_en_societe(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Apport en société"


class chiffre_affaire_baguettes_revente_au_detail(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Bagettes revente au détail"


class chiffre_affaire_coprah(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Coprah"


class chiffre_affaire_farine_riz_sucre(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Farine, riz, sucre"


class chiffre_affaire_hydrocarbures_au_detail(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Hydrcarbures au détail"


class chiffre_affaire_importateurs_grossistes(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Importateurs grossistes"


class chiffre_affaire_lait_frais(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Lait frais"


class chiffre_affaire_negociants_detaillants_ca_superieur_20mf(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Négociants détaillants CA > 20M"


class chiffre_affaire_tabacs(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Tabacs"


class chiffre_affaire_timbres_postes_et_fiscaux(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Timbres postes et fiscaux"


class chiffre_affaire_ventes_sans_abattement(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Ventes sans abattement"


class chiffre_affaire_ventes_a_l_aventure_armateurs(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Ventes à l'aventure (armateurs)"


class chiffre_affaire_ventes_a_l_aventure_goelettes(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Ventes à l'aventure (goelettes)"


class chiffre_affaire_ventes_en_gros(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Ventes en gros"


class chiffre_affaire_vente_gros_lait_frais(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Ventes en gros lait frais d'origine local"


class chiffre_affaire_ventes_inferieur_20_millions(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Ventes < 20 millions"
