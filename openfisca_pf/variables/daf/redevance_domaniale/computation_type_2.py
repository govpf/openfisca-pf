# -*- coding: utf-8 -*-

# This file defines the computation for occupation on public domain that relies the same computation as type_1,
# but the parameters depends on the area.
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# # Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.variables.daf.redevance_domaniale.enums.enums import *
from openfisca_pf.base import *


class montant_base_redevance_domaniale_type_2(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de base (journalier, annuel, mensuel) de la redevance domaniale dûe avec un calcul dépendant de la zone géographique de la demande"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne, period, parameters):
        # Variables
        type_calcul = personne('type_calcul_redevance_domaniale', period)
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        # Lors de demandes multiples avec des types de calculs différents, il est nécessaire de figer l'emprise sur une donnée existante pour le type associé.
        nature_emprise_occupation_redevance_domaniale = where(type_calcul == '2', nature_emprise_occupation_redevance_domaniale.decode_to_str(), 'ip_eco_06_infra_restauration_aero')
        variable_redevance_domaniale = personne('variable_redevance_domaniale', period)
        nombre_unite_redevance_domaniale = personne('nombre_unite_redevance_domaniale', period)
        zone_occupation_redevance_domaniale = personne('zone_occupation_redevance_domaniale', period)

        # Parameters
        part_fixe = parameters(period).daf.redevance_domaniale.type_2[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].part_fixe
        part_unitaire = parameters(period).daf.redevance_domaniale.type_2[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].part_unitaire
        part_variable = parameters(period).daf.redevance_domaniale.type_2[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].part_variable
        montant_minimum = parameters(period).daf.redevance_domaniale.type_2[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].montant_minimum

        # Calcul du montant
        montant_intermediaire = part_fixe + part_unitaire * nombre_unite_redevance_domaniale + part_variable * variable_redevance_domaniale

        # Comparaison avec le minimum
        montant_base = max_(arrondiSup(montant_intermediaire), montant_minimum)
        return where(type_calcul == '2', montant_base, 0)


class montant_total_redevance_domaniale_type_2(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant total de la redevance domaniale dûe avec un calcul dépendant de la zone géographique de la demande"
    reference = "Arrêté NOR DAF2120267AC-3"
    unit = 'currency-XPF'

    def formula(personne, period, parameters):
        # Variables
        type_calcul = personne('type_calcul_redevance_domaniale', period)
        # Lors de demandes multiples avec des types de calculs différents, il est nécessaire de figer l'emprise sur une donnée existante pour le type associé.
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        nature_emprise_occupation_redevance_domaniale = where(type_calcul == '2', nature_emprise_occupation_redevance_domaniale.decode_to_str(), 'ip_eco_06_infra_restauration_aero')
        duree_occupation_redevance_domaniale_jour = personne('duree_occupation_redevance_domaniale_jour', period)
        majoration_redevance_domaniale = personne('majoration_redevance_domaniale', period)
        montant_base = personne('montant_base_redevance_domaniale_type_2', period)
        zone_occupation_redevance_domaniale = personne('zone_occupation_redevance_domaniale', period)
        activite_cultuelle = personne('activite_cultuelle', period)
        exoneration = parameters(period).daf.redevance_domaniale.exoneration.discount_rate

        # Parameters
        base_calcul_jour = parameters(period).daf.redevance_domaniale.type_2[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].base_calcul_jour
        montant_minimum = parameters(period).daf.redevance_domaniale.type_2[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].montant_minimum

        # Calcul du montant sur la durée totale
        montant_intermediaire = max_(montant_base * duree_occupation_redevance_domaniale_jour / base_calcul_jour + majoration_redevance_domaniale, montant_minimum)

        # Exonération pour certaines activités
        montant_total = arrondiSup(montant_intermediaire * (1 - exoneration * activite_cultuelle))
        return where(type_calcul == '2', montant_total, 0)


class temporalite_redevance_domaniale_type_2(Variable):
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
        nature_emprise_occupation_redevance_domaniale = where(type_calcul == '2', nature_emprise_occupation_redevance_domaniale.decode_to_str(), 'ip_eco_06_infra_restauration_aero')
        zone_occupation_redevance_domaniale = personne('zone_occupation_redevance_domaniale', period)
        # Parameters
        base_calcul_jour = parameters(period).daf.redevance_domaniale.type_2[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].base_calcul_jour
        # Constantes
        nombre_jour_par_an = parameters(period).daf.redevance_domaniale.constantes.nombre_jour_par_an_rd
        nombre_jour_par_mois = parameters(period).daf.redevance_domaniale.constantes.nombre_jour_par_mois_rd
        nombre_jour_par_semaine = parameters(period).daf.redevance_domaniale.constantes.nombre_jour_par_semaine_rd
        # Transformation
        temporalite = select([
            base_calcul_jour == 1,
            base_calcul_jour == nombre_jour_par_semaine,
            base_calcul_jour == nombre_jour_par_mois,
            base_calcul_jour == nombre_jour_par_an
            ], [
                Temporalite.Journalier,
                Temporalite.Hebdomadaire,
                Temporalite.Mensuel,
                Temporalite.Annuel
                ])

        return where(type_calcul == '2', temporalite, Temporalite.Non_Applicable)
