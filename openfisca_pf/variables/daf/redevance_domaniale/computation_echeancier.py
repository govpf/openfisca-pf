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
from openfisca_core import periods

class montant_redevance_domaniale_echeancier_jour(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    calculate_output = calculate_output_add

    def formula(personne, period, parameters):
        nature_emprise_occupation_redevance_domaniale_echeancier = personne('nature_emprise_occupation_redevance_domaniale_echeancier', period)
        variable_redevance_domaniale_echeancier = personne('variable_redevance_domaniale_echeancier', period)
        nombre_unite_redevance_domaniale_echeancier = personne('nombre_unite_redevance_domaniale_echeancier', period)
        date_validation_redevance_domaniale_echeancier = personne('date_validation_redevance_domaniale_echeancier', period)
        epsilon = timedelta64(1)
        # How many days since start of redevance
        nombre_jours_depuis_signature = (datetime64(period.start) - date_validation_redevance_domaniale_echeancier + epsilon).astype('timedelta64[D]').astype(int)
        part_fixe = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale_echeancier].part_fixe
        part_unitaire = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale_echeancier].part_unitaire
        part_variable = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale_echeancier].part_variable


        # premier_jour = nombre_jours_depuis_signature == 1
        duree_occupation_redevance_domaniale_echeancier = personne('duree_occupation_redevance_domaniale_echeancier', period)
        redevance_du = (nombre_jours_depuis_signature > 0) * (nombre_jours_depuis_signature <= duree_occupation_redevance_domaniale_echeancier)
        # print(redevance_du)
        return redevance_du * (part_fixe + part_unitaire * nombre_unite_redevance_domaniale_echeancier + part_variable * variable_redevance_domaniale_echeancier)


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
        duree_occupation_redevance_domaniale_echeancier = personne('duree_occupation_redevance_domaniale_echeancier', period)
        unite_insecable = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale_echeancier].unite_insecable
        nb_periode_mini = numpy.ceil(duree_occupation_redevance_domaniale_echeancier / unite_insecable)
        date_validation_redevance_domaniale_echeancier = personne('date_validation_redevance_domaniale_echeancier', period)
        # epsilon = timedelta64(1)
        date_deb_redevance = numpy.array(date_validation_redevance_domaniale_echeancier, dtype='datetime64')
        date_fin_redevance = date_deb_redevance + numpy.array(nb_periode_mini * unite_insecable, dtype='timedelta64[D]')
        date_debut_annee = datetime64(period.start) - 1
        date_fin_annee = datetime64(period.offset(1, 'year').start) - 1
        duree = min_(date_fin_redevance, date_fin_annee) - max_(date_deb_redevance, date_debut_annee)
        # print((duree > timedelta64(0)) * duree)
        
        nombre_jours_factures = ((duree > timedelta64(0)) * duree).astype('timedelta64[D]').astype(int)

        # Récupération des paramètres
        part_fixe = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale_echeancier].part_fixe
        part_unitaire = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale_echeancier].part_unitaire
        part_variable = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale_echeancier].part_variable
        montant_minimum = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale_echeancier].montant_minimum
        # nb_periode_mini = numpy.ceil(nombre_jours_factures / unite_insecable) # Use of ceil aims at taking into account that a started period has to be counted in the price
        # print(nb_periode_mini)
        # Calcul du montant
        montant_intermediaire = (part_fixe +
                        part_unitaire * nombre_unite_redevance_domaniale_echeancier +
                        part_variable * variable_redevance_domaniale_echeancier) * nombre_jours_factures / unite_insecable
                        #* nb_periode_mini

        # Comparaison avec le minimum
        montant_global = arrondiSup(max_(montant_intermediaire, nombre_jours_factures / unite_insecable * montant_minimum))
        # + majoration_redevance_domaniale

        return montant_global
