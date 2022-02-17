# -*- coding: utf-8 -*-

# This file defines the computation for occupation on public domain that relies on the surface with a ratinf that evolve with the surface.
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# # Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.variables.daf.redevance_domaniale.Enums.enums import *
from openfisca_pf.base import *


class montant_base_redevance_domaniale_type_5(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de base (journalier, mensuel, annuel) de la redevance domaniale dûe avec un calcul dont le montant annuel évolue par palier de surface"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne, period, parameters):
        # Variables
        type_calcul = personne('type_calcul_redevance_domaniale', period)
        # Lors de demandes multiples avec des types de calculs différents, il est nécessaire de figer l'emprise sur une donnée existante pour le type associé.
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        nature_emprise_occupation_redevance_domaniale = where(type_calcul == '5', nature_emprise_occupation_redevance_domaniale.decode_to_str(), 'if_eco_01_parc_poisson_hors_passe')
        variable_redevance_domaniale = personne('variable_redevance_domaniale', period)

        # Parametres
        init = parameters(period).daf.redevance_domaniale.type_5[nature_emprise_occupation_redevance_domaniale].init
        rate_0 = parameters(period).daf.redevance_domaniale.type_5[nature_emprise_occupation_redevance_domaniale].rate_0
        threshold_1 = parameters(period).daf.redevance_domaniale.type_5[nature_emprise_occupation_redevance_domaniale].threshold_1
        rate_1 = parameters(period).daf.redevance_domaniale.type_5[nature_emprise_occupation_redevance_domaniale].rate_1
        threshold_2 = parameters(period).daf.redevance_domaniale.type_5[nature_emprise_occupation_redevance_domaniale].threshold_2
        rate_2 = parameters(period).daf.redevance_domaniale.type_5[nature_emprise_occupation_redevance_domaniale].rate_2

        montant_minimum = parameters(period).daf.redevance_domaniale.type_5[nature_emprise_occupation_redevance_domaniale].montant_minimum

        # Calcul du montant
        montant_intermediaire = select([
            variable_redevance_domaniale < threshold_1,
            variable_redevance_domaniale <= threshold_2,
            variable_redevance_domaniale > threshold_2
            ], [
                init + rate_0 * variable_redevance_domaniale,
                init + rate_0 * threshold_1 + rate_1 * (variable_redevance_domaniale - threshold_1),
                init + rate_0 * threshold_1 + rate_1 * (threshold_2 - threshold_1) + rate_2 * (variable_redevance_domaniale - threshold_2)
                ])

        montant_base = max_(arrondiSup(montant_intermediaire), montant_minimum)

        return where(type_calcul == '5', montant_base, 0)


class montant_total_redevance_domaniale_type_5(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de total de la redevance domaniale dûe avec un calcul dont le montant annuel évolue par palier de surface"
    reference = "Arrêté NOR DAF2120267AC-3"
    unit = 'currency-XPF'

    def formula(personne, period, parameters):
        # Variables
        type_calcul = personne('type_calcul_redevance_domaniale', period)
        # Lors de demandes multiples avec des types de calculs différents, il est nécessaire de figer l'emprise sur une donnée existante pour le type associé.
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        nature_emprise_occupation_redevance_domaniale = where(type_calcul == '5', nature_emprise_occupation_redevance_domaniale.decode_to_str(), 'if_eco_01_parc_poisson_hors_passe')
        duree_occupation_redevance_domaniale_jour = personne('duree_occupation_redevance_domaniale_jour', period)
        majoration_redevance_domaniale = personne('majoration_redevance_domaniale', period)
        montant_base = personne('montant_base_redevance_domaniale_type_5', period)

        # Parametres
        base_calcul_jour = parameters(period).daf.redevance_domaniale.type_5[nature_emprise_occupation_redevance_domaniale].base_calcul_jour
        montant_minimum = parameters(period).daf.redevance_domaniale.type_5[nature_emprise_occupation_redevance_domaniale].montant_minimum

        # Calcul du montant pour la durée totale
        montant_total = max_(arrondiSup(montant_base * duree_occupation_redevance_domaniale_jour / base_calcul_jour), montant_minimum) + majoration_redevance_domaniale
        # La comparaison avec le minmum est effectué sur le montant de base et le montant totale pour correctement calculer pour des durées inférieures à la durée de base

        return where(type_calcul == '5', montant_total, 0)


class temporalite_redevance_domaniale_type_5(Variable):
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
        nature_emprise_occupation_redevance_domaniale = where(type_calcul == '5', nature_emprise_occupation_redevance_domaniale.decode_to_str(), 'if_eco_01_parc_poisson_hors_passe')
        # Parametres
        base_calcul_jour = parameters(period).daf.redevance_domaniale.type_5[nature_emprise_occupation_redevance_domaniale].base_calcul_jour

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

        return where(type_calcul == '5', temporalite, Temporalite.Non_Applicable)
