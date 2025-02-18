# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    DAY,
    Enum,
    Parameters,
    Period,
    select,
    Variable,
    where
    )
from openfisca_pf.constants.units import XPF, BOOLEAN
from openfisca_pf.entities import Personne
from openfisca_pf.enums.domaine import Temporalite
from openfisca_pf.functions.currency import arrondi_superieur
from openfisca_pf.functions.domaine import figer_emprise


class type_calcul_redevance_domaniale_est_type_3(Variable):
    entity = Personne
    definition_period = DAY
    value_type = bool
    default_value = False
    unit = BOOLEAN
    label = "Determine si le calcul de redevance domaniale est de type 3"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return personne('type_calcul_redevance_domaniale', period, parameters) == '3'


class montant_base_redevance_domaniale_type_3(Variable):
    value_type = str
    entity = Personne
    definition_period = DAY
    label = "Montant de la redevance domaniale dûe avec un calcul dont le taux journalier évolue par palier"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        # Il n'y a pas de différence entre montant de basse et montant total pour ce type de calcul.
        return personne('montant_total_redevance_domaniale_type_3', period, parameters)


class montant_total_redevance_domaniale_type_3(Variable):
    entity = Personne
    definition_period = DAY
    value_type = float
    default_value = 0.
    unit = XPF
    label = "Montant de la redevance domaniale dûe avec un calcul dont le taux journalier évolue par palier"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        # Variables
        type_calcul_est_3 = personne('type_calcul_redevance_domaniale_est_type_3', period, parameters)
        emprise = personne('nature_emprise_occupation_redevance_domaniale', period, parameters)
        duree = personne('duree_occupation_redevance_domaniale_jour', period, parameters)
        majoration = personne('majoration_redevance_domaniale', period, parameters)
        activite_cultuelle = personne('activite_cultuelle', period, parameters)

        # Lors de demandes multiples avec des types de calculs différents,
        # il est nécessaire de figer l'emprise sur une donnée existante pour le type associé.
        emprise = figer_emprise(
            type_calcul_est_3,
            emprise,
            'em_eco_01_espace_pelouse_ac_elec'
            )

        # Parametres
        exoneration = parameters(period).daf.redevance_domaniale.exoneration.discount_rate
        init = parameters(period).daf.redevance_domaniale.type_3[emprise].init
        threshold_1 = parameters(period).daf.redevance_domaniale.type_3[emprise].threshold_1
        rate_1 = parameters(period).daf.redevance_domaniale.type_3[emprise].rate_1
        threshold_2 = parameters(period).daf.redevance_domaniale.type_3[emprise].threshold_2
        rate_2 = parameters(period).daf.redevance_domaniale.type_3[emprise].rate_2
        threshold_3 = parameters(period).daf.redevance_domaniale.type_3[emprise].threshold_3
        rate_3 = parameters(period).daf.redevance_domaniale.type_3[emprise].rate_3

        # Calcul du montant
        # Pour les durées en heures inférieures à la journée, le type de calcul est mis à type_23
        # Si jamais dans le future, le calcul du montant par heures devient linéraire,
        # il sera possible d'ajouter un rate_0 et de supprimer celle type_23
        montant_intermediaire = select(
            [
                duree < threshold_1,
                duree <= threshold_2,
                duree <= threshold_3,
                duree > threshold_3
                ],
            [
                init,
                init + rate_1 * (duree - threshold_1),
                init + rate_1 * (threshold_2 - threshold_1) + rate_2 * (duree - threshold_2),
                init + rate_1 * (threshold_2 - threshold_1) + rate_2 * (threshold_3 - threshold_2) + rate_3 * (duree - threshold_3)
                ]
            )

        montant_total = arrondi_superieur(
            (montant_intermediaire + majoration) * (1. - exoneration * activite_cultuelle)
            )
        return where(type_calcul_est_3, montant_total, 0.)


class temporalite_redevance_domaniale_type_3(Variable):
    value_type = Enum
    possible_values = Temporalite
    default_value = Temporalite.Non_Applicable
    entity = Personne
    definition_period = DAY
    label = "Temporalité (journalier, annuel, mensuel) pour la redevance domaniale"
    reference = "Arrêté NOR DAF2120267AC-3"
