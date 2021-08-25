# -*- coding: utf-8 -*-

# This file defines the computation for occupation on public domain that relies the same computation as type_1,
# but the parameters depends on a area.
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# # Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.variables.daf.redevance_domaniale.enums import *
from openfisca_pf.base import *


class montant_test_scale(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY

    def formula(personne, period, parameters):
        # duree_occupation_redevance_domaniale_jour = personne('duree_occupation_redevance_domaniale_jour', period)

        return 3
# class montant_test_redevance_annuelle(Variable):
#     value_type = float
#     entity = Personne
#     definition_period = YEAR
#     label = "test pour calcul redevance annuelle"

#     def formula(personne, period, parameters):
#         nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
#         surface_redevance_domaniale = personne('surface_redevance_domaniale', period)
#         nombre_unite_redevance_domaniale = personne('nombre_unite_redevance_domaniale', period)
#         duree_occupation_redevance_domaniale_jour = personne('duree_occupation_redevance_domaniale_jour', period)
#         part_fixe = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale].part_fixe
#         part_unitaire = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale].part_unitaire
#         part_variable = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale].part_variable
#         montant_minimum = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale].montant_minimum
#         facteur_prorata = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale].facteur_prorata

#         return max_(part_fixe + part_unitaire * nombre_unite_redevance_domaniale + part_variable * surface_redevance_domaniale , montant_minimum) * duree_occupation_redevance_domaniale_annee
