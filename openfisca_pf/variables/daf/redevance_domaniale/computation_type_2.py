# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    DAY,
    Enum,
    full,
    max_,
    ParameterNode,
    Period,
    Population,
    select,
    Variable,
    where
    )
from openfisca_pf.constants.time import (
    NOMBRE_DE_JOURS_PAR_SEMAINE,
    NOMBRE_DE_JOURS_PAR_MOIS_AU_PRO_RATA_TEMPORIS,
    NOMBRE_DE_JOURS_PAR_AN_AU_PRO_RATA_TEMPORIS
    )
from openfisca_pf.constants.units import XPF, BOOLEAN
from openfisca_pf.entities import Personne
from openfisca_pf.enums.domaine import Temporalite
from openfisca_pf.functions.currency import arrondi_superieur
from openfisca_pf.functions.domaine import figer_emprise


class type_calcul_redevance_domaniale_est_type_2(Variable):
    entity = Personne
    definition_period = DAY
    value_type = bool
    default_value = False
    unit = BOOLEAN
    label = "Determine si le calcul de redevance domaniale est de type 2"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return personne('type_calcul_redevance_domaniale', period) == '2'


class montant_base_redevance_domaniale_type_2(Variable):
    entity = Personne
    definition_period = DAY
    value_type = float
    default_value = 0.
    unit = XPF
    label = "Montant de base de la redevance domaniale dûe avec un calcul dépendant de la zone géographique de la demande (journalier, annuel, mensuel)"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        # Variables
        type_calcul_est_2 = personne('type_calcul_redevance_domaniale_est_type_2', period)
        emprise = personne('nature_emprise_occupation_redevance_domaniale', period)
        variable = personne('variable_redevance_domaniale', period)
        nombre_unite = personne('nombre_unite_redevance_domaniale', period)
        zone = personne('zone_occupation_redevance_domaniale', period)

        # Lors de demandes multiples avec des types de calculs différents,
        # il est nécessaire de figer l'emprise sur une donnée existante pour le type associé.
        emprise = figer_emprise(
            type_calcul_est_2,
            emprise,
            'ip_eco_06_infra_restauration_aero'
            )

        # Parameters
        part_fixe = parameters(period).daf.redevance_domaniale.type_2[emprise][zone].part_fixe
        part_unitaire = parameters(period).daf.redevance_domaniale.type_2[emprise][zone].part_unitaire
        part_variable = parameters(period).daf.redevance_domaniale.type_2[emprise][zone].part_variable
        montant_minimum = parameters(period).daf.redevance_domaniale.type_2[emprise][zone].montant_minimum

        # Calcul du montant
        montant_intermediaire = part_fixe + (part_unitaire * nombre_unite) + (part_variable * variable)

        # Comparaison avec le minimum
        montant_base = max_(
            arrondi_superieur(montant_intermediaire),
            montant_minimum
            )
        return where(type_calcul_est_2, montant_base, 0.)


class montant_total_redevance_domaniale_type_2(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    default_value = 0.
    unit = XPF
    label = "Montant total de la redevance domaniale dûe avec un calcul dépendant de la zone géographique de la demande"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        # Variables
        type_calcul_est_2 = personne('type_calcul_redevance_domaniale_est_type_2', period)
        emprise = personne('nature_emprise_occupation_redevance_domaniale', period)
        duree_occupation = personne('duree_occupation_redevance_domaniale_jour', period)
        majoration = personne('majoration_redevance_domaniale', period)
        montant = personne('montant_base_redevance_domaniale_type_2', period)
        zone = personne('zone_occupation_redevance_domaniale', period)
        activite_cultuelle = personne('activite_cultuelle', period)

        # Lors de demandes multiples avec des types de calculs différents,
        # il est nécessaire de figer l'emprise sur une donnée existante pour le type associé.
        emprise = figer_emprise(
            type_calcul_est_2,
            emprise,
            'ip_eco_06_infra_restauration_aero'
            )

        # Parameters
        exoneration = parameters(period).daf.redevance_domaniale.exoneration.discount_rate
        base_calcul_jour = parameters(period).daf.redevance_domaniale.type_2[emprise][zone].base_calcul_jour
        montant_minimum = parameters(period).daf.redevance_domaniale.type_2[emprise][zone].montant_minimum

        # Calcul du montant sur la durée totale
        montant_intermediaire = max_(montant * duree_occupation / base_calcul_jour + majoration, montant_minimum)

        # Exonération pour certaines activités
        montant_total = arrondi_superieur(montant_intermediaire * (1. - exoneration * activite_cultuelle))
        return where(type_calcul_est_2, montant_total, 0.)


class temporalite_redevance_domaniale_type_2(Variable):
    value_type = Enum
    possible_values = Temporalite
    default_value = Temporalite.Non_Applicable
    entity = Personne
    definition_period = DAY
    label = "Temporalité (journalier, annuel, mensuel) pour la redevance domaniale"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        # Variables
        type_calcul_est_2 = personne('type_calcul_redevance_domaniale_est_type_2', period)
        emprise = personne('nature_emprise_occupation_redevance_domaniale', period)
        zone = personne('zone_occupation_redevance_domaniale', period)

        # Lors de demandes multiples avec des types de calculs différents,
        # il est nécessaire de figer l'emprise sur une donnée existante pour le type associé.
        emprise = figer_emprise(
            type_calcul_est_2,
            emprise,
            'ip_eco_06_infra_restauration_aero'
            )

        # Parameters
        base_calcul_jour = parameters(period).daf.redevance_domaniale.type_2[emprise][zone].base_calcul_jour

        # Transformation
        temporalite = select(
            [
                base_calcul_jour == 1,
                base_calcul_jour == NOMBRE_DE_JOURS_PAR_SEMAINE,
                base_calcul_jour == NOMBRE_DE_JOURS_PAR_MOIS_AU_PRO_RATA_TEMPORIS,
                base_calcul_jour == NOMBRE_DE_JOURS_PAR_AN_AU_PRO_RATA_TEMPORIS
                ],
            [
                full(personne.count, Temporalite.Journalier),
                full(personne.count, Temporalite.Hebdomadaire),
                full(personne.count, Temporalite.Mensuel),
                full(personne.count, Temporalite.Annuel)
                ]
            )
        return where(
            type_calcul_est_2,
            temporalite,
            full(personne.count, Temporalite.Non_Applicable)
            )
