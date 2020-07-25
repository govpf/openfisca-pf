# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *

class chiffre_affaire_total_prestations(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant total du chiffre d'affaire concernant des prestations avant abattement"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(entreprise, period, parameters):
        value = 0
        for nom in [*parameters(period).dicp.it.abattements_it.prestations]:
            value += entreprise('chiffre_affaire_' + nom, period)
        return value

class chiffre_affaire_acconage_de_coprah(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie acconage de coprah"

class charges_acconage_de_coprah(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Charges dans la catégorie acconage de coprah"

class chiffre_affaire_armateurs(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie armateurs"

class charges_armateurs(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Charges dans la catégorie armateurs"

class chiffre_affaire_armateurs_de_goelettes(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie armateurs de goelettes"

class charges_armateurs_de_goelettes(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Charges dans la catégorie armateurs de goelettes"

class chiffre_affaire_artisans(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie artisans"

class charges_artisans(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Charges dans la catégorie artisans"

class chiffre_affaire_atelier_de_mecanique(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie atelier de mécanique"

class charges_atelier_de_mecanique(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Charges dans la catégorie atelier de mécanique"

class chiffre_affaire_blanchisseur(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie blanchisseur"

class charges_blanchisseur(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Charges dans la catégorie blanchisseur"

class chiffre_affaire_boucher_en_detail(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie boucher en detail"

class charges_boucher_en_detail(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Charges dans la catégorie boucher en detail"

class chiffre_affaire_boulangeries_autres(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie boulangeries autres"

class charges_boulangeries_autres(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Charges dans la catégorie boulangeries autres"

class chiffre_affaire_boulangeries_baguettes_detail(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie boulangeries baguettes detail"

class charges_boulangeries_baguettes_detail(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Charges dans la catégorie boulangeries baguettes detail"

class chiffre_affaire_autres_natures_de_prestation_de_services(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie autres natures de prestation de services"

class charges_autres_natures_de_prestation_de_services(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Charges dans la catégorie autres natures de prestation de services"

class chiffre_affaire_location_meublee(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie location meublee"

class charges_location_meublee(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Charges dans la catégorie location_meublee"

class chiffre_affaire_location_non_meublee(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie location non meublee"

class charges_location_non_meublee(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Charges dans la catégorie location non meublee"

class chiffre_affaire_location_terrain_nu(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie location terrain nu"

class charges_location_terrain_nu(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = "Charges dans la catégorie location terrain nu"
