# -*- coding: utf-8 -*-

from openfisca_pf.base import (
    ArrayLike,
    floor,
    Parameters,
    Period,
    Variable,
    YEAR
    )
from openfisca_pf.entities import Personne
from openfisca_pf.constants.units import XPF, PER_ONE


class chiffre_affaire_total_prestations(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant total du chiffre d'affaire concernant des prestations avant abattement"
    reference = []
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        value = 0.
        for activite in [*parameters(period).dicp.abattements_it_cstns.activites_prestations]:
            chiffre_d_affaire_activite = personne(f'chiffre_affaire_{activite}', period)
            value += floor(chiffre_d_affaire_activite / 1000.) * 1000.
        return value


class chiffre_affaire_acconage_de_coprah(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Acconage de coprah"
    unit = XPF


class chiffre_affaire_armateurs(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Armateurs"
    unit = XPF


class chiffre_affaire_armateurs_de_goelettes(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Armateurs de goelettes"
    unit = XPF


class chiffre_affaire_artisans(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Artisans"
    unit = XPF


class chiffre_affaire_atelier_de_mecanique(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Atelier de mécanique"
    unit = XPF


class chiffre_affaire_blanchisseur(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Blanchisseur"
    unit = XPF


class chiffre_affaire_boucher_en_detail(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Boucher en détail"
    unit = XPF


class chiffre_affaire_boulangerie_autres(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie boulangerie autres"
    unit = XPF


class chiffre_affaire_boulangerie_baguettes_detail(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie boulangerie baguettes détail"
    unit = XPF


class chiffre_affaire_boulangerie_baguettes_gros(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie boulangerie baguettes gros"
    unit = XPF


class chiffre_affaire_bourrelier(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Bourrelier"
    unit = XPF


class chiffre_affaire_charcutier(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Charcutier"
    unit = XPF


class chiffre_affaire_coiffeur(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Coiffeur"
    unit = XPF


class chiffre_affaire_autres_natures_de_prestation_de_services(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Autre natures de prestation de services"
    unit = XPF


class chiffre_affaire_location_meublee(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Location meublée"
    unit = PER_ONE

    def formula(personne: Personne, period: Period, parameters: Parameters):
        # We return something not 0 if the flag activite_location is set (for TPE evaluation)
        activite_location = personne('activite_location', period, parameters)
        return activite_location * 1


class chiffre_affaire_location_non_meublee(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Location non meublée"
    unit = XPF


class chiffre_affaire_location_terrains_nus(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Location terrain nu"
    unit = XPF


class chiffre_affaire_cordonnier_reparateur(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Cordonnier réparateur"
    unit = XPF


class chiffre_affaire_couturier(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Couturier"
    unit = XPF


class chiffre_affaire_cuisine_a_emporter_en_detail(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Cuisine à emporter en détail"
    unit = XPF


class chiffre_affaire_debitant_de_boissons_hygieniques_sur_place(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Débitant de boissons hygiéniques sur place "
    unit = XPF


class chiffre_affaire_denrees_emporter_ou_sur_place(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie  Denrées emporter ou sur place"
    unit = XPF


class chiffre_affaire_electricien(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Electricien"
    unit = XPF


class chiffre_affaire_entreprise_de_travaux_publics(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie  Entreprise de travaux publics"
    unit = XPF


class chiffre_affaire_fabricant_de_boissons_gazeuses(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie  Fabricant de boissons gazeuses"
    unit = XPF


class chiffre_affaire_ferblantier(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Ferblantier"
    unit = XPF


class chiffre_affaire_garagiste(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Garagiste"
    unit = XPF


class chiffre_affaire_hotel_pension_famille(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Hôtel, pension famille, ..."
    unit = XPF


class chiffre_affaire_loueur_de_meubles_objets_ou_ustensiles(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie  Loueur de meubles, objets ou ustensiles"
    unit = XPF


class chiffre_affaire_marchand_ambulant(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie  Marchand ambulant"
    unit = XPF


class chiffre_affaire_matelassier(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Matelassier"
    unit = XPF


class chiffre_affaire_mecanicien_reparateur(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie  Mécanicien réparateur"
    unit = XPF


class chiffre_affaire_menuisier(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Menuisier"
    unit = XPF


class chiffre_affaire_patissier(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Patissier"
    unit = XPF


class chiffre_affaire_photographe_ambulant(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie  Photographe ambulant"
    unit = XPF


class chiffre_affaire_plomberie_et_installation_sanitaire(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Plomberie et installation sanitaire"
    unit = XPF


class chiffre_affaire_prestations_avec_reduction(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Prestations avec réduction"
    unit = XPF


class chiffre_affaire_prestations_sans_reduction(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie  Prestations sans réduction"
    unit = XPF


class chiffre_affaire_profession_liberale(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie  Profession libérale"
    unit = XPF


class chiffre_affaire_reparateur_de_cycles_et_pneumatiques(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie  Réparateur de cycles et pneumatiques"
    unit = XPF


class chiffre_affaire_restaurants_hors_licence_classe_4(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie  Restaurants hors licence classe 4"
    unit = XPF


class chiffre_affaire_serrurier(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Serrurier"
    unit = XPF


class chiffre_affaire_soudeur(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Soudeur"
    unit = XPF


class chiffre_affaire_tailleur(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Tailleur"
    unit = XPF


class chiffre_affaire_toliercarossier(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Tolier-carossier"
    unit = XPF


class chiffre_affaire_torrefacteur_de_cafe(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Torrefacteur de café"
    unit = XPF


class chiffre_affaire_transporteur_de_marchandises(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Transporteur de marchandises"
    unit = XPF


class chiffre_affaire_transporteur_de_voyageurs_et_marchandises(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Transporteur de voyageurs et marchandises"
    unit = XPF


class chiffre_affaire_vannerie(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Vannerie"
    unit = XPF
