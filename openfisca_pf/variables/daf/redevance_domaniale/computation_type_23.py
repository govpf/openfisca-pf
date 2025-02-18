# -*- coding: utf-8 -*-

from openfisca_pf.base import (
    ArrayLike,
    arrondi_superrieur,
    DAY,
    Enum,
    min_,
    Parameters,
    Period,
    select,
    Variable,
    where
    )
from openfisca_pf.constants.time import NOMBRE_D_HEURES_PAR_DEMI_JOURNEE_AU_PRO_RATA_TEMPORIS
from openfisca_pf.constants.units import BOOLEAN, XPF
from openfisca_pf.entities import Personne
from openfisca_pf.enums.domaine import Temporalite
from openfisca_pf.functions.domaine import figer_emprise


class type_calcul_redevance_domaniale_est_type_23(Variable):
    entity = Personne
    definition_period = DAY
    value_type = bool
    default_value = False
    unit = BOOLEAN
    label = "Determine si le calcul de redevance domaniale est de type 23"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return personne('type_calcul_redevance_domaniale', period, parameters) == '23'


class montant_base_redevance_domaniale_type_23(Variable):
    entity = Personne
    definition_period = DAY
    value_type = float
    default_value = 0.
    unit = XPF
    label = "Montant de la redevance domaniale dûe pour les occupations de moins d'une journée"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        # Il n'y a pas de différence entre montant de basse et montant total pour ce type de calcul.
        return personne('montant_total_redevance_domaniale_type_23', period, parameters)


class montant_total_redevance_domaniale_type_23(Variable):
    entity = Personne
    definition_period = DAY
    value_type = float
    default_value = 0.
    unit = XPF
    label = "Montant de la redevance domaniale dûe pour les occupations de moins d'une journée"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        # Variables
        type_calcul_est_23 = personne('type_calcul_redevance_domaniale_est_type_23', period, parameters)
        emprise = personne('nature_emprise_occupation_redevance_domaniale', period, parameters)
        duree = personne('duree_occupation_redevance_domaniale', period, parameters)
        majoration = personne('majoration_redevance_domaniale', period, parameters)

        # Lors de demandes multiples avec des types de calculs différents,
        # il est nécessaire de figer l'emprise sur une donnée existante pour le type associé.
        emprise = figer_emprise(
            type_calcul_est_23,
            emprise,
            'em_eco_01_espace_pelouse_ac_elec'
            )

        # Parameters
        tarif_horaire = parameters(period).daf.redevance_domaniale.type_23[emprise].tarif_horaire
        tarif_demi_jour = parameters(period).daf.redevance_domaniale.type_23[emprise].tarif_demi_jour
        tarif_jour = parameters(period).daf.redevance_domaniale.type_23[emprise].tarif_jour

        # Price computation
        montant_intermediaire = select(
            [
                duree <= NOMBRE_D_HEURES_PAR_DEMI_JOURNEE_AU_PRO_RATA_TEMPORIS,
                duree > NOMBRE_D_HEURES_PAR_DEMI_JOURNEE_AU_PRO_RATA_TEMPORIS
                ],
            [
                min_(tarif_horaire * duree, tarif_demi_jour),
                min_(tarif_demi_jour + tarif_horaire * (duree - NOMBRE_D_HEURES_PAR_DEMI_JOURNEE_AU_PRO_RATA_TEMPORIS), tarif_jour)
                ]
            )
        montant_total = arrondi_superrieur(montant_intermediaire) + majoration
        return where(type_calcul_est_23, montant_total, 0.)


class temporalite_redevance_domaniale_type_23(Variable):
    value_type = Enum
    possible_values = Temporalite
    default_value = Temporalite.Non_Applicable
    entity = Personne
    definition_period = DAY
    label = "Temporalité (journalier, annuel, mensuel) pour la redevance domaniale"
    reference = "Arrêté NOR DAF2120267AC-3"
