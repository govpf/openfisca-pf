# -*- coding: utf-8 -*-

# This file defines the computation for occupation on public domain that relies the same computation as type_1,
# but the parameters depends on a area.
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# # Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *

from numpy import datetime64, timedelta64
from openfisca_pf.base import *


class nombre_jours_occupation_domaniale_echeancier_annee(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    calculate_output = calculate_output_add

    def formula(personne, period, parameters):
        nature_emprise_occupation_redevance_domaniale_echeancier = personne('nature_emprise_occupation_redevance_domaniale_echeancier', period)
        duree_occupation_redevance_domaniale_echeancier = personne('duree_occupation_redevance_domaniale_echeancier', period)
        base_calcul_jour = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale_echeancier].base_calcul_jour
        nb_periode_mini = numpy.ceil(duree_occupation_redevance_domaniale_echeancier / base_calcul_jour)
        date_validation_redevance_domaniale_echeancier = personne('date_validation_redevance_domaniale_echeancier', period)
        # epsilon = timedelta64(1)
        date_debut_annee = datetime64(period.start) - 1
        date_fin_annee = datetime64(period.offset(1, 'year').start) - 1
        base_calcul_jour = where(base_calcul_jour == 365, date_fin_annee - date_debut_annee, base_calcul_jour)
        date_deb_redevance = numpy.array(date_validation_redevance_domaniale_echeancier, dtype='datetime64') - 1
        date_fin_redevance = date_deb_redevance + numpy.array(nb_periode_mini * base_calcul_jour, dtype='timedelta64[D]')
        duree = min_(date_fin_redevance, date_fin_annee) - max_(date_deb_redevance, date_debut_annee)
        return ((duree > timedelta64(0)) * duree).astype('timedelta64[D]').astype(int)


class montant_redevance_domaniale_echeancier_annee(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    calculate_output = calculate_output_add

    def formula(personne, period, parameters):
        nature_emprise_occupation_redevance_domaniale_echeancier = personne('nature_emprise_occupation_redevance_domaniale_echeancier', period)
        variable_redevance_domaniale_echeancier = personne('variable_redevance_domaniale_echeancier', period)
        nombre_unite_redevance_domaniale_echeancier = personne('nombre_unite_redevance_domaniale_echeancier', period)
        # majoration_redevance_domaniale = personne('majoration_redevance_domaniale', period)
        base_calcul_jour = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale_echeancier].base_calcul_jour
        date_debut_annee = datetime64(period.start) - 1
        date_fin_annee = datetime64(period.offset(1, 'year').start) - 1
        base_calcul_jour = where(base_calcul_jour == 365, (date_fin_annee - date_debut_annee).astype(int), base_calcul_jour)
        nombre_jours_factures = personne('nombre_jours_occupation_domaniale_echeancier_annee', period)
        # Parameters
        part_fixe = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale_echeancier].part_fixe
        part_unitaire = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale_echeancier].part_unitaire
        part_variable = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale_echeancier].part_variable
        montant_minimum = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale_echeancier].montant_minimum
        # nb_periode_mini = numpy.ceil(nombre_jours_factures / base_calcul_jour) # Use of ceil aims at taking into account that a started period has to be counted in the price
        # print(nb_periode_mini)
        # Price computation
        montant_intermediaire = (part_fixe + part_unitaire * nombre_unite_redevance_domaniale_echeancier + part_variable * variable_redevance_domaniale_echeancier) * nombre_jours_factures / base_calcul_jour

        # Minimum comparison
        montant_global = arrondiSup(max_(montant_intermediaire, nombre_jours_factures / base_calcul_jour * montant_minimum))
        # + majoration_redevance_domaniale

        return montant_global
