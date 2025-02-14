# -*- coding: utf-8 -*-

from openfisca_pf.base import (
    ArrayLike,
    Parameters,
    Period,
    Variable,
    YEAR
    )
from openfisca_pf.constants.units import XPF
from openfisca_pf.entities import Personne


class charges_total_prestations(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant total des charges concernant des prestations avant abattement"
    reference = "https://law.gov.example/income_tax"
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        value = 0
        for activite in [*parameters(period).dicp.abattements_it_cstns.activites_prestations]:
            value += personne(f'charges_{activite}', period, parameters)
        return value


class charges_acconage_de_coprah(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Acconage de coprah"
    unit = XPF


class charges_armateurs(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Armateurs"
    unit = XPF


class charges_armateurs_de_goelettes(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Armateurs de goelettes"
    unit = XPF


class charges_artisans(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Artisans"
    unit = XPF


class charges_atelier_de_mecanique(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Atelier de mécanique"
    unit = XPF


class charges_blanchisseur(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Blanchisseur"
    unit = XPF


class charges_boucher_en_detail(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Boucher en détail"
    unit = XPF


class charges_boulangerie_autres(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie boulangerie autres"
    unit = XPF


class charges_boulangerie_baguettes_detail(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie boulangerie baguettes détail"
    unit = XPF


class charges_boulangerie_baguettes_gros(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie boulangerie baguettes gros"
    unit = XPF


class charges_bourrelier(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Bourrelier"
    unit = XPF


class charges_charcutier(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Charcutier"
    unit = XPF


class charges_coiffeur(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Coiffeur"
    unit = XPF


class charges_autres_natures_de_prestation_de_services(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Autre natures de prestation de services"
    unit = XPF


class charges_location_meublee(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Location meublée"
    unit = XPF


class charges_location_non_meublee(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Location non meublée"
    unit = XPF


class charges_location_terrains_nus(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Location terrain nu"
    unit = XPF


class charges_cordonnier_reparateur(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Cordonnier réparateur"
    unit = XPF


class charges_couturier(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Couturier"
    unit = XPF


class charges_cuisine_a_emporter_en_detail(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Cuisine à emporter en détail"
    unit = XPF


class charges_debitant_de_boissons_hygieniques_sur_place(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Débitant de boissons hygiéniques sur place"
    unit = XPF


class charges_denrees_emporter_ou_sur_place(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie  Denrées emporter ou sur place"
    unit = XPF


class charges_electricien(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Electricien"
    unit = XPF


class charges_entreprise_de_travaux_publics(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie  Entreprise de travaux publics"
    unit = XPF


class charges_fabricant_de_boissons_gazeuses(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie  Fabricant de boissons gazeuses"
    unit = XPF


class charges_ferblantier(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Ferblantier"
    unit = XPF


class charges_garagiste(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Garagiste"

    unit = XPF


class charges_hotel_pension_famille(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Hôtel, pension famille, ..."
    unit = XPF


class charges_loueur_de_meubles_objets_ou_ustensiles(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie  Loueur de meubles, objets ou ustensiles"
    unit = XPF


class charges_marchand_ambulant(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie  Marchand ambulant"
    unit = XPF


class charges_matelassier(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Matelassier"
    unit = XPF


class charges_mecanicien_reparateur(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie  Mécanicien réparateur"
    unit = XPF


class charges_menuisier(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Menuisier"
    unit = XPF


class charges_patissier(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Patissier"
    unit = XPF


class charges_photographe_ambulant(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie  Photographe ambulant"
    unit = XPF


class charges_plomberie_et_installation_sanitaire(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Plomberie et installation sanitaire"
    unit = XPF


class charges_prestations_avec_reduction(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Prestations avec réduction"
    unit = XPF


class charges_prestations_sans_reduction(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie  Prestations sans réduction"
    unit = XPF


class charges_profession_liberale(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie  Profession libérale"
    unit = XPF


class charges_reparateur_de_cycles_et_pneumatiques(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie  Réparateur de cycles et pneumatiques"
    unit = XPF


class charges_restaurants_hors_licence_classe_4(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie  Restaurants hors licence classe 4"
    unit = XPF


class charges_serrurier(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Serrurier"
    unit = XPF


class charges_soudeur(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Soudeur"
    unit = XPF


class charges_tailleur(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Tailleur"
    unit = XPF


class charges_toliercarossier(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Tolier-carossier"
    unit = XPF


class charges_torrefacteur_de_cafe(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Torrefacteur de café"
    unit = XPF


class charges_transporteur_de_marchandises(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Transporteur de marchandises"
    unit = XPF


class charges_transporteur_de_voyageurs_et_marchandises(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Transporteur de voyageurs et marchandises"
    unit = XPF


class charges_vannerie(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Vannerie"
    unit = XPF
