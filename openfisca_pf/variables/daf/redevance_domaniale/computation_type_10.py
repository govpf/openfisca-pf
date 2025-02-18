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
from openfisca_pf.functions.domaine import figer_emprise, indexer_zone_commune


class type_calcul_redevance_domaniale_est_type_10(Variable):
    entity = Personne
    definition_period = DAY
    value_type = bool
    default_value = False
    unit = BOOLEAN
    label = "Determine si le calcul de redevance domaniale est de type 10"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return personne('type_calcul_redevance_domaniale', period, parameters) == '10'


class montant_base_redevance_domaniale_type_10(Variable):
    entity = Personne
    definition_period = DAY
    value_type = float
    default_value = 0.
    unit = XPF
    label = "Montant annuel de la redevance domaniale sur les lotissements agricoles"
    reference = "Arrêté NOR DAF1620009AC-1"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        # Variables
        type_calcul_est_10 = personne('type_calcul_redevance_domaniale_est_type_10', period, parameters)
        emprise = personne('nature_emprise_occupation_redevance_domaniale', period, parameters)
        variable = personne('variable_redevance_domaniale', period, parameters)
        commune = personne('commune_redevance_domaniale', period, parameters)
        zone = personne('zone_lot_agricole', period, parameters)

        # Lors de demandes multiples avec des types de calculs différents,
        # il est nécessaire de figer l'emprise sur une donnée existante pour le type associé.
        emprise = figer_emprise(
            type_calcul_est_10,
            emprise,
            'ag_priv_06_lot_agricole'
            )

        # Parametres
        montant_minimum = parameters(period).daf.redevance_domaniale.type_10[emprise].montant_minimum
        part_variable = parameters(period).daf.redevance_domaniale.type_10[emprise].part_variable
        loyer = indexer_zone_commune(
            parameters(period).daf.redevance_domaniale.lot_agricole,
            commune,
            zone,
            'loyer'
            )

        # Calcul du montant
        montant_intermediaire = arrondi_superrieur(part_variable / 100. * loyer * variable)
        montant_base = max_(montant_intermediaire, montant_minimum)
        return where(type_calcul_est_10, montant_base, 0.)


class montant_total_redevance_domaniale_type_10(Variable):
    entity = Personne
    definition_period = DAY
    value_type = float
    default_value = 0.
    unit = XPF
    label = "Montant total de la redevance domaniale dûe sur les lotissements agricoles"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        # Variables
        type_calcul_est_10 = personne('type_calcul_redevance_domaniale_est_type_10', period, parameters)
        emprise = personne('nature_emprise_occupation_redevance_domaniale', period, parameters)
        duree = personne('duree_occupation_redevance_domaniale_jour', period, parameters)
        base = personne('montant_base_redevance_domaniale_type_10', period, parameters)

        # Lors de demandes multiples avec des types de calculs différents,
        # il est nécessaire de figer l'emprise sur une donnée existante pour le type associé.
        emprise = figer_emprise(
            type_calcul_est_10,
            emprise,
            'ag_priv_06_lot_agricole'
            )

        # Parametres
        base_calcul_jour = parameters(period).daf.redevance_domaniale.type_10[emprise].base_calcul_jour
        montant_minimum = parameters(period).daf.redevance_domaniale.type_10[emprise].montant_minimum

        # Calcul
        montant = arrondi_superrieur(max_(base * duree / base_calcul_jour, montant_minimum))
        return where(type_calcul_est_10, montant, 0.)


class temporalite_redevance_domaniale_type_10(Variable):
    entity = Personne
    definition_period = DAY
    value_type = Enum
    possible_values = Temporalite
    default_value = Temporalite.Non_Applicable
    label = "Temporalité (journalier, annuel, mensuel) pour la redevance domaniale"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        # Variables
        type_calcul_est_10 = personne('type_calcul_redevance_domaniale_est_type_10', period, parameters)
        emprise = personne('nature_emprise_occupation_redevance_domaniale', period, parameters)

        # Lors de demandes multiples avec des types de calculs différents,
        # il est nécessaire de figer l'emprise sur une donnée existante pour le type associé.
        emprise = figer_emprise(
            type_calcul_est_10,
            emprise,
            'ag_priv_06_lot_agricole'
            )

        # Parameters
        base_calcul_jour = parameters(period).daf.redevance_domaniale.type_10[emprise].base_calcul_jour

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
        return where(type_calcul_est_10, temporalite, Temporalite.Non_Applicable)
