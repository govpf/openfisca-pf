# -*- coding: utf-8 -*-

from openfisca_pf.base import (
    ArrayLike,
    arrondi_superrieur,
    DAY,
    Enum,
    max_,
    Parameters,
    Period,
    select,
    Variable,
    where
    )
from openfisca_pf.constants.time import (
    NOMBRE_DE_JOURS_PAR_SEMAINE,
    NOMBRE_DE_JOURS_PAR_MOIS_AU_PRO_RATA_TEMPORIS,
    NOMBRE_DE_JOURS_PAR_AN_AU_PRO_RATA_TEMPORIS
    )
from openfisca_pf.constants.units import BOOLEAN, XPF
from openfisca_pf.entities import Personne
from openfisca_pf.enums.domaine import Temporalite
from openfisca_pf.functions.domaine import figer_emprise


class type_calcul_redevance_domaniale_est_type_1(Variable):
    entity = Personne
    definition_period = DAY
    value_type = bool
    default_value = False
    unit = BOOLEAN
    label = "Determine si le calcul de redevance domaniale est de type 1"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return personne('type_calcul_redevance_domaniale', period, parameters) == '1'


class montant_base_redevance_domaniale_type_1(Variable):
    entity = Personne
    definition_period = DAY
    value_type = float
    default_value = 0.
    unit = XPF
    label = "Montant de base pour la redevance domaniale dûe avec un calcul dit de type classique"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        # Variables
        type_calcul_est_1 = personne('type_calcul_redevance_domaniale_est_type_1', period, parameters)
        emprise = personne('nature_emprise_occupation_redevance_domaniale', period, parameters)
        variable_redevance_domaniale = personne('variable_redevance_domaniale', period, parameters)
        nombre_unite_redevance_domaniale = personne('nombre_unite_redevance_domaniale', period, parameters)

        # Lors de demandes multiples avec des types de calculs différents,
        # il est nécessaire de figer l'emprise sur une donnée existante pour le type associé.
        emprise = figer_emprise(
            type_calcul_est_1,
            emprise,
            'ip_eco_01_equipement_pays'
            )

        # Parametres
        part_fixe = parameters(period).daf.redevance_domaniale.type_1[emprise].part_fixe
        part_unitaire = parameters(period).daf.redevance_domaniale.type_1[emprise].part_unitaire
        part_variable = parameters(period).daf.redevance_domaniale.type_1[emprise].part_variable
        montant_minimum = parameters(period).daf.redevance_domaniale.type_1[emprise].montant_minimum

        # Calcul du montant
        montant_intermediaire = part_fixe + (part_unitaire * nombre_unite_redevance_domaniale) + (part_variable * variable_redevance_domaniale)

        # Comparaison avec le minimum
        montant_base = max_(
            arrondi_superrieur(montant_intermediaire),
            montant_minimum
            )
        return where(type_calcul_est_1, montant_base, 0.)


class montant_total_redevance_domaniale_type_1(Variable):
    entity = Personne
    definition_period = DAY
    value_type = float
    default_value = 0.
    unit = XPF
    label = "Montant total de la redevance domaniale dûe avec un calcul de type classique"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        # Variables
        type_calcul_est_1 = personne('type_calcul_redevance_domaniale_est_type_1', period, parameters)
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period, parameters)
        duree_occupation_redevance_domaniale_jour = personne('duree_occupation_redevance_domaniale_jour', period, parameters)
        majoration_redevance_domaniale = personne('majoration_redevance_domaniale', period, parameters)
        montant_base = personne('montant_base_redevance_domaniale_type_1', period, parameters)
        activite_cultuelle = personne('activite_cultuelle', period, parameters)

        # Lors de demandes multiples avec des types de calculs différents,
        # il est nécessaire de figer l'emprise sur une donnée existante pour le type associé.
        nature_emprise_occupation_redevance_domaniale = figer_emprise(
            type_calcul_est_1,
            nature_emprise_occupation_redevance_domaniale,
            'ip_eco_01_equipement_pays'
            )

        # Parameters
        exoneration = parameters(period).daf.redevance_domaniale.exoneration.discount_rate
        base_calcul_jour = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale].base_calcul_jour
        montant_minimum = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale].montant_minimum

        # Calcul du montant
        montant_intermediaire = max_(
            montant_base * duree_occupation_redevance_domaniale_jour / base_calcul_jour + majoration_redevance_domaniale,
            montant_minimum
            )
        montant_total = arrondi_superrieur(montant_intermediaire * (1. - exoneration * activite_cultuelle))

        return where(type_calcul_est_1, montant_total, 0.)


class temporalite_redevance_domaniale_type_1(Variable):
    entity = Personne
    definition_period = DAY
    value_type = Enum
    possible_values = Temporalite
    default_value = Temporalite.Non_Applicable
    label = "Temporalité pour la redevance domaniale (journalier, annuel, mensuel)"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        # Variables
        type_calcul_est_1 = personne('type_calcul_redevance_domaniale_est_type_1', period, parameters)
        emprise = personne('nature_emprise_occupation_redevance_domaniale', period, parameters)

        # Lors de demandes multiples avec des types de calculs différents,
        # il est nécessaire de figer l'emprise sur une donnée existante pour le type associé.
        emprise = figer_emprise(
            type_calcul_est_1,
            emprise,
            'ip_eco_01_equipement_pays'
            )

        # Parameters
        base_calcul_jour = parameters(period).daf.redevance_domaniale.type_1[emprise].base_calcul_jour

        # Transformation
        temporalite = select(
            [
                base_calcul_jour == 1,
                base_calcul_jour == NOMBRE_DE_JOURS_PAR_SEMAINE,
                base_calcul_jour == NOMBRE_DE_JOURS_PAR_MOIS_AU_PRO_RATA_TEMPORIS,
                base_calcul_jour == NOMBRE_DE_JOURS_PAR_AN_AU_PRO_RATA_TEMPORIS
                ],
            [
                Temporalite.Journalier,
                Temporalite.Hebdomadaire,
                Temporalite.Mensuel,
                Temporalite.Annuel
                ]
            )
        return where(type_calcul_est_1, temporalite, Temporalite.Non_Applicable)
