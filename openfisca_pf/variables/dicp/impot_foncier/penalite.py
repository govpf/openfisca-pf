# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    date,
    max_,
    ParameterNode,
    Period,
    Population,
    Variable,
    YEAR,
    where
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
    definition_period = YEAR
    default_value = date(1970, 1, 1)
    label = "Date à laquelle est effectué le changement de la valeur locative d'un bien"


class date_de_declaration(Variable):
    value_type = date
    entity = Personne
    definition_period = YEAR
    default_value = date(1970, 1, 1)
    label = "Date de déclaration de la modification de la valeur locative d'un bien"


class date_de_reception_premiere_mise_en_demeure(Variable):
    value_type = date
    entity = Personne
    definition_period = YEAR
    default_value = date(1970, 1, 1)
    label = "Date de la réception de la première mise en demeure du foncier"


class impot_foncier_total_avant_changement(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant d'impôt foncier précédemment mis en recouvrement avant la saisie du changement"


class base_de_calcul_penalites(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Base de calcul des pénalités de retard à l'impôt foncier"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        avant = personne('impot_foncier_total_avant_changement', period)
        apres = personne('impot_foncier_total', period)
        base = apres - avant
        return max_(0, base)


class date_limite_de_declaration(Variable):
    value_type = date
    entity = Personne
    definition_period = YEAR
    default_value = date(1970, 1, 1)
    label = "Date à partir de laquelle un déclaration est en retard."

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        date_de_changement = personne('date_de_changement', period).astype(date)
        return date_de_changement + relative_delta_months(3)


class penalite_majoration_fixe_appliquee(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Indique si il faut appliquer la pénalité de majoration fixe suite à une déclaration"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        date_dernier_delai_declaration = personne('date_limite_de_declaration', period).astype(date)
        date_de_declaration = personne('date_de_declaration', period).astype(date)
        base_de_calcul = personne('base_de_calcul_penalites', period)
        return (date_de_declaration > date_dernier_delai_declaration) \
            * (base_de_calcul > 0)


class date_debut_decompte_interet_de_retard(Variable):
    value_type = date
    entity = Personne
    definition_period = YEAR
    default_value = date(1970, 1, 1)
    label = "Date à partir de laquelle la pénalité d'intérêt de retard est appliquée à la déclaration de modification de valeur locative"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        date_debut_decompte_interet_de_retard = personne('date_limite_de_declaration', period).astype(date)
        date_debut_decompte_interet_de_retard += relative_delta_months(1)
        date_debut_decompte_interet_de_retard -= relative_delta_days(jour_de_la_date(date_debut_decompte_interet_de_retard))
        return date_debut_decompte_interet_de_retard


class penalite_interet_de_retard_appliquee(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Indique s'il faut appliquer la pénalité d'intérêt de retard suite à une déclaration"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        date_de_changement = personne('date_de_changement', period).astype(date)
        date_de_declaration = personne('date_de_declaration', period).astype(date)
        date_debut_decompte_interet_de_retard = personne('date_debut_decompte_interet_de_retard', period).astype(date)
        base_de_calcul = personne('base_de_calcul_penalites', period)
        annee_changement = annee_de_la_date(date_de_changement)
        annee_declaration = annee_de_la_date(date_de_declaration)
        return (date_de_declaration >= date_debut_decompte_interet_de_retard) \
            * (annee_changement != annee_declaration) \
            * (base_de_calcul > 0)


class reception_premiere_mise_en_demeure(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Inidique si une première mise en demeure a été réceptionnée"


class penalite_majoration_fixe_apres_premiere_mise_en_demeure_appliquee(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Indique si il faut appliquer la pénalité de majoration fixe suite à une déclaration tardive après une première mise en demeure"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        penalite_majoration_fixe_appliquee = personne('penalite_majoration_fixe_appliquee', period)
        reception_premiere_mise_en_demeure = personne('reception_premiere_mise_en_demeure', period)
        date_de_declaration = personne('date_de_declaration', period).astype(date)
        date_limite_de_declaration = personne('date_limite_de_declaration', period).astype(date)
        date_de_reception_premiere_mise_en_demeure = personne('date_de_reception_premiere_mise_en_demeure', period).astype(date)

        date_dernier_delai_declaration_premiere_mise_en_demeure = date_de_reception_premiere_mise_en_demeure + relative_delta_days(30)
        return penalite_majoration_fixe_appliquee \
            * reception_premiere_mise_en_demeure \
            * (date_dernier_delai_declaration_premiere_mise_en_demeure >= date_limite_de_declaration) \
            * (date_de_declaration > date_dernier_delai_declaration_premiere_mise_en_demeure)


class taux_penalite_majoration_fixe(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.
    label = "Taux de la majoration fixe d'une pénalité de retard à l'impôt foncier"

    def formula_1995_08_24(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        penalite_majoration_fixe_apres_premiere_mise_en_demeure_appliquee = personne('penalite_majoration_fixe_apres_premiere_mise_en_demeure_appliquee', period)
        return where(
            penalite_majoration_fixe_apres_premiere_mise_en_demeure_appliquee,
            parameters(period).dicp.impot_foncier.penalites.taux.majoration_fixe_premiere_mise_en_demeure,
            parameters(period).dicp.impot_foncier.penalites.taux.majoration_fixe
            )


class montant_penalite_majoration_fixe(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.
    label = "Montant de la majoration fixe d'une pénalité de retard à l'impôt foncier"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        penalite_majoration_fixe_appliquee = personne('penalite_majoration_fixe_appliquee', period)
        base_de_calcul = personne('base_de_calcul_penalites', period)
        taux = personne('taux_penalite_majoration_fixe', period)
        return where(
            penalite_majoration_fixe_appliquee,
            base_de_calcul * taux,
            0
            )


class nombre_de_mois_de_retard_de_la_declaration(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Nombre de mois de retard accumulés entre la date limite de declaration suite au changement et la date de declaration actuelle"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        date_debut_decompte_interet_de_retard = personne('date_debut_decompte_interet_de_retard', period).astype(date)
        date_de_declaration = personne('date_de_declaration', period).astype(date)
        return as_duration(
            as_date(date_de_declaration, 'M') - as_date(date_debut_decompte_interet_de_retard, 'M'),
            'M'
            ) + 1


class taux_penalite_interet_de_retard(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.
    label = "Taux de la pénalité d'intérêt de retard du foncier."

    def formula_1995_08_24(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.impot_foncier.penalites.taux.interet_de_retard


class montant_penalite_interet_de_retard(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.
    label = "Montant de la pénalité d'intérêt de retard du rôle foncier."

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        penalite_interet_de_retard_appliquee = personne('penalite_interet_de_retard_appliquee', period)
        total_mois_de_retard = personne('nombre_de_mois_de_retard_de_la_declaration', period)
        base_de_calcul = personne('base_de_calcul_penalites', period)
        taux = personne('taux_penalite_interet_de_retard', period)
        return where(
            penalite_interet_de_retard_appliquee,
            base_de_calcul * total_mois_de_retard * taux,
            0
            )
