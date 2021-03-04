# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *


class charges_total_ventes(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant total des charges concernant des ventes avant abattement"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(entreprise, period, parameters):
        value = 0
        for nom in [*parameters(period).dicp.abattements_it_cstns.activites_ventes]:
            value += entreprise('charges_' + nom, period)
        return value


class charges_apport_en_societe(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Apport en société"


class charges_baguettes_revente_au_detail(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Bagettes revente au détail"


class charges_coprah(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Coprah"


class charges_farine_riz_sucre(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Farine, riz, sucre"


class charges_hydrocarbures_au_detail(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Hydrcarbures au détail"


class charges_importateurs_grossistes(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Importateurs grossistes"


class charges_lait_frais(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Lait frais"


class charges_negociants_detaillants_ca_superieur_20mf(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Négociants détaillants CA > 20M"


class charges_tabacs(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Tabacs"


class charges_timbres_postes_et_fiscaux(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Timbres postes et fiscaux"


class charges_ventes_sans_abattement(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Ventes sans abattement"


class charges_ventes_a_l_aventure_armateurs(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Ventes à l'aventure (armateurs)"


class charges_ventes_a_l_aventure_goelettes(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Ventes à l'aventure (goelettes)"


class charges_ventes_en_gros(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Ventes en gros"


class charges_vente_gros_lait_frais(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Ventes en gros lait frais d'origine local"


class charges_ventes_inferieur_20_millions(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Ventes < 20 millions"
