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
from openfisca_pf.constants.units import BOOLEAN, XPF
from openfisca_pf.entities import Personne
from openfisca_pf.enums.domaine import Temporalite
from openfisca_pf.functions.domaine import figer_emprise


class type_calcul_redevance_domaniale_est_type_5(Variable):
    entity = Personne
    definition_period = DAY
    value_type = bool
    default_value = False
    unit = BOOLEAN
    label = "Determine si le calcul de redevance domaniale est de type 5"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return personne('type_calcul_redevance_domaniale', period, parameters) == '5'


class montant_base_redevance_domaniale_type_5(Variable):
    entity = Personne
    definition_period = DAY
    value_type = float
    default_value = 0.
    unit = XPF
    label = "Montant de base (journalier, mensuel, annuel) de la redevance domaniale dûe avec un calcul dont le montant annuel évolue par palier de surface"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        # Variables
        type_calcul = personne('type_calcul_redevance_domaniale_est_type_5', period, parameters)
        emprise = personne('nature_emprise_occupation_redevance_domaniale', period)
        variable = personne('variable_redevance_domaniale', period)

        # Lors de demandes multiples avec des types de calculs différents,
        # il est nécessaire de figer l'emprise sur une donnée existante pour le type associé.
        emprise = figer_emprise(
            type_calcul,
            emprise,
            'if_eco_01_parc_poisson_hors_passe'
            )

        # Parametres
        init = parameters(period).daf.redevance_domaniale.type_5[emprise].init
        rate_0 = parameters(period).daf.redevance_domaniale.type_5[emprise].rate_0
        threshold_1 = parameters(period).daf.redevance_domaniale.type_5[emprise].threshold_1
        rate_1 = parameters(period).daf.redevance_domaniale.type_5[emprise].rate_1
        threshold_2 = parameters(period).daf.redevance_domaniale.type_5[emprise].threshold_2
        rate_2 = parameters(period).daf.redevance_domaniale.type_5[emprise].rate_2
        montant_minimum = parameters(period).daf.redevance_domaniale.type_5[emprise].montant_minimum

        # Calcul du montant
        montant_intermediaire = select(
            [
                variable < threshold_1,
                variable <= threshold_2,
                variable > threshold_2
                ],
            [
                init + rate_0 * variable,
                init + rate_0 * threshold_1 + rate_1 * (variable - threshold_1),
                init + rate_0 * threshold_1 + rate_1 * (threshold_2 - threshold_1) + rate_2 * (variable - threshold_2)
                ]
            )

        montant_base = max_(arrondi_superrieur(montant_intermediaire), montant_minimum)
        return where(type_calcul, montant_base, 0.)


class montant_total_redevance_domaniale_type_5(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de total de la redevance domaniale dûe avec un calcul dont le montant annuel évolue par palier de surface"
    reference = "Arrêté NOR DAF2120267AC-3"
    unit = 'currency-XPF'

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        # Variables
        type_calcul = personne('type_calcul_redevance_domaniale_est_type_5', period, parameters)
        emprise = personne('nature_emprise_occupation_redevance_domaniale', period)
        duree = personne('duree_occupation_redevance_domaniale_jour', period)
        majoration = personne('majoration_redevance_domaniale', period)
        base = personne('montant_base_redevance_domaniale_type_5', period)

        # Lors de demandes multiples avec des types de calculs différents,
        # il est nécessaire de figer l'emprise sur une donnée existante pour le type associé.
        emprise = figer_emprise(
            type_calcul,
            emprise,
            'if_eco_01_parc_poisson_hors_passe'
            )

        # Parametres
        base_calcul_jour = parameters(period).daf.redevance_domaniale.type_5[emprise].base_calcul_jour
        montant_minimum = parameters(period).daf.redevance_domaniale.type_5[emprise].montant_minimum

        # Calcul du montant pour la durée totale
        montant_total = max_(arrondi_superrieur(base * duree / base_calcul_jour), montant_minimum) + majoration

        # La comparaison avec le minmum est effectué sur le montant de base et le montant totale
        # pour correctement calculer pour des durées inférieures à la durée de base
        return where(type_calcul, montant_total, 0.)


class temporalite_redevance_domaniale_type_5(Variable):
    value_type = Enum
    possible_values = Temporalite
    default_value = Temporalite.Non_Applicable
    entity = Personne
    definition_period = DAY
    label = "Temporalité (journalier, annuel, mensuel) pour la redevance domaniale"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        # Variables
        type_calcul = personne('type_calcul_redevance_domaniale_est_type_5', period)
        emprise = personne('nature_emprise_occupation_redevance_domaniale', period)

        # Lors de demandes multiples avec des types de calculs différents,
        # il est nécessaire de figer l'emprise sur une donnée existante pour le type associé.
        emprise = figer_emprise(
            type_calcul,
            emprise,
            'if_eco_01_parc_poisson_hors_passe'
            )

        # Parametres
        base_calcul_jour = parameters(period).daf.redevance_domaniale.type_5[emprise].base_calcul_jour
        nombre_jour_par_an = parameters(period).daf.redevance_domaniale.constantes.nombre_jour_par_an_rd
        nombre_jour_par_mois = parameters(period).daf.redevance_domaniale.constantes.nombre_jour_par_mois_rd
        nombre_jour_par_semaine = parameters(period).daf.redevance_domaniale.constantes.nombre_jour_par_semaine_rd

        # Transformation
        temporalite = select(
            [
                base_calcul_jour == 1,
                base_calcul_jour == nombre_jour_par_semaine,
                base_calcul_jour == nombre_jour_par_mois,
                base_calcul_jour == nombre_jour_par_an
                ],
            [
                Temporalite.Journalier,
                Temporalite.Hebdomadaire,
                Temporalite.Mensuel,
                Temporalite.Annuel
                ]
            )
        return where(type_calcul, temporalite, Temporalite.Non_Applicable)
