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
    entity = Personne
    definition_period = YEAR
    label = u"Montant total du chiffre d'affaire concernant des ventes avant abattement"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source
    unit = "currency-XPF"
    default_value = 0

    # The formula to compute the income tax for a given person at a given period
    def formula(personne, period, parameters):
        value = 0
        for nom in [*parameters(period).dicp.abattements_it_cstns.activites_ventes]:
            ca = numpy.floor(personne('chiffre_affaire_' + nom, period) / 1000) * 1000
            value += ca
        return value


class chiffre_affaire_apport_en_societe(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Apport en société"
    unit = "currency-XPF"


class chiffre_affaire_baguettes_revente_au_detail(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Bagettes revente au détail"
    unit = "currency-XPF"


class chiffre_affaire_coprah(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Coprah"
    unit = "currency-XPF"


class chiffre_affaire_farine_riz_sucre(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Farine, riz, sucre"
    unit = "currency-XPF"


class chiffre_affaire_hydrocarbures_au_detail(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Hydrcarbures au détail"
    unit = "currency-XPF"


class chiffre_affaire_importateurs_grossistes(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Importateurs grossistes"
    unit = "currency-XPF"


class chiffre_affaire_lait_frais(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Lait frais"
    unit = "currency-XPF"


class chiffre_affaire_negociants_detaillants_ca_superieur_20mf(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Négociants détaillants CA > 20M"
    unit = "currency-XPF"


class chiffre_affaire_tabacs(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Tabacs"
    unit = "currency-XPF"


class chiffre_affaire_timbres_postes_et_fiscaux(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Timbres postes et fiscaux"
    unit = "currency-XPF"


class chiffre_affaire_ventes_sans_abattement(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Ventes sans abattement"
    unit = "currency-XPF"


class chiffre_affaire_ventes_a_l_aventure_armateurs(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Ventes à l'aventure (armateurs)"
    unit = "currency-XPF"


class chiffre_affaire_ventes_a_l_aventure_goelettes(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Ventes à l'aventure (goelettes)"
    unit = "currency-XPF"


class chiffre_affaire_ventes_en_gros(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Ventes en gros"
    unit = "currency-XPF"


class chiffre_affaire_vente_gros_lait_frais(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Ventes en gros lait frais d'origine local"
    unit = "currency-XPF"


class chiffre_affaire_ventes_inferieur_20_millions(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Ventes < 20 millions"
    unit = "currency-XPF"
