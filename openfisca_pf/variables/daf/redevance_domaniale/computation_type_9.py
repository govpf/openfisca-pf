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


class montant_base_redevance_domaniale_type_8(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de base (journalier, annuel, mensuel) de la redevance domaniale dûe avec un calcul dépendant de l'archipel'"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne, period, parameters):
        # Variables
        type_calcul = personne('type_calcul_redevance_domaniale', period)
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        nature_emprise_occupation_redevance_domaniale = where(type_calcul == '8', nature_emprise_occupation_redevance_domaniale.decode_to_str(), 'test_zone_archi')

        variable_redevance_domaniale = personne('variable_redevance_domaniale', period)
        nombre_unite_redevance_domaniale = personne('nombre_unite_redevance_domaniale', period)
        zone_occupation_redevance_domaniale = personne('zone_occupation_redevance_domaniale', period)

        # Parameters
        part_fixe = parameters(period).daf.redevance_domaniale.type_8[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].part_fixe
        part_unitaire = parameters(period).daf.redevance_domaniale.type_8[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].part_unitaire
        part_variable = parameters(period).daf.redevance_domaniale.type_8[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].part_variable
        montant_minimum = parameters(period).daf.redevance_domaniale.type_8[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].montant_minimum

        # Price computation
        montant_intermediaire = part_fixe + part_unitaire * nombre_unite_redevance_domaniale + part_variable * variable_redevance_domaniale

        # Minimum comparison
        montant_base = max_(arrondiSup(montant_intermediaire), montant_minimum)
        return where(type_calcul == '8', montant_base, 0)


class montant_total_redevance_domaniale_type_8(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant total de la redevance domaniale dûe avec un calcul dépendant de l'archipel'"
    reference = "Arrêté NOR DAF2120267AC-3"
    unit = 'currency-XPF'

    def formula(personne, period, parameters):
        # Variables
        type_calcul = personne('type_calcul_redevance_domaniale', period)
        # multiple occupation can be asked with different type of computation.
        # In order to avoid misinterpretation for array input, only the element with the good type is computed
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        nature_emprise_occupation_redevance_domaniale = where(type_calcul == '8', nature_emprise_occupation_redevance_domaniale.decode_to_str(), 'test_zone_archi')
        duree_occupation_redevance_domaniale_jour = personne('duree_occupation_redevance_domaniale_jour', period)
        majoration_redevance_domaniale = personne('majoration_redevance_domaniale', period)
        montant_base = personne('montant_base_redevance_domaniale_type_8', period)
        zone_occupation_redevance_domaniale = personne('zone_occupation_redevance_domaniale', period)
        activite_cultuelle = personne('activite_cultuelle', period)

        # Parameters
        base_calcul_jour = parameters(period).daf.redevance_domaniale.type_8[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].base_calcul_jour
        montant_minimum = parameters(period).daf.redevance_domaniale.type_8[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].montant_minimum

        # Price computation on the whole duration
        montant_intermediaire = max_(montant_base * duree_occupation_redevance_domaniale_jour / base_calcul_jour + majoration_redevance_domaniale, montant_minimum)

        # Price discount for religious activites
        montant_total = arrondiSup(montant_intermediaire * (1 - 0.8 * activite_cultuelle))
        return where(type_calcul == '8', montant_total, 0)
