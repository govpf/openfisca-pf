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
    ##Tarif de type_1 (calcul de type part_fixe + part_unitaire * nombre_element + part_surfacique * surface)
    bati_cas_general = u'Bâti (cas général)'
    emprise_activite_lucrative = u'Emprise dédiée à une activité lucrative'
    equipement_du_pays = u'Equipement du pays'
    installation_technique = u'Installation technique'

    ##Tarif de type_2 (les paramètres du type_1 dépendent de la zone géographique)
    vente_etale = u'Vente à l étale'
    
    ##Tarif de type_3 (calculs selon des paliers sur un tarif journalier dégressif avec la durée d'occupation)
    activite_lucrative_inf_3mois = u'Activité lucrative de mois de 3 mois'
    activite_alimentaire_lucrative_inf_3mois = u'Activité alimentaire à but lucratif de moins de 3 mois'
    terrain_sport_ac_elec = u'Terrain de sport avec éléctricité'
    terrain_sport_sans_elec = u'Terrain de sport sans éléctricité'
    surface_mineralise_ac_elec = u'Surface minéralisée avec électricité'
    surface_mineralise_sans_elec = u'Surface minéralisée sans électricité'
    espace_pelouse_ac_elec = u'Espace pelouse avec électricité'
    espace_pelouse_sans_elec = u'Espace pelouse sans électricité'
    bati_tout_public_ac_elec = u'Bâti à usage tout public avec électricité'
    bati_tout_public_sans_elec = u'Bâti à usage tout public sans électricité'

    ##Emprise de test
    test_fonction_palier = u'test fonction pallier'
    test_fonction_palier_zone = u'test fonction pallier zone'