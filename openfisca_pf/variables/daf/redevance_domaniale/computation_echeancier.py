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


class montant_redevance_domaniale_echeancier_jour(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    # calculate_output = calculate_output_add

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
    # calculate_output = calculate_output_add

    def formula(personne, period, parameters):
        # duree_occupation_redevance_domaniale_echeancier = personne('duree_occupation_redevance_domaniale_echeancier', period)
        nature_emprise_occupation_redevance_domaniale_echeancier = personne('nature_emprise_occupation_redevance_domaniale_echeancier', period)
        # unite_insecable = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale_echeancier].unite_insecable
        # nb_periode_mini =  numpy.ceil(duree_occupation_redevance_domaniale_echeancier/unite_insecable) ##Use of ceil aims at taking into account that a started period has to be counted in the price
        montant_minimum = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale_echeancier].montant_minimum

        total = arrondiSup(personne('montant_redevance_domaniale_echeancier_jour', period, options = [ADD]))
        return max_(total, montant_minimum )


# class montant_redevance_domaniale_echeancier_total(Variable):
#     value_type = float
#     entity = Personne
#     definition_period = ETERNITY

#     def formula(personne, period, parameters):
#         # duree_occupation_redevance_domaniale_echeancier = personne('duree_occupation_redevance_domaniale_echeancier', period)
#         # nature_emprise_occupation_redevance_domaniale_echeancier = personne('nature_emprise_occupation_redevance_domaniale_echeancier', period)
#         # unite_insecable = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale_echeancier].unite_insecable
#         # nb_periode_mini =  numpy.ceil(duree_occupation_redevance_domaniale_echeancier/unite_insecable) ##Use of ceil aims at taking into account that a started period has to be counted in the price
#         # montant_minimum = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale_echeancier].montant_minimum

#         total = personne('montant_redevance_domaniale_echeancier_annee', period, options = [ADD])
#         return total
