# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

from openfisca_core.model_api import *
from openfisca_pf.entities import *
from openfisca_pf.variables.daf.rch.enums.enums import *
from openfisca_pf.base import *
from numpy import logical_and
from fractions import Fraction


class montant_droit_enregistrement(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant des droits d'enregistrement"
    reference = "A renseigner"

    def formula(personne, period, parameters):
        # possible formula functions
        def acquisition_formula():
            type_acheteur_rch = personne('type_acheteur_rch', period)
            type_bien_rch = personne('type_bien_rch', period)
            valeur_totale_bien_achat = personne('valeur_totale_bien_achat', period)
            montant_droit_enregistrement = select([
                type_acheteur_rch == TypeAcheteur.DroitCommun,
                logical_and(type_acheteur_rch == TypeAcheteur.PrimoAcquereur, type_bien_rch == TypeBien.TerrainNu),
                logical_and(type_acheteur_rch == TypeAcheteur.PrimoAcquereur, type_bien_rch != TypeBien.TerrainNu)
                ], [
                    parameters(period).daf.rch.droit_enregistrement.droit_commun.calc(valeur_totale_bien_achat),
                    parameters(period).daf.rch.droit_enregistrement.primo_acquereur_terrain_nu.calc(valeur_totale_bien_achat),
                    parameters(period).daf.rch.droit_enregistrement.primo_acquereur_terrain_bati.calc(valeur_totale_bien_achat)
                    ])
            return montant_droit_enregistrement

        def navire_formula():
            valeur_totale_bien_achat = personne('valeur_totale_bien_achat', period)
            return parameters(period).daf.rch.droit_enregistrement.vente_navire.calc(valeur_totale_bien_achat)

        def baux_formula():
            valeur_totale_bien_achat = personne('valeur_locative_bien', period)
            duree_bail_annee = personne('duree_bail_annee', period)
            scale = parameters(period).daf.rch.droit_enregistrement.baux
            rate = scale.calc(duree_bail_annee)
            return valeur_totale_bien_achat * rate

        # retrieve the demarche type to select the correct formula
        type_demarche = personne('type_demarche_rch', period)

        # compute the values using the correct formula
        montant_droit_enregistrement = select([
            type_demarche == TypeDemarche.Acquisition,
            type_demarche == TypeDemarche.Baux,
            type_demarche == TypeDemarche.Navire], [
            acquisition_formula(),
            baux_formula(),
            navire_formula()])

        return montant_droit_enregistrement


class montant_taxe_publicite(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de la taxe de publicité"
    reference = "A renseigner"

    def formula(personne, period, parameters):
        # Variables
        type_demarche = personne('type_demarche_rch', period)

        def acquisition_formula():
            valeur_totale_bien_achat = personne('valeur_totale_bien_achat', period)
            # Here we convert float value to a Fraction class to avoid potential floating-point precision errors
            # when dealing with very large or small numbers such as 0.001
            # https://docs.python.org/3/tutorial/floatingpoint.html
            rate = Fraction.from_float(parameters(period).daf.rch.taxe_publicite_immobiliere.acquisition.rate)
            return valeur_totale_bien_achat * rate

        def baux_formula():
            valeur_locative_bien = personne('valeur_locative_bien', period)
            duree_bail_annee = personne('duree_bail_annee', period)
            rate = parameters(period).daf.rch.taxe_publicite_immobiliere.baux.calc(duree_bail_annee)
            return valeur_locative_bien * rate

        # Calcul du montant
        montant_taxe_publicite = select([
            type_demarche == TypeDemarche.Acquisition,
            type_demarche == TypeDemarche.Baux], [
            acquisition_formula(),
            baux_formula()])

        return montant_taxe_publicite


class montant_plus_value(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de la plus-value immobilière"
    reference = "A renseigner"

    def formula(personne, period, parameters):
        # Variables
        valeur_plus_value_net = personne('valeur_plus_value_net', period)
        duree_possession_annee = personne('duree_possession_annee', period)

        # Parameters
        rate = parameters(period).daf.rch.plus_values_immobiliere.calc(duree_possession_annee)

        # Calcul du montant
        return valeur_plus_value_net * rate


# ===========================
# ===========================
# ===========================


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
