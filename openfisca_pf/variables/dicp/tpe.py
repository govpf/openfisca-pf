# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    GroupPopulation,
    not_,
    ParameterNode,
    Period,
    Population,
    select,
    Variable,
    YEAR
    )
from openfisca_pf.entities import Pays, Personne
from openfisca_pf.enums.impots import TypePersonne


class redevable_tpe(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    label = "Défini si l'entreprise est éligible TPE"
    reference = []

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        est_personne_physique = personne('type_personne', period) == TypePersonne.P
        ca_total = personne('chiffre_affaire_total', period)
        ca_inferieur_a_5000000 = ca_total < 5000000
        eligible_tpe = True
        for activite in [*parameters(period).dicp.abattements_it_cstns.activites_prestations]:
            activite_eligible = parameters(period).dicp.abattements_it_cstns.activites_prestations[activite].eligible_tpe
            chiffre_affaire_activite = personne(f'chiffre_affaire_{activite}', period)
            eligible_tpe = eligible_tpe * ((activite_eligible == 1) + (chiffre_affaire_activite == 0))
        return est_personne_physique * eligible_tpe * ca_inferieur_a_5000000


class montant_tpe_du(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant TPE dû par l'entreprise"
    reference = []

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        redevable_tpe = personne('redevable_tpe', period)
        ca_total = personne('chiffre_affaire_total', period)
        ca_inferieur_a_2000000 = ca_total < 2000000
        ca_superieur_a_2000000 = ca_total >= 2000000
        return select(
            [redevable_tpe * ca_inferieur_a_2000000, redevable_tpe * ca_superieur_a_2000000, not_(redevable_tpe)],
            [25000, 45000, 0]
            )


class nombre_entreprises_redevables_TPE_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = "Nombre d'entreprises du pays redevables de la TPE"
    reference = []

    def formula(pays: GroupPopulation, period: Period, parameters: ParameterNode) -> ArrayLike:
        redevable_tpe = pays.members('redevable_tpe', period)
        return pays.sum(redevable_tpe * 1)
