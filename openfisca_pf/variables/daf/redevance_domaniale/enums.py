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
    # The zoning depends on activities.
    # The basic zoning is made using the average price of seaside terrain
    # A second zoning is on the airport frequentation
    # A last zoning is on polynesian archipelagos
    zone_1 = u'Zone 1'
    zone_2 = u'Zone 2'
    zone_3 = u'Zone 3'
    zone_4 = u'Zone 4'
    zone_5 = u'Zone 5'


class TypesNatureEmprise(Enum):
    # Tarif de type_1 (calcul de type part_fixe + part_unitaire * nombre_element + part_surfacique * surface)
    ip_eco_01_equipement_pays = u'IP-ECO-01 Equipement du Pays'
    ip_eco_08_centre_artisanaux_aero = u'IP-ECO-08 Centre artisanaux (zone aéroportuaire)'
    ip_eco_09_infra_restauration_tourisme = u'IP-ECO-09 Infrastructure de restauration (sites touristiques)'
    ip_eco_10_boutique_vente_tourisme = u'IP-ECO-10 Boutiques de vente (sites touristiques)'
    ip_eco_11_support_embarcation_legere = u'IP-ECO-11 Support pour embarcation légère'
    co_eco_01_bati = u'CO-ECO-01 Bâti (cas général)'
    co_eco_03_ouvrage_rehabilitation = u'CO-ECO-03 Ouvrage de réhabilitation'
    co_eco_04_bati_perli = u'CO-ECO-04 Bâti pour la perliculture et l aquaculture'
    em_eco_05_emprise_maririme_general = u'EM-ECO-05 Emprise maritime (cas général)'
    em_eco_06_emprise_maritime_lucratif = u'EM-ECO-06 Emprise dédiée à une activité lucrative'
    em_eco_08_emprise_eco_tourisme = u'EM-ECO-08 Emprise éco-touristique'
    em_eco_09_activite_agricole_aero = u'EM-ECO-09 Activités agricoles (zone aéroportuaire)'
    im_eco_06_activite_resto_mobile_aero = u'IM-ECO-06 Activités de restauration mobiles (zone aéroportuaire)'
    im_eco_08_autres_lucrative = u'IM-ECO-08 Autres activités lucratives  (zone aéroportuaire)'
    im_eco_10_activite_non_lucrative_inf_trim = u'IM-ECO-10 Activité à but non lucratif de moins de 3 mois'
    if_eco_03_operu_hors_passe = u'IF-ECO-03 Peche: Parc à Operu (Zone Hors passe)'
    if_eco_04_operu_passe = u'IF-ECO-04 Peche: Parc à Operu (Zone passe)'
    if_eco_05_aquaculture_lagon = u'IF-ECO-05 Aquaculture (hors perliculture) en lagon '
    if_eco_06_aquaculture_canalisation = u'IF-ECO-06 Aquaculture : canalisations'
    if_eco_07_aquaculture_mer = u'IF-ECO-07 Aquaculture (hors perliculture) en haute mer '
    if_eco_08_perliculture_collectage = u'IF-ECO-08 Perliculture collectage'
    if_eco_09_perliculture_elevage = u'IF-ECO-09 Perliculture élevage'
    if_eco_10_canalisation_publique = u'IF-ECO-10 Canalisations publiques, SWAC, OSMOSER'
    if_eco_11_canalisation_secteur_prim = u'IF-ECO-11 Canalisations secteur primaire'
    if_eco_12_canalisation_secteur_sec = u'IF-ECO-12 Canalisations secteurs secondaire et tertiaire'
    if_eco_13_installation_technique = u'IF-ECO-13 Installation technique'
    if_eco_14_support_publicitaire = u'IF-ECO-14 Support publicitaire, comptoir accueil'
    if_eco_16_captage_eau_sousterraine = u'IF-ECO-16 Captage d eau souterraine'
    ip_pr_05_support_embarcation_legere = u'IP-PR-05 Support pour embarcation légère'
    co_pr_01_bati = u'CO-PR-01 Bâti (cas général)'
    co_pr_03_ouvrage_rehabilitation = u'CO-PR-03 Ouvrage de réhabilitation'
    co_pr_04_habitation_zone_aero = u'CO-PR-04 Habitation (zone aéropotuaire)'
    em_pr_05_emprise_maririme_general = u'EM-PR-05 Emprise maritime (cas général)'
    em_pr_07_emprise_maritime_non_lucratif = u'EM-PR-07 Emprise maritime non lucrative'
    if_pr_03_support_publicitaire = u'IF-PR-03 Support publicitaire'
    if_pr_02_ancrage_sans_droit = u'IF-PR-02 Ancrage et/ou mouillage sans droit immobilier'

    # Tarif de type_2 (les paramètres du type_1 dépendent de la zone géographique)
    ip_eco_06_infra_restauration_aero = u'IP-ECO-06 Infrastructure de restauration aéroportuaire'
    ip_eco_07_boutique_produit_local_aero = u'IP-ECO-07 Boutique de produit locaux (zone aéroportuaire)'
    co_eco_02_ouvrage_defence = u'CO-ECO-02 Ouvrage d aménagement, de défense ou d accessibilité'
    em_eco_07_emprise_maritime_prive = u'EM-ECO-07 Emprise maritime privatisée'
    im_eco_01_activite_lucrative_manifestation = u'IM-ECO-01 Activité lucrative annexe à une manifestation sportive'
    im_eco_05_marche_puces = u'IM-ECO-05 Marché aux puces'
    im_eco_07_vente_produit_locaux_aero = u'IM-ECO-07 Vente de produits locaux  (zone aéroportuaire)'
    im_eco_09_vente_etale = u'IM-ECO-09 Vente à l étale'
    im_eco_13_restau_mobile = u'IM-ECO-13 Restauration ambulante'
    if_eco_15_corp_mort = u'IF-ECO-15 Corps-mort, ancrage, mouillage'
    if_eco_17_gestion_corp_mort = u'IF-ECO-17 Activité de gestion des corps-morts et/ou ancrages, mouillage'
    co_pr_02_ouvrage_defence = u'CO-PR-02 Ouvrage d aménagement, de défense ou d accessibilité'
    em_pr_06_emprise_maritime_prive = u'EM-PR-06 Emprise maritime privatisée'
    if_pr_01_ancrage_avec_droit_immo = u'IF-PR-01 Ancrage et/ou mouillage avec droit immobilier'

    # Tarif de type_3 (calculs selon des paliers sur un tarif journalier dégressif avec la durée d'occupation)
    ip_eco_02_bati_tout_public_ac_elec = u'IP-ECO-02 Bâti à usage tout public avec électricité'
    ip_eco_03_terrain_sport_ac_elec = u'IP-ECO-03 Terrain de sport avec éléctricité'
    ip_eco_04_bati_tout_public_sans_elec = u'IP-ECO-04 Bâti à usage tout public sans électricité'
    ip_eco_05_terrain_sport_sans_elec = u'IP-ECO-05 Terrain de sport sans électricité'
    em_eco_01_espace_pelouse_ac_elec = u'EM-ECO-01 Espace pelouse avec électricité'
    em_eco_02_surface_mineral_ac_elec = u'EM-ECO-02 Surface minéralisée avec électricité'
    em_eco_03_espace_pelouse_sans_elec = u'EM-ECO-03 Espace pelouse sans électricité'
    em_eco_04_surface_mineral_sans_elec = u'EM-ECO-04 Surface minéralisée sans électricité'
    im_eco_11_activite_lucrative_inf_trim = u'IM-ECO-11 Activité à but lucratif de moins de 3 mois'
    im_eco_12_activite_alim_lucrative_inf_trim = u'IM-ECO-12 Activité alimentaire à but lucratif de moins de 3 mois'
    ip_pr_01_bati_tout_public_ac_elec = u'IP-PR-01 Bâti à usage tout public avec électricité'
    ip_pr_02_terrain_sport_ac_elec = u'IP-PR-02 Terrain de sport avec électricité'
    ip_pr_03_bati_tout_public_sans_elec = u'IP-PR-03 Bâti à usage tout public sans électricité'
    ip_pr_04_terrain_sport_sans_elec = u'IP-PR-04 Terrain de sport sans électricité'
    em_pr_01_espace_pelouse_ac_elec = u'EM-PR-01 Espace pelouse avec électricité'
    em_pr_02_surface_mineral_ac_elec = u'EM-PR-02 Surface minéralisée avec électricité'
    em_pr_03_espace_pelouse_sans_elec = u'EM-PR-03 Espace pelouse sans électricité'
    em_pr_04_surface_mineral_sans_elec = u'EM-PR-04 Surface minéralisée sans électricité'

    # Tarif de type_4 (les paramètres du type_3 dépendent de la zone géographique)
    im_eco_02_foire_produit_locaux = u'IM-ECO-02 Foire de produits locaux'
    im_eco_03_foire_commerciale = u'IM-ECO-03 Foire commerciale'
    im_eco_04_activite_ludique = u'IM-ECO-04 Activité ludique'
    im_eco_14_foire_locaux_agricoles = u'IM-ECO-14 Foire de produits locaux agricoles'

    # Tarif de type_5 (calcul par pallier de surface)
    if_eco_01_parc_poisson_hors_passe = u'IF-ECO-01 Pêche : Parc à poissons et viviers (Zone hors passe)'
    if_eco_02_parc_poisson_passe = u'IF-ECO-02 Pêche : Parc à poissons et viviers (Zone passe)'

    # Tarif Type_7 (indépendant de la durée) i.e extraction
    ex_eco_01_dpf_hors_entite_publique = u'EX-ECO-01 Domaine public fluvial Hors entité publique'
    ex_eco_02_dpf_pour_entite_publique = u'EX-ECO-02 Domaine public fluvial pour entité publique'
    ex_eco_03_dpm_hors_entite_publique = u'EX-ECO-03 Domaine public maritime Hors entité publique'
    ex_eco_04_dpm_pour_entite_publique = u'EX-ECO-04 Domaine public maritime Pour entité publique'

    # Tarif Type _8 (5 different areas)
    ag_priv_01_maraichage = u'AG-PRIV-01 Agriculture de type maraîchère, vivière, fruitière'
    ag_priv_02_elevage = u'AG-PRIV-02 Elevage'
    ag_priv_03_coprah = u'AG-PRIV-03 Coprah-Culture'
    ag_priv_04_agroforesterie = u'AG-PRIV-04 Agro-foresterie'
    ag_priv_05_agrotransformation = u'AG-PRIV-05 Agro-transformation'

    # Nature d'emprise pour le domaine privé (location)
    priv_01_touristique = u'PRIV-01 Aménagement touristique'
    priv_02_eco_industriel = u'PRIV-02 Opération économique ou industrielle'
    priv_03_projet_social = u'PRIV-03 Projet à caractère social, éducatif ou sportif'
    priv_04_etablissement_public = u'PRIV-04 Location au profit des établissements publics pour les besoins de leur fonctionnement '
    priv_05_habitat_social = u'PRIV-05 Habitat social'
    priv_06_developpement_durable = u'PRIV-06 Développement durable'
    priv_07_technologie_information = u'PRIV-07 Activités liées aux technologies, contenus et support de l information'
    priv_08_cultuel = u'PRIV-08 Projet à caractère cultuel'
    priv_09_autres = u'PRIV-09 Autre occupation'
