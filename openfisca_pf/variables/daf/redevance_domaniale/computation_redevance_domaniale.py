# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# # Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.variables.daf.redevance_domaniale.enums.enums import *
from openfisca_pf.base import *


class type_calcul_redevance_domaniale(Variable):
    value_type = str
    entity = Personne
    definition_period = DAY
    label = "Type de calcul utilisé"

    def formula(personne, period, parameters):
        # Variables
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        unite_duree_occupation_redevance_domaniale = personne('unite_duree_occupation_redevance_domaniale', period)
        duree_occupation_redevance_domaniale = personne('duree_occupation_redevance_domaniale', period)
        type_calcul = parameters(period).daf.redevance_domaniale.type_calcul[nature_emprise_occupation_redevance_domaniale]
        # Constantes
        nombre_heure_par_jour = parameters(period).daf.redevance_domaniale.constantes.nombre_heure_par_jour_rd

        # Selection selon un tarif horaire ou journalier
        # Pour les tarifs du SPJP, le mode de calcul pour une même emprise change si la durée est
        # exprimée en heure et pour une durée inférieure à la journée.
        # Pour distinguer le type de calcul horaire (et sélectionner donc le bon calcul), on ajoute arbitrairement 20 au type de calcul journalier.
        # Cet ajout de 20, permet de créer des nouveaux types de calculs dans le futur.
        # L'ensemble des tarifs spéciaux du SPJP sont de type = 3
        unite_est_heure = unite_duree_occupation_redevance_domaniale == UnitesDuree.Heures
        duree_inferieur_jour = duree_occupation_redevance_domaniale <= nombre_heure_par_jour
        tarif_spjp = type_calcul == 3
        type_calcul_inter = parameters(period).daf.redevance_domaniale.type_calcul[nature_emprise_occupation_redevance_domaniale] + 20 * unite_est_heure * duree_inferieur_jour * tarif_spjp

        # Transformation en entier et en string
        type_calcul = type_calcul_inter.astype(int).astype(str)
        return type_calcul


class montant_base_redevance_domaniale(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de base la redevance domaniale dûe"

    def formula(personne, period, parameters):
        type_calcul = personne('type_calcul_redevance_domaniale', period)
        return aggregateVariables(personne, period, 'montant_base_redevance_domaniale_type_', type_calcul)


class montant_total_redevance_domaniale(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de la redevance domaniale dûe"

    def formula(personne, period, parameters):
        type_calcul = personne('type_calcul_redevance_domaniale', period)
        return aggregateVariables(personne, period, 'montant_total_redevance_domaniale_type_', type_calcul)


class temporalite_redevance_domaniale(Variable):
    value_type = Enum
    possible_values = Temporalite
    default_value = Temporalite.Non_Applicable
    entity = Personne
    definition_period = DAY
    label = "Temporalite du tarif"

    def formula(personne, period, parameters):
        type_calcul = personne('type_calcul_redevance_domaniale', period)
        return aggregateVariables(personne, period, 'temporalite_redevance_domaniale_type_', type_calcul)


class montant_base_redevance_domaniale_dossier(Variable):
    value_type = float
    entity = Dossier
    definition_period = DAY
    label = u"Montant de base de redevance domaniale de toutes les demandes du dossier"

    def formula(dossier, period, parameters):
        montant_base_redevance_domaniale = dossier.members('montant_base_redevance_domaniale', period)
        return dossier.sum(montant_base_redevance_domaniale)


class montant_total_redevance_domaniale_dossier(Variable):
    value_type = float
    entity = Dossier
    definition_period = DAY
    label = u"Montant total de redevance domaniale de toutes les demandes du dossier"

    def formula(dossier, period, parameters):
        montant_total_redevance_domaniale = dossier.members('montant_total_redevance_domaniale', period)
        return dossier.sum(montant_total_redevance_domaniale)
