# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# # Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.base import *


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
    equipement_du_pays = u'Equipement du pays'
    terrain_de_sport_avec_electricite = u'Terrain de sport avec électricité'
    terrain_de_sport_sans_electricite = u'Terrain de sport sans électricité'
    infrastructure_de_restauration_aeroportuaire = u'Infrastructure de restauration aéroportuaire'
    bati_cas_general = u'Bâti (cas général)'
    boutique_de_produit_locaux_zone_aeroportuaire = u'Boutique de produit locaux (zone aéroportuaire)'
    ouvrage_d_amenagement_de_defense_ou_d_accessibilite = u'Ouvrage d\'aménagement, de défense ou d\'accessibilité'
    emprise_maritime_privatisee = u'Emprise maritime privatisée'
    vente_de_produits_locaux_zone_aeroportuaire = u'Vente de produits locaux (zone aéroportuaire)'


class duree_occupation_redevance_domaniale(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Durée de l'occupation du domaine"


class unite_duree_occupation_redevance_domaniale(Variable):
    value_type = Enum
    possible_values = UnitesDuree
    default_value = UnitesDuree.Jours
    entity = Personne
    definition_period = DAY
    label = "Unité de la durée d'occupation (heures, jours, mois, années...)"


class duree_occupation_redevance_domaniale_annee(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "La durée d'occupation en année"

    def formula(personne, period, parameters):
        duree_occupation_redevance_domaniale = personne('duree_occupation_redevance_domaniale', period)
        unite_duree_occupation_redevance_domaniale = personne('unite_duree_occupation_redevance_domaniale', period)
        value = select(
            [unite_duree_occupation_redevance_domaniale == UnitesDuree.Annees, unite_duree_occupation_redevance_domaniale == UnitesDuree.Mois, unite_duree_occupation_redevance_domaniale == UnitesDuree.Jours, unite_duree_occupation_redevance_domaniale == UnitesDuree.Heures],
            [duree_occupation_redevance_domaniale, duree_occupation_redevance_domaniale / 12, duree_occupation_redevance_domaniale / 365, duree_occupation_redevance_domaniale / (365 * 8)],
            )
        return value


class nombre_unite_redevance_domaniale(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Nombre d'unités dans l'occupation du domaine"


class surface_redevance_domaniale(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Surface de l'occupation du domaine"


class zone_occupation_redevance_domaniale(Variable):
    value_type = Enum
    possible_values = ZonesOccupations
    default_value = ZonesOccupations.zone_0
    entity = Personne
    definition_period = DAY
    label = "Zone de l'occupation du domaine"


class nature_emprise_occupation_redevance_domaniale(Variable):
    value_type = Enum
    possible_values = TypesNatureEmprise
    default_value = TypesNatureEmprise.equipement_du_pays
    entity = Personne
    definition_period = DAY
    label = "Type de nature d'emprise"


class montant_redevance_domaniale(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de la redevance domaniale dûe"

    def formula(personne, period, parameters):
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        type_calcul = int(parameters(period).daf.redevance_domaniale.type_calcul[nature_emprise_occupation_redevance_domaniale])
        return personne('montant_redevance_domaniale_type_' + str(type_calcul), period)


class montant_redevance_domaniale_type_1(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de la redevance domaniale dûe calcul type 1"

    def formula(personne, period, parameters):
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        surface_redevance_domaniale = personne('surface_redevance_domaniale', period)
        nombre_unite_redevance_domaniale = personne('nombre_unite_redevance_domaniale', period)
        duree_occupation_redevance_domaniale_annee = personne('duree_occupation_redevance_domaniale_annee', period)
        part_fixe = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale].part_fixe
        part_variable = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale].part_variable
        return (part_fixe * nombre_unite_redevance_domaniale + part_variable * surface_redevance_domaniale) * duree_occupation_redevance_domaniale_annee


class montant_redevance_domaniale_type_2(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de la redevance domaniale dûe calcul type 2"

    def formula(personne, period, parameters):
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        zone_occupation_redevance_domaniale = personne('zone_occupation_redevance_domaniale', period)
        surface_redevance_domaniale = personne('surface_redevance_domaniale', period)
        duree_occupation_redevance_domaniale_annee = personne('duree_occupation_redevance_domaniale_annee', period)
        montant_minimum = parameters(period).daf.redevance_domaniale.type_2[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].montant_minimum
        part_variable = parameters(period).daf.redevance_domaniale.type_2[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].part_variable
        return max_(part_variable * surface_redevance_domaniale * duree_occupation_redevance_domaniale_annee, montant_minimum * duree_occupation_redevance_domaniale_annee)


class montant_redevance_domaniale_type_3(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de la redevance domaniale dûe calcul type 3"

    def formula(personne, period, parameters):
        return 3


class montant_redevance_domaniale_type_4(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de la redevance domaniale dûe calcul type 4"

    def formula(personne, period, parameters):
        return 4
