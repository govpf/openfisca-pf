# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    DAY,
    Enum,
    GroupPopulation,
    ParameterNode,
    Period,
    Population,
    Variable
    )
from openfisca_pf.constants.time import NOMBRE_D_HEURES_PAR_JOUR
from openfisca_pf.constants.units import XPF_PER_DAY
from openfisca_pf.enums.domaine import (
    Temporalite,
    UnitesDuree
    )
from openfisca_pf.entities import Dossier, Personne
from openfisca_pf.functions.domaine import aggreger_variables


class type_calcul_redevance_domaniale(Variable):
    entity = Personne
    definition_period = DAY
    value_type = str
    label = 'Type de calcul utilisé pour calculer la redevance domaniale'
    reference = []

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        # Variables
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        unite_duree_occupation_redevance_domaniale = personne('unite_duree_occupation_redevance_domaniale', period)
        duree_occupation_redevance_domaniale = personne('duree_occupation_redevance_domaniale', period)

        # Paramètres
        type_calcul = parameters(period).daf.redevance_domaniale.type_calcul[nature_emprise_occupation_redevance_domaniale]

        # Selection selon un tarif horaire ou journalier
        # Pour les tarifs du SPJP, le mode de calcul pour une même emprise change si la durée est
        # exprimée en heure et pour une durée inférieure à la journée.
        # Pour distinguer le type de calcul horaire (et sélectionner donc le bon calcul), on ajoute arbitrairement 20 au type de calcul quotidien.
        # Cet ajout de 20, permet de créer des nouveaux types de calculs dans le futur.
        # L'ensemble des tarifs spéciaux du SPJP sont de type = 3
        unite_est_heure = (unite_duree_occupation_redevance_domaniale == UnitesDuree.Heures)
        duree_inferieur_jour = (duree_occupation_redevance_domaniale <= NOMBRE_D_HEURES_PAR_JOUR)
        tarif_spjp = (type_calcul == 3)

        # Calcul du type de calcul
        type_calcul_inter = type_calcul + (20 * unite_est_heure * duree_inferieur_jour * tarif_spjp)

        # Transformation en entier, puis en string (enum)
        return type_calcul_inter.astype(int).astype(str)


class montant_base_redevance_domaniale(Variable):
    entity = Personne
    definition_period = DAY
    value_type = float
    default_value = 0.
    unit = XPF_PER_DAY
    label = 'Montant de base la redevance domaniale dûe'

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        type_calcul = personne('type_calcul_redevance_domaniale', period)
        return aggreger_variables(personne, period, 'montant_base_redevance_domaniale_type_', type_calcul)


class montant_total_redevance_domaniale(Variable):
    entity = Personne
    definition_period = DAY
    value_type = float
    default_value = 0.
    unit = XPF_PER_DAY
    label = 'Montant de la redevance domaniale dûe'

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        type_calcul = personne('type_calcul_redevance_domaniale', period)
        return aggreger_variables(personne, period, 'montant_total_redevance_domaniale_type_', type_calcul)


class temporalite_redevance_domaniale(Variable):
    entity = Personne
    definition_period = DAY
    value_type = Enum
    possible_values = Temporalite
    default_value = Temporalite.Non_Applicable
    label = 'Temporalite du tarif de la redevance domaniale'

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        type_calcul = personne('type_calcul_redevance_domaniale', period)
        return aggreger_variables(personne, period, 'temporalite_redevance_domaniale_type_', type_calcul)


class montant_base_redevance_domaniale_dossier(Variable):
    entity = Dossier
    definition_period = DAY
    value_type = float
    default_value = 0.
    unit = XPF_PER_DAY
    label = 'Montant de base de redevance domaniale de toutes les demandes du dossier'

    def formula(dossier: GroupPopulation, period: Period, parameters: ParameterNode) -> ArrayLike:
        montant_base_redevance_domaniale = dossier.members('montant_base_redevance_domaniale', period)
        return dossier.sum(montant_base_redevance_domaniale)


class montant_total_redevance_domaniale_dossier(Variable):
    entity = Dossier
    definition_period = DAY
    value_type = float
    default_value = 0.
    unit = XPF_PER_DAY
    label = 'Montant total de redevance domaniale de toutes les demandes du dossier'

    def formula(dossier: GroupPopulation, period: Period, parameters: ParameterNode) -> ArrayLike:
        montant_total_redevance_domaniale = dossier.members('montant_total_redevance_domaniale', period)
        return dossier.sum(montant_total_redevance_domaniale)
