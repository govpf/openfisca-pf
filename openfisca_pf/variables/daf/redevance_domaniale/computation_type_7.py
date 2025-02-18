# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    DAY,
    Enum,
    max_,
    Parameters,
    Period,
    Variable,
    where
    )
from openfisca_pf.constants.units import BOOLEAN, XPF
from openfisca_pf.entities import Personne
from openfisca_pf.enums.domaine import Temporalite
from openfisca_pf.functions.currency import arrondi_superieur
from openfisca_pf.functions.domaine import figer_emprise


class type_calcul_redevance_domaniale_est_type_7(Variable):
    entity = Personne
    definition_period = DAY
    value_type = bool
    default_value = False
    unit = BOOLEAN
    label = "Determine si le calcul de redevance domaniale est de type 7"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return personne('type_calcul_redevance_domaniale', period, parameters) == '7'


class montant_base_redevance_domaniale_type_7(Variable):
    entity = Personne
    definition_period = DAY
    value_type = float
    default_value = 0.
    unit = XPF
    label = "Montant de base (journalier, annuel, mensuel) de la redevance domaniale dûe avec un calcul dépendant de la zone géographique mais pas de la durée"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        # Variables
        type_calcul = personne('type_calcul_redevance_domaniale_est_type_7', period, parameters)
        emprise = personne('nature_emprise_occupation_redevance_domaniale', period, parameters)
        variable = personne('variable_redevance_domaniale', period, parameters)
        nombre = personne('nombre_unite_redevance_domaniale', period, parameters)
        zone = personne('zone_occupation_redevance_domaniale', period, parameters)

        # Lors de demandes multiples avec des types de calculs différents,
        # il est nécessaire de figer l'emprise sur une donnée existante pour le type associé.
        emprise = figer_emprise(
            type_calcul,
            emprise,
            'ip_eco_01_equipement_pays'
            )

        # Parameters
        part_fixe = parameters(period).daf.redevance_domaniale.type_7[emprise][zone].part_fixe
        part_unitaire = parameters(period).daf.redevance_domaniale.type_7[emprise][zone].part_unitaire
        part_variable = parameters(period).daf.redevance_domaniale.type_7[emprise][zone].part_variable
        montant_minimum = parameters(period).daf.redevance_domaniale.type_7[emprise][zone].montant_minimum

        # Price computation
        montant_intermediaire = part_fixe + part_unitaire * nombre + part_variable * variable

        # Minimum comparison
        montant_base = max_(arrondi_superieur(montant_intermediaire), montant_minimum)
        return where(type_calcul, montant_base, 0.)


class montant_total_redevance_domaniale_type_7(Variable):
    entity = Personne
    definition_period = DAY
    value_type = float
    default_value = 0.
    unit = XPF
    label = "Montant total de la redevance domaniale dûe avec un calcul dépendant de la zone géographique mais pas de la durée"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return personne('montant_base_redevance_domaniale_type_7', period, parameters)


class temporalite_redevance_domaniale_type_7(Variable):
    entity = Personne
    definition_period = DAY
    value_type = Enum
    possible_values = Temporalite
    default_value = Temporalite.Non_Applicable
    label = "Temporalité (journalier, annuel, mensuel) pour la redevance domaniale dûe avec un calcul de type classique"
    reference = "Arrêté NOR DAF2120267AC-3"
