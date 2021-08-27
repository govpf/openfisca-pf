# -*- coding: utf-8 -*-

# This file defines the computation for occupation on public domain that relies on a affin computation
#  with a constant part, a unitary part and a surfacic part
# See https://openfisca.org/doc/key-concepts/variables.html

# Pour certaines emprises, une majoration peut-être apporté au prix pour différentes raisons:
#       - seuil de nombre de participatn à l'evenement
#       - Utilisation de service en plus


# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# # Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.variables.daf.redevance_domaniale.enums import *
from openfisca_pf.base import *


class majoration_redevance_domaniale(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Majoration apportée à la tarification de base"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne, period, parameters):
        # Variables
        nbr_participant = personne('nombre_participant_redevance_domaniale', period)

        # Parameters
        rate_participant_1 = parameters(period).daf.redevance_domaniale.majoration_redevance_domaniale.rate_participant_1
        threshold_participant_1 = parameters(period).daf.redevance_domaniale.majoration_redevance_domaniale.threshold_participant_1
        rate_participant_2 = parameters(period).daf.redevance_domaniale.majoration_redevance_domaniale.rate_participant_2
        threshold_participant_2 = parameters(period).daf.redevance_domaniale.majoration_redevance_domaniale.threshold_participant_2

        # Calcul de la majoration liée au nombre de participant
        #  Price computation
        montant_intermediaire = select([nbr_participant < threshold_participant_1,
                                        nbr_participant < threshold_participant_2,
                                        nbr_participant >= threshold_participant_2],
                                    [0,
                                    rate_participant_1 * nbr_participant,
                                    rate_participant_2 * nbr_participant
                                    ])
        # Minimum comparison
        majoration_redevance_domaniale = arrondiSup(montant_intermediaire)

        return majoration_redevance_domaniale
