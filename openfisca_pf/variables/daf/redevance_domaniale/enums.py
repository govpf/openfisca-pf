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
    Mois = u'Mois' ##peut-être plus utile si on rammmèène à une unité journalière?
    Annees = u'Années'


class ZonesOccupations(Enum):
    zone_0 = u'Non applicable'
    zone_1 = u'Zone 1'
    zone_2 = u'Zone 2'
    zone_3 = u'Zone 3'
    zone_4 = u'Zone 4'


class TypesNatureEmprise(Enum):
    equipement_du_pays = u'Equipement du pays'
    terrain_de_sport_avec_electricite = u'Terrain de sport avec électricité'
    terrain_de_sport_sans_electricite = u'Terrain de sport sans électricité'
    infrastructure_de_restauration_aeroportuaire = u'Infrastructure de restauration aéroportuaire'
    bati_cas_general = u'Bâti (cas général)'
    boutique_de_produit_locaux_zone_aeroportuaire = u'Boutique de produit locaux (zone aéroportuaire)'
    ouvrage_d_amenagement_de_defense_ou_d_accessibilite = u'Ouvrage d\'aménagement, de défense ou d\'accessibilité'
    emprise_maritime_privatisee = u'Emprise maritime privatisée'
    vente_de_produits_locaux_zone_aeroportuaire = u'Vente de produits locaux (zone aéroportuaire)'
    emprise_activite_lucrative = u'Emprise dédiée à une activité lucrative'
    installation_technique = u'Installation technique'
    vente_etale = u'Vente à l étale'
    restauration_ambulante = u'Restauration ambulante'
