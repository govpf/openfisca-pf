# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# # Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *

class UnitesDuree(Enum):
    Heures = u'Heures'
    Jours = u'Jours'
    Mois = u'Mois'
    Annees = u'Années'


class ZonesOccupations(Enum):
    zone_0 = u'Non applicable'
    zone_1 = u'Zone 1'
    zone_2 = u'Zone 2'
    zone_3 = u'Zone 3'
    zone_4 = u'Zone 4'


class TypesNatureEmprise(Enum):
    # ##Tarif de type_1 (calcul de type part_fixe + part_unitaire * nombre_element + part_surfacique * surface)
    ip_eco_01_equipement_pays = u'Equipement du Pays'
    ip_eco_08_centre_artisanaux_aero = u'Centre artisanaux (zone aéroportuaire)'
    ip_eco_09_infra_restauration_tourisme = u'Infrastructure de restauration (sites touristiques)'
    ip_eco_10_boutique_vente_tourisme = u'Boutiques de vente (sites touristiques)'
    ip_eco_11_support_embarcation_legere = u'Support pour embarcation légère'
    co_eco_01_bati = u'Bâti (cas général)'
    co_eco_04_ouvrage_rehabilitation = u'Ouvrage de réhabilitation'
    co_eco_04_bati_perli = u'Bâti pour la perliculture et l aquaculture'
    em_eco_05_emprise_maririme_general = u'Emprise maritime (cas général)'
    em_eco_06_emprise_maritime_lucratif = u'Emprise dédiée à une activité lucrative'
    em_eco_08_emprise_eco_tourisme = u'Emprise éco-touristique'
    em_eco_09_activite_agricole_aero = u'Activités agricoles (zone aéroportuaire)'
    im_eco_06_activite_resto_mobile_aero = u'Activités de restauration mobiles (zone aéroportuaire)'
    im_eco_08_autres_lucrative = u'Autres activités lucratives  (zone aéroportuaire)'
    im_eco_10_activite_non_lucrative_inf_trim = u'Activité à but non lucratif de moins de 3 mois'
    if_eco_01_operu_hors_passe = u'Peche: Parc à Operu (Zone Hors passe)'
    if_eco_02_operu_passe = u'Peche: Parc à Operu (Zone passe)'
    if_eco_05_aquaculture_lagon = u'Aquaculture (hors perliculture) en lagon '
    if_eco_06_aquaculture_canalisation = u'Aquaculture : canalisations'
    if_eco_07_aquaculture_mer = u'Aquaculture (hors perliculture) en haute mer '
    if_eco_08_perliculture_collectage = u'Perliculture collectage'
    if_eco_09_perliculture_elevage = u'Perliculture élevage'
    if_eco_10_canalisation_publique = u'Canalisations publiques, SWAC, OSMOSER'
    if_eco_11_canalisation_secteur_prim = u'Canalisations secteur primaire'
    if_eco_12_canalisation_secteur_sec = u'Canalisations secteurs secondaire et tertiaire'
    if_eco_13_installation_technique = u'Installation technique'
    if_eco_14_support_publicitaire = u'Support publicitaire, comptoir accueil'
    if_eco_16_captage_eau_sousterraine = u'Captage d eau souterraine'
    ip_pr_05_support_embarcation_legere = u'Support pour embarcation légère'
    co_pr_01_bati = u'Bâti (cas général)'
    co_pr_03_ouvrage_rehabilitation = u'Ouvrage de réhabilitation'
    co_pr_04_habitation_zone_aero = u'Habitation (zone aéropotuaire)'
    em_pr_05_emprise_maririme_general = u'Emprise maritime (cas général)'
    em_pr_07_emprise_maritime_non_lucratif = u'Emprise maritime non lucrative'
    if_pr_03_support_publicitaire = u'Support publicitaire'
    if_pr_02_ancrage_sans_droit = u'Ancrage et/ou mouillage sans droit immobilier'

    # ##Tarif de type_2 (les paramètres du type_1 dépendent de la zone géographique)
    ip_eco_06_infra_restauration_aero = u'Infrastructure de restauration aéroportuaire'
    ip_eco_07_boutique_produit_local_aero = u'Boutique de produit locaux (zone aéroportuaire)'
    co_eco_02_ouvrage_defence = u'Ouvrage d aménagement, de défense ou d accessibilité'
    em_eco_07_emprise_maritime_prive = u'Emprise maritime privatisée'
    im_eco_01_activite_lucrative_manifestation = u'Activité lucrative annexe à une manifestation sportive'
    im_eco_05_marche_puces = u'Marché aux puces'
    im_eco_07_vente_produit_locaux_aero = u'Vente de produits locaux  (zone aéroportuaire)'
    im_eco_09_vente_etale = u'Vente à l étale'
    im_eco_13_restau_mobile = u'Restauration ambulante'
    if_eco_15_corp_mort = u'Corps-mort, ancrage, mouillage'
    if_eco_17_gestion_corp_mort = u'Activité de gestion des corps-morts et/ou ancrages, mouillage'
    ex_eco_01_dpf_hors_entite_publique = u'Domaine public fluvial Hors entité publique'
    ex_eco_02_dpf_pour_entite_publique = u'Domaine public fluvial pour entité publique'
    ex_eco_03_dpm_hors_entite_publique = u'Domaine public maritime Hors entité publique'
    ex_eco_04_dpm_pour_entite_publique = u'Domaine public maritime Pour entité publique'
    co_pr_02_ouvrage_defence = u'Ouvrage d aménagement, de défense ou d accessibilité'
    em_pr_06_emprise_maritime_prive = u'Emprise maritime privatisée'
    if_pr_01_ancrage_avec_droit_immo = u'Ancrage et/ou mouillage avec droit immobilier'

    # ##Tarif de type_3 (calculs selon des paliers sur un tarif journalier dégressif avec la durée d'occupation)
    # ip_eco_02_bati_tout_public_ac_elec = u'Bâti à usage tout public avec électricité'
    # ip_eco_03_terrain_sport_ac_elec = u'Terrain de sport avec éléctricité'
    # ip_eco_04_bati_tout_public_sans_elec = u'Bâti à usage tout public sans électricité'
    # ip_eco_05_terrain_sport_sans_elec = u'Terrain de sport sans électricité'
    # em_eco_01_espace_pelouse_ac_elec = u'Espace pelouse avec électricité'
    # em_eco_02_surface_mineral_ac_elec = u'Surface minéralisée avec électricité'
    # em_eco_03_espace_pelouse_sans_elec = u'Espace pelouse sans électricité'
    # em_eco_04_surface_mineral_sans_elec = u'Surface minéralisée sans électricité'
    # im_eco_11_activite_lucrative_inf_trim = u'Activité à but lucratif de moins de 3 mois'
    # im_eco_12_activite_alim_lucrative_inf_trim = u'Activité alimentaire à but lucratif de moins de 3 mois'
    # ip_pr_01_bati_tout_public_ac_elec = u'Bâti à usage tout public avec électricité'
    # ip_pr_02_terrain_sport_ac_elec = u'Terrain de sport avec électricité'
    # ip_pr_03_bati_tout_public_sans_elec = u'Bâti à usage tout public sans électricité'
    # ip_pr_04_terrain_sport_sans_elec = u'Terrain de sport sans électricité'
    # em_pr_01_espace_pelouse_ac_elec = u'Espace pelouse avec électricité'
    # em_pr_02_surface_mineral_ac_elec = u'Surface minéralisée avec électricité'
    # em_pr_03_espace_pelouse_sans_elec = u'Espace pelouse sans électricité'
    # em_pr_04_surface_mineral_sans_elec = u'Surface minéralisée sans électricité'

    # ##Tarif de type_4 (les paramètres du type_3 dépendent de la zone géographique)
    # im_eco_02_foire_produit_locaux = u'Foire de produits locaux'
    # im_eco_03_foire_commerciale = u'Foire commerciale'
    # im_eco_04_activite_ludique = u'Activité ludique'

    # ##Tarif de type_5 (calcul par pallier de surface)
    # if_eco_03_parc_poisson_hors_passe = u'Pêche : Parc à poissons et viviers (Zone hors passe)'
    # if_eco_04_parc_poisson_passe = u'Pêche : Parc à poissons et viviers (Zone passe)'

    ## Enum pour les tests de la fonction
    ## Test de type_1 (calcul de type part_fixe + part_unitaire * nombre_element + part_surfacique * surface)
    bati_cas_general = u'Blabla'
    emprise_activite_lucrative = u'blabla1'
    equipement_du_pays = u'blabla2'
    installation_technique = u'blabla3'

    ##Test de type_2 (les paramètres du type_1 dépendent de la zone géographique)
    vente_etale = u'blabla4'
    activite_lucrative_manif_sport = u'blabla25'
    extraction_essai = u'blabla26'

    ##Test de type_3 (calculs selon des paliers sur un tarif journalier dégressif avec la durée d'occupation)
    activite_lucrative_inf_3mois = u'blabla27'
    activite_alimentaire_lucrative_inf_3mois = u'blabla28'
    terrain_sport_ac_elec = u'blabla29'
    terrain_sport_sans_elec = u'blabla31'
    surface_mineralise_ac_elec = u'blabla32'
    surface_mineralise_sans_elec = u'blabla33'
    espace_pelouse_ac_elec = u'blabla34'
    espace_pelouse_sans_elec = u'blabla35'
    bati_tout_public_ac_elec = u'blabla36'
    bati_tout_public_sans_elec = u'blabla37'

    ##Emprise de test
    test_fonction_palier = u'test fonction palier'
    test_fonction_palier_zone = u'test fonction palier zone'

    ##Test de type_5
    test_fonction_palier_surface = u'Test palier surface'

    ##Tarif de type_6
    test_ancrage = u'Test ancrage'
