# -*- coding: utf-8 -*-

# This file defines the computation for occupation on public domain that relies the same computation as type_2,
# but the zoning is divided in 5 areas iinstead of 4.
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# # Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.variables.daf.redevance_domaniale.Enums.enums import *
from openfisca_pf.base import *


class montant_base_redevance_domaniale_type_8(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de base (journalier, annuel, mensuel) de la redevance domaniale avec un zonage par archipel"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne, period, parameters):
        # Variables
        type_calcul = personne('type_calcul_redevance_domaniale', period)
        # Lors de demandes multiples avec des types de calculs différents, il est nécessaire de figer l'emprise sur une donnée existante pour le type associé.
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        nature_emprise_occupation_redevance_domaniale = where(type_calcul == '8', nature_emprise_occupation_redevance_domaniale.decode_to_str(), 'ag_priv_01_maraichage')
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
    label = "Montant total de la redevance domaniale avec un zonage par archipel"
    reference = "Arrêté NOR DAF2120267AC-3"
    unit = 'currency-XPF'

    def formula(personne, period, parameters):
        # Variables
        type_calcul = personne('type_calcul_redevance_domaniale', period)
        # Lors de demandes multiples avec des types de calculs différents, il est nécessaire de figer l'emprise sur une donnée existante pour le type associé.
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        nature_emprise_occupation_redevance_domaniale = where(type_calcul == '8', nature_emprise_occupation_redevance_domaniale.decode_to_str(), 'ag_priv_01_maraichage')
        duree_occupation_redevance_domaniale_jour = personne('duree_occupation_redevance_domaniale_jour', period)
        majoration_redevance_domaniale = personne('majoration_redevance_domaniale', period)
        montant_base = personne('montant_base_redevance_domaniale_type_8', period)
        zone_occupation_redevance_domaniale = personne('zone_occupation_redevance_domaniale', period)
        activite_cultuelle = personne('activite_cultuelle', period)

        # Parametres
        base_calcul_jour = parameters(period).daf.redevance_domaniale.type_8[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].base_calcul_jour
        montant_minimum = parameters(period).daf.redevance_domaniale.type_8[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].montant_minimum

        # Calcul du montant total
        montant_intermediaire = max_(montant_base * duree_occupation_redevance_domaniale_jour / base_calcul_jour + majoration_redevance_domaniale, montant_minimum)

        # Exoneration
        montant_total = arrondiSup(montant_intermediaire * (1 - 0.8 * activite_cultuelle))
        return where(type_calcul == '8', montant_total, 0)


class temporalite_redevance_domaniale_type_8(Variable):
    value_type = Enum
    possible_values = Temporalite
    default_value = Temporalite.Non_Applicable
    entity = Personne
    definition_period = DAY
    label = "Temporalité (journalier, annuel, mensuel) pour la redevance domaniale"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne, period, parameters):
        # Variables
        type_calcul = personne('type_calcul_redevance_domaniale', period)
        # Lors de demandes multiples avec des types de calculs différents, il est nécessaire de figer l'emprise sur une donnée existante pour le type associé.
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        nature_emprise_occupation_redevance_domaniale = where(type_calcul == '8', nature_emprise_occupation_redevance_domaniale.decode_to_str(), 'ag_priv_01_maraichage')
        zone_occupation_redevance_domaniale = personne('zone_occupation_redevance_domaniale', period)
        # Parametres
        base_calcul_jour = parameters(period).daf.redevance_domaniale.type_8[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].base_calcul_jour

        # Transformation
        temporalite = select([
            base_calcul_jour == 1,
            base_calcul_jour == 7,
            base_calcul_jour == 30,
            base_calcul_jour == 360
            ], [
                Temporalite.Journalier,
                Temporalite.Hebdomadaire,
                Temporalite.Mensuel,
                Temporalite.Annuel
                ])

        return where(type_calcul == '8', temporalite, Temporalite.Non_Applicable)
