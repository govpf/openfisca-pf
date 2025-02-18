# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
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
from openfisca_pf.functions.currency import arrondi_superieur
from openfisca_pf.functions.domaine import figer_emprise, indexer_zone_commune


class type_calcul_redevance_domaniale_est_type_9(Variable):
    entity = Personne
    definition_period = DAY
    value_type = bool
    default_value = False
    unit = BOOLEAN
    label = "Determine si le calcul de redevance domaniale est de type 9"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return personne('type_calcul_redevance_domaniale', period, parameters) == '9'


class montant_base_redevance_domaniale_type_9(Variable):
    entity = Personne
    definition_period = DAY
    value_type = float
    default_value = 0.
    unit = XPF
    label = "Montant de base (journalier, annuel, mensuel) de la redevance domaniale sur le domaine privé"
    reference = "Arrêté NOR DAF1620009AC-1"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        # Variables
        type_calcul = personne('type_calcul_redevance_domaniale_est_type_9', period, parameters)
        emprise = personne('nature_emprise_occupation_redevance_domaniale', period, parameters)
        variable = personne('variable_redevance_domaniale', period, parameters)
        commune = personne('commune_redevance_domaniale', period, parameters)
        zone = personne('zone_domaine_prive', period, parameters)

        # Lors de demandes multiples avec des types de calculs différents,
        # il est nécessaire de figer l'emprise sur une donnée existante pour le type associé.
        emprise = figer_emprise(
            type_calcul,
            emprise,
            'priv_09_autres'
            )

        # Parametres
        montant_minimum = parameters(period).daf.redevance_domaniale.type_9[emprise].montant_minimum
        part_variable = parameters(period).daf.redevance_domaniale.type_9[emprise].part_variable
        valeur_venale = indexer_zone_commune(
            parameters(period).daf.redevance_domaniale.commune_prive,
            commune,
            zone,
            'valeur_venale'
            )

        # Calcul du montant
        montant_intermediaire = arrondi_superieur(part_variable / 100. * valeur_venale * variable)
        montant_base = max_(montant_intermediaire, montant_minimum)
        return where(type_calcul, montant_base, 0.)


class montant_total_redevance_domaniale_type_9(Variable):
    entity = Personne
    definition_period = DAY
    value_type = float
    default_value = 0.
    unit = XPF
    label = "Montant total de la redevance domaniale dûe sur le domaine privé"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        # Variables
        type_calcul = personne('type_calcul_redevance_domaniale_est_type_9', period, parameters)
        emprise = personne('nature_emprise_occupation_redevance_domaniale', period, parameters)
        duree = personne('duree_occupation_redevance_domaniale_jour', period, parameters)
        base = personne('montant_base_redevance_domaniale_type_9', period, parameters)

        # Lors de demandes multiples avec des types de calculs différents,
        # il est nécessaire de figer l'emprise sur une donnée existante pour le type associé.
        emprise = figer_emprise(
            type_calcul,
            emprise,
            'priv_09_autres'
            )

        # Parameters
        base_calcul_jour = parameters(period).daf.redevance_domaniale.type_9[emprise].base_calcul_jour
        montant_minimum = parameters(period).daf.redevance_domaniale.type_9[emprise].montant_minimum

        # Calcul du montant total
        montant_intermediaire = max_(base * duree / base_calcul_jour, montant_minimum)
        montant_total = arrondi_superieur(montant_intermediaire)
        return where(type_calcul, montant_total, 0.)


class temporalite_redevance_domaniale_type_9(Variable):
    entity = Personne
    definition_period = DAY
    value_type = Enum
    possible_values = Temporalite
    default_value = Temporalite.Non_Applicable
    label = "Temporalité (journalier, annuel, mensuel) pour la redevance domaniale"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        # Variables
        type_calcul = personne('type_calcul_redevance_domaniale_est_type_9', period, parameters)
        emprise = personne('nature_emprise_occupation_redevance_domaniale', period, parameters)

        # Lors de demandes multiples avec des types de calculs différents,
        # il est nécessaire de figer l'emprise sur une donnée existante pour le type associé.
        emprise = figer_emprise(
            type_calcul,
            emprise,
            'priv_09_autres'
            )

        # Parametres
        base_calcul_jour = parameters(period).daf.redevance_domaniale.type_9[emprise].base_calcul_jour

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
