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
from openfisca_pf.constants.time import NOMBRE_DE_JOURS_PAR_SEMAINE, NOMBRE_DE_JOURS_PAR_MOIS_AU_PRO_RATA_TEMPORIS, \
    NOMBRE_DE_JOURS_PAR_AN_AU_PRO_RATA_TEMPORIS
from openfisca_pf.constants.units import BOOLEAN, XPF
from openfisca_pf.entities import Personne
from openfisca_pf.enums.domaine import Temporalite
from openfisca_pf.functions.domaine import figer_emprise


class type_calcul_redevance_domaniale_est_type_8(Variable):
    entity = Personne
    definition_period = DAY
    value_type = bool
    default_value = False
    unit = BOOLEAN
    label = "Determine si le calcul de redevance domaniale est de type 8"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return personne('type_calcul_redevance_domaniale', period, parameters) == '8'


class montant_base_redevance_domaniale_type_8(Variable):
    entity = Personne
    definition_period = DAY
    value_type = float
    default_value = 0.
    unit = XPF
    label = "Montant de base de la redevance domaniale avec un zonage par archipel (journalier, annuel, mensuel)"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        # Variables
        type_calcul = personne('type_calcul_redevance_domaniale_est_type_8', period, parameters)
        emprise = personne('nature_emprise_occupation_redevance_domaniale', period, parameters)
        variable = personne('variable_redevance_domaniale', period, parameters)
        nombre = personne('nombre_unite_redevance_domaniale', period, parameters)
        zone = personne('zone_occupation_redevance_domaniale', period, parameters)

        # Lors de demandes multiples avec des types de calculs différents,
        # il est nécessaire de figer l'emprise sur une donnée existante pour le type associé.
        emprise = figer_emprise(
            type_calcul,
            emprise,
            'ag_priv_01_maraichage'
            )

        # Parameters
        part_fixe = parameters(period).daf.redevance_domaniale.type_8[emprise][zone].part_fixe
        part_unitaire = parameters(period).daf.redevance_domaniale.type_8[emprise][zone].part_unitaire
        part_variable = parameters(period).daf.redevance_domaniale.type_8[emprise][zone].part_variable
        montant_minimum = parameters(period).daf.redevance_domaniale.type_8[emprise][zone].montant_minimum

        # Price computation
        montant_intermediaire = part_fixe + part_unitaire * nombre + part_variable * variable

        # Minimum comparison
        montant_base = max_(arrondi_superrieur(montant_intermediaire), montant_minimum)
        return where(type_calcul, montant_base, 0.)


class montant_total_redevance_domaniale_type_8(Variable):
    entity = Personne
    definition_period = DAY
    value_type = float
    default_value = 0.
    unit = XPF
    label = "Montant total de la redevance domaniale avec un zonage par archipel"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        # Variables
        type_calcul = personne('type_calcul_redevance_domaniale_est_type_8', period)
        emprise = personne('nature_emprise_occupation_redevance_domaniale', period)
        duree = personne('duree_occupation_redevance_domaniale_jour', period)
        majoration = personne('majoration_redevance_domaniale', period)
        base = personne('montant_base_redevance_domaniale_type_8', period)
        zone = personne('zone_occupation_redevance_domaniale', period)
        exonere = personne('activite_cultuelle', period)

        # Lors de demandes multiples avec des types de calculs différents,
        # il est nécessaire de figer l'emprise sur une donnée existante pour le type associé.
        emprise = figer_emprise(
            type_calcul,
            emprise,
            'ag_priv_01_maraichage'
            )

        # Parametres
        exoneration = parameters(period).daf.redevance_domaniale.exoneration.discount_rate
        base_calcul_jour = parameters(period).daf.redevance_domaniale.type_8[emprise][zone].base_calcul_jour
        montant_minimum = parameters(period).daf.redevance_domaniale.type_8[emprise][zone].montant_minimum

        # Calcul du montant total
        montant_intermediaire = max_(base * duree / base_calcul_jour + majoration, montant_minimum)

        # Exoneration
        montant_total = arrondi_superrieur(montant_intermediaire * (1. - exoneration * exonere))
        return where(type_calcul, montant_total, 0.)


class temporalite_redevance_domaniale_type_8(Variable):
    value_type = Enum
    possible_values = Temporalite
    default_value = Temporalite.Non_Applicable
    entity = Personne
    definition_period = DAY
    label = "Temporalité (journalier, annuel, mensuel) pour la redevance domaniale"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        # Variables
        type_calcul = personne('type_calcul_redevance_domaniale_est_type_8', period, parameters)
        emprise = personne('nature_emprise_occupation_redevance_domaniale', period, parameters)
        zone = personne('zone_occupation_redevance_domaniale', period, parameters)

        # Lors de demandes multiples avec des types de calculs différents,
        # il est nécessaire de figer l'emprise sur une donnée existante pour le type associé.
        emprise = figer_emprise(
            type_calcul,
            emprise,
            'ag_priv_01_maraichage'
            )

        # Parametres
        base_calcul_jour = parameters(period).daf.redevance_domaniale.type_8[emprise][zone].base_calcul_jour

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
        return where(type_calcul, temporalite, Temporalite.Non_Applicable)
