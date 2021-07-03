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

class montant_redevance_domaniale_type_2(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de la redevance domaniale dûe avec un calcul dépendant de la zone géographique de la demande"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne, period, parameters):
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        surface_redevance_domaniale = personne('surface_redevance_domaniale', period)
        nombre_unite_redevance_domaniale = personne('nombre_unite_redevance_domaniale', period)
        duree_occupation_redevance_domaniale_jour = personne('duree_occupation_redevance_domaniale_jour', period)
        zone_occupation_redevance_domaniale = personne('zone_occupation_redevance_domaniale', period)
        part_fixe = parameters(period).daf.redevance_domaniale.type_2[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].part_fixe
        part_unitaire = parameters(period).daf.redevance_domaniale.type_2[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].part_unitaire
        part_surfacique = parameters(period).daf.redevance_domaniale.type_2[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].part_surfacique
        # montant_minimum = parameters(period).daf.redevance_domaniale.type_2[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].montant_minimum
        facteur_prorata = parameters(period).daf.redevance_domaniale.type_2[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].facteur_prorata

        return arrondiInf((part_fixe + part_unitaire * nombre_unite_redevance_domaniale + part_surfacique * surface_redevance_domaniale) * duree_occupation_redevance_domaniale_jour / facteur_prorata)



