# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# # Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.variables.daf.rch.enums.enums import *
from openfisca_pf.base import *
from numpy import logical_and


class montant_droit_enregistrement(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant des droits d'enregistrement"
    reference = "A renseigner"

    def formula(personne, period, parameters):
        # Variables
        # type_demarche_rch = personne('type_demarche_rch', period)
        type_acheteur_rch = personne('type_acheteur_rch', period)
        type_bien_rch = personne('type_bien_rch', period)
        valeur_totale_bien_achat = personne('valeur_totale_bien_achat', period)

        # # Lors de demandes multiples avec des types de calculs différents, il est nécessaire de figer l'emprise sur une donnée existante pour le type associé.
        # nature_emprise_occupation_redevance_domaniale = where(type_calcul == '1', nature_emprise_occupation_redevance_domaniale.decode_to_str(), 'ip_eco_01_equipement_pays')
        # variable_redevance_domaniale = personne('variable_redevance_domaniale', period)
        # nombre_unite_redevance_domaniale = personne('nombre_unite_redevance_domaniale', period)
        # Parameters
        regime = select([
            type_acheteur_rch == TypeAcheteur.DroitCommun,
            logical_and(type_acheteur_rch == TypeAcheteur.PrimoAcquereur, type_bien_rch == TypeBien.TerrainNu),
            logical_and(type_acheteur_rch == TypeAcheteur.PrimoAcquereur, type_bien_rch != TypeBien.TerrainNu)
            ], [
                'droit_commun',
                'primo_acquereur_terrain_nu',
                'primo_acquereur_terrain_bati'
                ])

        init = parameters(period).daf.rch.droit_enregistrement[regime].init
        rate_0 = parameters(period).daf.rch.droit_enregistrement[regime].rate_0
        threshold_1 = parameters(period).daf.rch.droit_enregistrement[regime].threshold_1
        rate_1 = parameters(period).daf.rch.droit_enregistrement[regime].rate_1

        # Calcul du montant
        montant_droit_enregistrement = select([
            valeur_totale_bien_achat < threshold_1,
            valeur_totale_bien_achat > threshold_1
            ], [
                init + rate_0 * valeur_totale_bien_achat,
                init + rate_0 * threshold_1 + rate_1 * (valeur_totale_bien_achat - threshold_1),
                ])

        return montant_droit_enregistrement


class montant_droit_publicite(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant des droits de publicité"
    reference = "A renseigner"

    def formula(personne, period, parameters):
        # Variables
        # type_demarche_rch = personne('type_demarche_rch', period)
        type_acheteur_rch = personne('type_acheteur_rch', period)
        type_bien_rch = personne('type_bien_rch', period)
        valeur_totale_bien_achat = personne('valeur_totale_bien_achat', period)

        # # Lors de demandes multiples avec des types de calculs différents, il est nécessaire de figer l'emprise sur une donnée existante pour le type associé.
        # nature_emprise_occupation_redevance_domaniale = where(type_calcul == '1', nature_emprise_occupation_redevance_domaniale.decode_to_str(), 'ip_eco_01_equipement_pays')
        # variable_redevance_domaniale = personne('variable_redevance_domaniale', period)
        # nombre_unite_redevance_domaniale = personne('nombre_unite_redevance_domaniale', period)
        # Parameters
        regime = select([
            type_acheteur_rch == TypeAcheteur.DroitCommun,
            logical_and(type_acheteur_rch == TypeAcheteur.PrimoAcquereur, type_bien_rch == TypeBien.TerrainNu),
            logical_and(type_acheteur_rch == TypeAcheteur.PrimoAcquereur, type_bien_rch != TypeBien.TerrainNu)
            ], [
                'droit_commun',
                'primo_acquereur_terrain_nu',
                'primo_acquereur_terrain_bati'
                ])

        init = parameters(period).daf.rch.droit_publicite_immobiliere[regime].init
        rate_0 = parameters(period).daf.rch.droit_publicite_immobiliere[regime].rate_0
        threshold_1 = parameters(period).daf.rch.droit_publicite_immobiliere[regime].threshold_1
        rate_1 = parameters(period).daf.rch.droit_publicite_immobiliere[regime].rate_1

        # Calcul du montant
        montant_droit_publicite = select([
            valeur_totale_bien_achat < threshold_1,
            valeur_totale_bien_achat > threshold_1
            ], [
                init + rate_0 * valeur_totale_bien_achat,
                init + rate_0 * threshold_1 + rate_1 * (valeur_totale_bien_achat - threshold_1),
                ])

        return montant_droit_publicite


class montant_taxe_publicite(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de la taxe de publicité"
    reference = "A renseigner"

    def formula(personne, period, parameters):
        # Variables
        # type_demarche_rch = personne('type_demarche_rch', period)
        valeur_totale_bien_achat = personne('valeur_totale_bien_achat', period)

        # # Lors de demandes multiples avec des types de calculs différents, il est nécessaire de figer l'emprise sur une donnée existante pour le type associé.
        # nature_emprise_occupation_redevance_domaniale = where(type_calcul == '1', nature_emprise_occupation_redevance_domaniale.decode_to_str(), 'ip_eco_01_equipement_pays')
        # variable_redevance_domaniale = personne('variable_redevance_domaniale', period)
        # nombre_unite_redevance_domaniale = personne('nombre_unite_redevance_domaniale', period)
        
        rate = parameters(period).daf.rch.taxe_publicite_immobiliere.rate

        # Calcul du montant
        montant_droit_publicite = rate * valeur_totale_bien_achat

        return montant_droit_publicite


class montant_total_a_payer(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant total à payer"
    reference = "A renseigner"

    def formula(personne, period, parameters):
        # Variables
        montant_droit_enregistrement = personne('montant_droit_enregistrement', period)
        montant_droit_publicite = personne('montant_droit_publicite', period)
        montant_taxe_publicite = personne('montant_taxe_publicite', period)

        # Calcul du montant
        montant_total_a_payer = montant_droit_enregistrement + montant_droit_publicite + montant_taxe_publicite

        return montant_total_a_payer


# class montant_base_redevance_domaniale_dossier(Variable):
#     value_type = float
#     entity = Dossier
#     definition_period = DAY
#     label = u"Montant de base de redevance domaniale de toutes les demandes du dossier"

#     def formula(dossier, period, parameters):
#         montant_base_redevance_domaniale = dossier.members('montant_base_redevance_domaniale', period)
#         return dossier.sum(montant_base_redevance_domaniale)


# class montant_total_redevance_domaniale_dossier(Variable):
#     value_type = float
#     entity = Dossier
#     definition_period = DAY
#     label = u"Montant total de redevance domaniale de toutes les demandes du dossier"

#     def formula(dossier, period, parameters):
#         montant_total_redevance_domaniale = dossier.members('montant_total_redevance_domaniale', period)
#         return dossier.sum(montant_total_redevance_domaniale)
