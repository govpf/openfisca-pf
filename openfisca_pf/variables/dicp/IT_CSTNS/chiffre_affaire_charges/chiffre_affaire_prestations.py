# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
import numpy


class chiffre_affaire_total_prestations(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant total du chiffre d'affaire concernant des prestations avant abattement"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source
    unit = "currency-XPF"

    # The formula to compute the income tax for a given person at a given period
    def formula(personne, period, parameters):
        value = 0
        for nom in [*parameters(period).dicp.abattements_it_cstns.activites_prestations]:
            ca = numpy.floor(personne('chiffre_affaire_' + nom, period) / 1000) * 1000
            value += ca
        return value


class chiffre_affaire_acconage_de_coprah(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Acconage de coprah"
    unit = "currency-XPF"


class chiffre_affaire_armateurs(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Armateurs"
    unit = "currency-XPF"


class chiffre_affaire_armateurs_de_goelettes(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Armateurs de goelettes"
    unit = "currency-XPF"


class chiffre_affaire_artisans(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Artisans"
    unit = "currency-XPF"


class chiffre_affaire_atelier_de_mecanique(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Atelier de mécanique"
    unit = "currency-XPF"


class chiffre_affaire_blanchisseur(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Blanchisseur"
    unit = "currency-XPF"


class chiffre_affaire_boucher_en_detail(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Boucher en détail"
    unit = "currency-XPF"


class chiffre_affaire_boulangerie_autres(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie boulangerie autres"
    unit = "currency-XPF"


class chiffre_affaire_boulangerie_baguettes_detail(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie boulangerie baguettes détail"
    unit = "currency-XPF"


class chiffre_affaire_boulangerie_baguettes_gros(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie boulangerie baguettes gros"
    unit = "currency-XPF"


class chiffre_affaire_bourrelier(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Bourrelier"
    unit = "currency-XPF"


class chiffre_affaire_charcutier(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Charcutier"
    unit = "currency-XPF"


class chiffre_affaire_coiffeur(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Coiffeur"
    unit = "currency-XPF"


class chiffre_affaire_autres_natures_de_prestation_de_services(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Autre natures de prestation de services"
    unit = "currency-XPF"


class chiffre_affaire_location_meublee(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Location meublée"
    unit = "currency-XPF"

    def formula(personne, period, parameters):
        # We return something not 0 if the flag activite_location is set (for TPE evaluation)
        activite_location = personne('activite_location', period)
        return activite_location * 1


class chiffre_affaire_location_non_meublee(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Location non meublée"
    unit = "currency-XPF"


class chiffre_affaire_location_terrains_nus(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Location terrain nu"
    unit = "currency-XPF"


class chiffre_affaire_cordonnier_reparateur(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Cordonnier réparateur"
    unit = "currency-XPF"


class chiffre_affaire_couturier(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Couturier"
    unit = "currency-XPF"


class chiffre_affaire_cuisine_a_emporter_en_detail(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Cuisine à emporter en détail"
    unit = "currency-XPF"


class chiffre_affaire_debitant_de_boissons_hygieniques_sur_place(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Débitant de boissons hygiéniques sur place "
    unit = "currency-XPF"


class chiffre_affaire_denrees_emporter_ou_sur_place(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie  Denrées emporter ou sur place"
    unit = "currency-XPF"


class chiffre_affaire_electricien(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Electricien"
    unit = "currency-XPF"


class chiffre_affaire_entreprise_de_travaux_publics(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie  Entreprise de travaux publics"
    unit = "currency-XPF"


class chiffre_affaire_fabricant_de_boissons_gazeuses(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie  Fabricant de boissons gazeuses"
    unit = "currency-XPF"


class chiffre_affaire_ferblantier(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Ferblantier"
    unit = "currency-XPF"


class chiffre_affaire_garagiste(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Garagiste"
    unit = "currency-XPF"


class chiffre_affaire_hotel_pension_famille(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Hôtel, pension famille, ..."
    unit = "currency-XPF"


class chiffre_affaire_loueur_de_meubles_objets_ou_ustensiles(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie  Loueur de meubles, objets ou ustensiles"
    unit = "currency-XPF"


class chiffre_affaire_marchand_ambulant(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie  Marchand ambulant"
    unit = "currency-XPF"


class chiffre_affaire_matelassier(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Matelassier"
    unit = "currency-XPF"


class chiffre_affaire_mecanicien_reparateur(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie  Mécanicien réparateur"
    unit = "currency-XPF"


class chiffre_affaire_menuisier(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Menuisier"
    unit = "currency-XPF"


class chiffre_affaire_patissier(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Patissier"
    unit = "currency-XPF"


class chiffre_affaire_photographe_ambulant(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie  Photographe ambulant"
    unit = "currency-XPF"


class chiffre_affaire_plomberie_et_installation_sanitaire(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Plomberie et installation sanitaire"
    unit = "currency-XPF"


class chiffre_affaire_prestations_avec_reduction(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Prestations avec réduction"
    unit = "currency-XPF"


class chiffre_affaire_prestations_sans_reduction(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie  Prestations sans réduction"
    unit = "currency-XPF"


class chiffre_affaire_profession_liberale(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie  Profession libérale"
    unit = "currency-XPF"


class chiffre_affaire_reparateur_de_cycles_et_pneumatiques(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie  Réparateur de cycles et pneumatiques"
    unit = "currency-XPF"


class chiffre_affaire_restaurants_hors_licence_classe_4(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie  Restaurants hors licence classe 4"
    unit = "currency-XPF"


class chiffre_affaire_serrurier(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Serrurier"
    unit = "currency-XPF"


class chiffre_affaire_soudeur(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Soudeur"
    unit = "currency-XPF"


class chiffre_affaire_tailleur(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Tailleur"
    unit = "currency-XPF"


class chiffre_affaire_toliercarossier(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Tolier-carossier"
    unit = "currency-XPF"


class chiffre_affaire_torrefacteur_de_cafe(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Torrefacteur de café"
    unit = "currency-XPF"


class chiffre_affaire_transporteur_de_marchandises(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Transporteur de marchandises"
    unit = "currency-XPF"


class chiffre_affaire_transporteur_de_voyageurs_et_marchandises(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Transporteur de voyageurs et marchandises"
    unit = "currency-XPF"


class chiffre_affaire_vannerie(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Vannerie"
    unit = "currency-XPF"
