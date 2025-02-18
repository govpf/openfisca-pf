# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    Enum,
    Parameters,
    Period,
    set_input_divide_by_period,
    Variable,
    where,
    YEAR
    )
from openfisca_pf.entities import Pays, Personne
from openfisca_pf.enums.impots import TypePersonne, TypeSociete


class type_societe(Variable):
    value_type = Enum
    possible_values = TypeSociete
    default_value = TypeSociete.EI
    entity = Personne
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = 'Statuts de la société'
    reference = []


class activite_location(Variable):
    entity = Personne
    definition_period = YEAR
    value_type = bool
    default_value = False
    label = "L'entreprise pratique t'elle une activité de location meublée, non meublée ou de terrain nu ?"


class type_personne(Variable):
    entity = Personne
    definition_period = YEAR
    value_type = Enum
    possible_values = TypePersonne
    default_value = TypePersonne.P
    set_input = set_input_divide_by_period
    label = 'Un contribuable peut etre une personne physique(P) ou morale (M)'
    reference = []

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        type_societe = personne('type_societe', period, parameters)
        return where(
            type_societe == TypeSociete.EI,
            TypePersonne.P,
            TypePersonne.M
            )


class activite_commerciale(Variable):
    entity = Personne
    definition_period = YEAR
    value_type = bool
    default_value = False
    label = "Indique si l'entreprise à une activité commerciale"
    reference = []

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        chiffre_affaire_total_ventes = personne('chiffre_affaire_total_ventes', period, parameters)
        return chiffre_affaire_total_ventes > 0


class activite_prestations(Variable):
    entity = Personne
    definition_period = YEAR
    default_value = False
    value_type = bool
    label = "Indique si l'entreprise à une activité de prestations"
    reference = []

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        chiffre_affaire_total_prestations = personne('chiffre_affaire_total_prestations', period, parameters)
        return chiffre_affaire_total_prestations > 0


class nombre_entreprises_contribuables_pays(Variable):
    entity = Pays
    definition_period = YEAR
    value_type = int
    default_value = 0
    label = "Nombre d'entreprises du pays"
    reference = []

    def formula(pays: Pays) -> ArrayLike:
        return pays.nb_persons(Pays.CONTRIBUABLES)


class chiffre_affaire_prestations_contribuables_pays(Variable):
    entity = Pays
    definition_period = YEAR
    value_type = float
    default_value = 0.
    label = "Chiffre d'affaire total en prestation des entreprises contribuables du pays"
    reference = []

    def formula(pays: Pays, period: Period) -> ArrayLike:
        chiffre_affaire_total_prestations = pays.members('chiffre_affaire_total_prestations', period)
        return pays.sum(chiffre_affaire_total_prestations)


class chiffre_affaire_ventes_contribuables_pays(Variable):
    entity = Pays
    definition_period = YEAR
    value_type = float
    default_value = 0.
    label = "Chiffre d'affaire total en ventes des entreprises contribuables du pays"
    reference = []

    def formula(pays: Pays, period: Period) -> ArrayLike:
        chiffre_affaire_total_ventes = pays.members('chiffre_affaire_total_ventes', period)
        return pays.sum(chiffre_affaire_total_ventes)


class base_imposable_it_prestations_contribuables_pays(Variable):
    entity = Pays
    definition_period = YEAR
    value_type = float
    default_value = 0.
    label = "Somme des bases imposables pour prestations de l'impôt sur les transactions de toutes les entreprises contribuables du pays"
    reference = []

    def formula(pays: Pays, period: Period) -> ArrayLike:
        base_imposable_it_prestations = pays.members('base_imposable_it_prestations', period)
        return pays.sum(base_imposable_it_prestations)


class base_imposable_it_ventes_contribuables_pays(Variable):
    entity = Pays
    definition_period = YEAR
    value_type = float
    default_value = 0.
    label = "Somme des bases imposables pour ventes de l'impôt sur les transactions de toutes les entreprises contribuables du pays"
    reference = []

    def formula(pays: Pays, period: Period) -> ArrayLike:
        base_imposable_it_ventes = pays.members('base_imposable_it_ventes', period)
        return pays.sum(base_imposable_it_ventes)
