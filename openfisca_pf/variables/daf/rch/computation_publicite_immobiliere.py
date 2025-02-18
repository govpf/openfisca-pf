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
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Montant des droits d'enregistrement"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=521011&idr=208&np=1"

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
            duree_bail_mois = personne('duree_bail_mois', period)
            scale = parameters(period).daf.rch.droit_enregistrement.baux
            rate = scale.calc(duree_bail_mois)

            return valeur_totale_bien_achat * duree_bail_mois * rate

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

        return arrondiSup(montant_droit_enregistrement)


class montant_taxe_publicite(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Montant de la taxe de publicité immobilière"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=521011&idr=208&np=1"

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
            duree_bail_mois = personne('duree_bail_mois', period)
            rate = parameters(period).daf.rch.taxe_publicite_immobiliere.baux.calc(duree_bail_mois)
            return arrondiSup(valeur_locative_bien * duree_bail_mois * rate)

        # Calcul du montant
        montant_taxe_publicite = select([
            type_demarche == TypeDemarche.Acquisition,
            type_demarche == TypeDemarche.Baux], [
            acquisition_formula(),
            baux_formula()])

        return montant_taxe_publicite


class montant_taxe_plus_value(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Montant de la taxe sur la plus-value immobilière"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=521011&idr=208&np=1"

    def formula(personne, period, parameters):
        # Variables
        valeur_plus_value_net = personne('valeur_plus_value_net', period)
        duree_possession_annee = personne('duree_possession_annee', period)

        # Parameters
        rate = parameters(period).daf.rch.plus_values_immobiliere.calc(duree_possession_annee)

        # Calcul du montant
        return arrondiSup(valeur_plus_value_net * rate)
