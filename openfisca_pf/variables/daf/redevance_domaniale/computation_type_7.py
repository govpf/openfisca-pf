# -*- coding: utf-8 -*-

# This file defines the computation for extraction on the public domaiin. The computation is the same as type_2 with 5 areas defined (archipelagos dvision)
# but the computation is independent of the duration.k
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# # Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.variables.daf.redevance_domaniale.enums.enums import *
from openfisca_pf.base import *


class montant_base_redevance_domaniale_type_7(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de base (journalier, annuel, mensuel) de la redevance domaniale dûe avec un calcul dépendant de la zone géographique mais pas de la durée"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne, period, parameters):
        # Variables
        type_calcul = personne('type_calcul_redevance_domaniale', period)
        # Lors de demandes multiples avec des types de calculs différents, il est nécessaire de figer l'emprise sur une donnée existante pour le type associé.
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        nature_emprise_occupation_redevance_domaniale = where(type_calcul == '7', nature_emprise_occupation_redevance_domaniale.decode_to_str(), 'ex_eco_01_dpf_hors_entite_publique')
        variable_redevance_domaniale = personne('variable_redevance_domaniale', period)
        nombre_unite_redevance_domaniale = personne('nombre_unite_redevance_domaniale', period)
        zone_occupation_redevance_domaniale = personne('zone_occupation_redevance_domaniale', period)

        # Parameters
        part_fixe = parameters(period).daf.redevance_domaniale.type_7[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].part_fixe
        part_unitaire = parameters(period).daf.redevance_domaniale.type_7[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].part_unitaire
        part_variable = parameters(period).daf.redevance_domaniale.type_7[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].part_variable
        montant_minimum = parameters(period).daf.redevance_domaniale.type_7[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].montant_minimum

        # Price computation
        montant_intermediaire = part_fixe + part_unitaire * nombre_unite_redevance_domaniale + part_variable * variable_redevance_domaniale

        # Minimum comparison
        montant_base = max_(arrondiSup(montant_intermediaire), montant_minimum)
        return where(type_calcul == '7', montant_base, 0)


class montant_total_redevance_domaniale_type_7(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant total de la redevance domaniale dûe avec un calcul dépendant de la zone géographique mais pas de la durée"
    reference = "Arrêté NOR DAF2120267AC-3"
    unit = 'currency-XPF'

    def formula(personne, period, parameters):
        # Il n'y a pas de différence entre montant de basse et montant total pour ce type de calcul.

        return personne('montant_base_redevance_domaniale_type_7', period)


class temporalite_redevance_domaniale_type_7(Variable):
    value_type = Enum
    possible_values = Temporalite
    default_value = Temporalite.Non_Applicable
    entity = Personne
    definition_period = DAY
    label = "Temporalité (journalier, annuel, mensuel) pour la redevance domaniale dûe avec un calcul de type classique"
    reference = "Arrêté NOR DAF2120267AC-3"
