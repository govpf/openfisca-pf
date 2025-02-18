# -*- coding: utf-8 -*-

from openfisca_pf.base import (
    ArrayLike,
    arrondi_superrieur,
    DAY,
    Enum,
    Parameters,
    Period,
    select,
    Variable,
    where
    )
from openfisca_pf.constants.units import BOOLEAN, XPF
from openfisca_pf.entities import Personne
from openfisca_pf.enums.domaine import Temporalite
from openfisca_pf.functions.domaine import figer_emprise


class type_calcul_redevance_domaniale_est_type_4(Variable):
    entity = Personne
    definition_period = DAY
    value_type = bool
    default_value = False
    unit = BOOLEAN
    label = "Determine si le calcul de redevance domaniale est de type 4"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return personne('type_calcul_redevance_domaniale', period, parameters) == '4'


class montant_base_redevance_domaniale_type_4(Variable):
    entity = Personne
    definition_period = DAY
    value_type = float
    default_value = 0.
    unit = XPF
    label = "Montant de la redevance domaniale dûe avec un calcul dont le taux journalier évolue par palier et les paramètres dépendant de la zone géographique"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return personne('montant_total_redevance_domaniale_type_4', period, parameters)


class montant_total_redevance_domaniale_type_4(Variable):
    entity = Personne
    definition_period = DAY
    value_type = float
    default_value = 0.
    unit = XPF
    label = "Montant de la redevance domaniale dûe avec un calcul dont le taux journalier évolue par palier et les paramètres dépendant de la zone géographique"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        # Variables
        type_calcul = personne('type_calcul_redevance_domaniale_est_type_4', period, parameters)
        emprise = personne('nature_emprise_occupation_redevance_domaniale', period, parameters)
        duree = personne('duree_occupation_redevance_domaniale_jour', period, parameters)
        zone = personne('zone_occupation_redevance_domaniale', period, parameters)
        majoration = personne('majoration_redevance_domaniale', period, parameters)
        exonere = personne('activite_cultuelle', period, parameters)

        # Lors de demandes multiples avec des types de calculs différents,
        # il est nécessaire de figer l'emprise sur une donnée existante pour le type associé.
        emprise = figer_emprise(
            type_calcul,
            emprise,
            'im_eco_02_foire_produit_locaux'
            )

        # Parametres
        exoneration = parameters(period).daf.redevance_domaniale.exoneration.discount_rate
        init = parameters(period).daf.redevance_domaniale.type_4[emprise][zone].init
        threshold_1 = parameters(period).daf.redevance_domaniale.type_4[emprise][zone].threshold_1
        rate_1 = parameters(period).daf.redevance_domaniale.type_4[emprise][zone].rate_1
        threshold_2 = parameters(period).daf.redevance_domaniale.type_4[emprise][zone].threshold_2
        rate_2 = parameters(period).daf.redevance_domaniale.type_4[emprise][zone].rate_2
        threshold_3 = parameters(period).daf.redevance_domaniale.type_4[emprise][zone].threshold_3
        rate_3 = parameters(period).daf.redevance_domaniale.type_4[emprise][zone].rate_3

        # Calcul du montant
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
        montant_total = arrondi_superrieur((montant_intermediaire + majoration) * (1 - exoneration * exonere))
        return where(type_calcul, montant_total, 0)


class temporalite_redevance_domaniale_type_4(Variable):
    entity = Personne
    definition_period = DAY
    value_type = Enum
    possible_values = Temporalite
    default_value = Temporalite.Non_Applicable
    label = "Temporalité (journalier, annuel, mensuel) pour la redevance domaniale"
    reference = "Arrêté NOR DAF2120267AC-3"
