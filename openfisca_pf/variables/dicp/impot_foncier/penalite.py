# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    date,
    DAY,
    ParameterNode,
    Period,
    Population,
    Variable,
    )
from openfisca_pf.entities import Personne
from openfisca_pf.functions.time import (
    annee_de_la_date,
    as_date,
    as_duration,
    jour_de_la_date,
    relative_delta_months,
    relative_delta_days
    )


class date_de_changement(Variable):
    value_type = date
    entity = Personne
    definition_period = DAY
    default_value = date(1970, 1, 1)
    label = "Date à laquelle est effectué le changement de la valeur locative d'un bien."


class date_de_declaration(Variable):
    value_type = date
    entity = Personne
    definition_period = DAY
    default_value = date(1970, 1, 1)
    label = "Date de déclaration de la modification de la valeur locative d'un bien."


class penalite_majoration_fixe_appliquee(Variable):
    value_type = bool
    entity = Personne
    definition_period = DAY
    default_value = False
    label = "True s'il faut appliquer la pénalité de majoration fixe suite à une déclaration de modification de valeur locative tardive, False sinon."

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        date_de_changement = personne('date_de_changement', period).astype(date)
        date_de_declaration = personne('date_de_declaration', period).astype(date)
        date_dernier_delai_declaration = date_de_changement + relative_delta_months(3)
        return date_de_declaration > date_dernier_delai_declaration


class date_debut_decompte_interet_de_retard(Variable):
    value_type = date
    entity = Personne
    definition_period = DAY
    default_value = date(1970, 1, 1)
    label = "Date à partir de laquelle la pénalité d'intérêt de retard est appliquée à la déclaration de modification de valeur locative."

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        date_de_changement = personne('date_de_changement', period).astype(date)
        date_debut_decompte_interet_de_retard = date_de_changement + relative_delta_months(4)
        date_debut_decompte_interet_de_retard -= relative_delta_days(jour_de_la_date(date_debut_decompte_interet_de_retard))
        return date_debut_decompte_interet_de_retard


class penalite_interet_de_retard_appliquee(Variable):
    value_type = bool
    entity = Personne
    definition_period = DAY
    default_value = False
    label = "True s'il faut appliquer la pénalité d'intérêt de retard suite à une déclaration de modification de valeur locative tardive, False sinon."

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        date_de_changement = personne('date_de_changement', period).astype(date)
        date_de_declaration = personne('date_de_declaration', period).astype(date)
        date_debut_decompte_interet_de_retard = personne('date_debut_decompte_interet_de_retard', period).astype(date)
        annee_changement = annee_de_la_date(date_de_changement)
        annee_declaration = annee_de_la_date(date_de_declaration)
        return (date_de_declaration >= date_debut_decompte_interet_de_retard) * (annee_changement != annee_declaration)


class montant_penalite_majoration_fixe(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    default_value = 0.
    label = "Montant de la pénalité de majoration fixe."

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        # TODO : Obtenir la bonne base de calcul
        impot_foncier_total = personne('impot_foncier_total', period)
        taux_majoration_fixe = parameters(period).dicp.impot_foncier.penalites.taux.majoration_fixe
        return impot_foncier_total * taux_majoration_fixe


class total_mois_de_retard_declaration_modification_valeur_locative(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    default_value = 0
    label = "Nombre de mois de retard accumulés avant la déclaration de la modification de la valeur locative."

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        date_debut_decompte_interet_de_retard = personne('date_debut_decompte_interet_de_retard', period).astype(date)
        date_de_declaration = personne('date_de_declaration', period).astype(date)
        return as_duration(
            as_date(date_de_declaration, 'M') - as_date(date_debut_decompte_interet_de_retard, 'M'),
            'M'
            ) + 1


class montant_penalite_interet_de_retard(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    default_value = 0.
    label = "Montant de la pénalité d'intérêt de retard du rôle foncier."

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        total_mois_de_retard = personne('total_mois_de_retard_declaration_modification_valeur_locative', period)
        # TODO : Obtenir la bonne base de calcul
        impot_foncier_total = personne('impot_foncier_total', period)
        taux_interet_de_retard = parameters(period).dicp.impot_foncier.penalites.taux.interet_de_retard
        return impot_foncier_total * total_mois_de_retard * taux_interet_de_retard
