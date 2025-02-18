# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    DAY,
    Parameters,
    Period,
    select,
    Variable
    )
from openfisca_pf.entities import Personne
from openfisca_pf.functions.currency import arrondi_superieur


class majoration_redevance_domaniale(Variable):
    entity = Personne
    definition_period = DAY
    value_type = float
    label = "Majoration apportée à la tarification de base"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        # Variables
        nbr_participant = personne('nombre_participant_redevance_domaniale', period)

        # Parameters
        rate_participant_1 = parameters(period).daf.redevance_domaniale.majoration_redevance_domaniale.rate_participant_1
        threshold_participant_1 = parameters(period).daf.redevance_domaniale.majoration_redevance_domaniale.threshold_participant_1
        rate_participant_2 = parameters(period).daf.redevance_domaniale.majoration_redevance_domaniale.rate_participant_2
        threshold_participant_2 = parameters(period).daf.redevance_domaniale.majoration_redevance_domaniale.threshold_participant_2

        # Calcul de la majoration liée au nombre de participant
        montant_intermediaire = select(
            [
                nbr_participant < threshold_participant_1,
                nbr_participant < threshold_participant_2,
                nbr_participant >= threshold_participant_2
                ],
            [
                0,
                rate_participant_1 * nbr_participant,
                rate_participant_2 * nbr_participant
                ]
            )
        return arrondi_superieur(montant_intermediaire)
