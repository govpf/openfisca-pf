# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    date,
    max_,
    ParameterNode,
    Period,
    Population,
    select,
    Variable,
    YEAR
    )
from openfisca_pf.entities import Personne
from openfisca_pf.functions.time import (
    as_date,
    as_duration,
    prochaine_date,
    relative_delta_months,
    relative_delta_days
    )


# --------------------------------------------------
# ---         DATES ET MONTANTS D'IMPÔTS         ---
# --------------------------------------------------


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


class date_limite_de_declaration(Variable):
    value_type = date
    entity = Personne
    definition_period = YEAR
    default_value = date(1970, 1, 1)
    label = "Date à partir de laquelle une déclaration est en retard par rapport à la date du changement"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        date_de_changement = personne('date_de_changement', period).astype(date)
        return date_de_changement + relative_delta_months(3)


class premiere_mise_en_demeure_recue(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce qu'une première mise en demeure à été émise et receptionnée"


class date_de_reception_premiere_mise_en_demeure(Variable):
    value_type = date
    entity = Personne
    definition_period = YEAR
    default_value = date(1970, 1, 1)
    label = "Date de la réception de la première mise en demeure"


class date_limite_premiere_mise_en_demeure(Variable):
    value_type = date
    entity = Personne
    definition_period = YEAR
    default_value = date(1970, 1, 1)
    label = "Date à partir de laquelle une déclaration est en retard par rapport à la date de la première mise en demeure"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        date_de_reception_premiere_mise_en_demeure = personne('date_de_reception_premiere_mise_en_demeure', period).astype(date)
        return date_de_reception_premiere_mise_en_demeure + relative_delta_days(30)


class premiere_mise_en_demeure_depassee(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce qu'une permière mise en demeure à été emise, reçue, et est-ce que  la déclaration à été faite après la date limite de la permière mise en demeure"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        premiere_mise_en_demeure_recue = personne('premiere_mise_en_demeure_recue', period)
        date_de_declaration = personne('date_de_declaration', period).astype(date)
        date_limite_premiere_mise_en_demeure = personne('date_limite_premiere_mise_en_demeure', period).astype(date)
        return premiere_mise_en_demeure_recue * (date_de_declaration > date_limite_premiere_mise_en_demeure)


class deuxieme_mise_en_demeure_recue(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce qu'une deuxième mise en demeure à été émise et receptionnée"


class date_de_reception_deuxieme_mise_en_demeure(Variable):
    value_type = date
    entity = Personne
    definition_period = YEAR
    default_value = date(1970, 1, 1)
    label = "Date de la réception de la deuxième mise en demeure"


class date_limite_deuxieme_mise_en_demeure(Variable):
    value_type = date
    entity = Personne
    definition_period = YEAR
    default_value = date(1970, 1, 1)
    label = "Date à partir de laquelle une déclaration est en retard par rapport à la date de la deuxième mise en demeure"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        date_de_reception_deuxieme_mise_en_demeure = personne('date_de_reception_deuxieme_mise_en_demeure', period).astype(date)
        return date_de_reception_deuxieme_mise_en_demeure + relative_delta_days(30)


class deuxieme_mise_en_demeure_depassee(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce qu'une deuxième mise en demeure à été emise, reçue, et est-ce que  la déclaration à été faite après la date limite de la deuxième mise en demeure"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        deuxieme_mise_en_demeure_recue = personne('deuxieme_mise_en_demeure_recue', period)
        date_de_declaration = personne('date_de_declaration', period)
        date_limite_deuxieme_mise_en_demeure = personne('date_limite_deuxieme_mise_en_demeure', period)
        return deuxieme_mise_en_demeure_recue * (date_de_declaration > date_limite_deuxieme_mise_en_demeure)


class impot_qui_a_ete_mis_en_recouvrement(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant d'impôt qui à été mis en recouvrement avant la reception de la déclaration tardive"


class impot_qui_aurait_du_etre_mis_en_recouvrement(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant d'impôt qui aurait dut être mis en recouvrement si la déclaration avait été recu dans les temps"


# --------------------------------------------------
# ---                    BASE                    ---
# --------------------------------------------------


class base_de_calcul_des_penalites(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Base de calcul des pénalités de retard"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        impot_qui_a_ete_mis_en_recouvrement = personne('impot_qui_a_ete_mis_en_recouvrement', period)
        impot_qui_aurait_du_etre_mis_en_recouvrement = personne('impot_qui_aurait_du_etre_mis_en_recouvrement', period)
        return max_(
            impot_qui_aurait_du_etre_mis_en_recouvrement - impot_qui_a_ete_mis_en_recouvrement,
            0
            )


class penalites_applicables(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce que des pénalités sont applicables compte tenu des dates et des montants d'impôt"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        base_de_calcul_des_penalites = personne('base_de_calcul_des_penalites', period)
        return base_de_calcul_des_penalites > 0


# --------------------------------------------------
# ---              MAJORATION FIXE               ---
# --------------------------------------------------


class penalite_majoration_fixe_appliquee(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Indique si une pénalité de majoration fixe s'applique suite à une déclaration"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        penalites_applicables = personne('penalites_applicables', period)
        date_limite_de_declaration = personne('date_limite_de_declaration', period).astype(date)
        date_de_declaration = personne('date_de_declaration', period).astype(date)
        return penalites_applicables * (date_de_declaration > date_limite_de_declaration)


class taux_penalite_majoration_fixe(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.
    label = "Taux de la majoration fixe d'une pénalité de retard à l'impôt foncier"

    def formula_1995_08_24(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        premiere_mise_en_demeure_depassee = personne('premiere_mise_en_demeure_depassee', period)
        deuxieme_mise_en_demeure_depassee = personne('deuxieme_mise_en_demeure_depassee', period)

        return select(
            [
                deuxieme_mise_en_demeure_depassee,
                premiere_mise_en_demeure_depassee
                ],
            [
                parameters(period).dicp.penalite.taux_majoration_fixe.apres_deuxieme_mise_en_demeure,
                parameters(period).dicp.penalite.taux_majoration_fixe.apres_premiere_mise_en_demeure
                ],
            parameters(period).dicp.penalite.taux_majoration_fixe.normal
            )


class montant_penalite_majoration_fixe(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.
    label = "Montant de la majoration fixe d'une pénalité de retard à l'impôt foncier"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        penalite_majoration_fixe_appliquee = personne('penalite_majoration_fixe_appliquee', period)
        base_de_calcul_des_penalites = personne('base_de_calcul_des_penalites', period)
        taux_penalite_majoration_fixe = personne('taux_penalite_majoration_fixe', period)
        return penalite_majoration_fixe_appliquee\
            * base_de_calcul_des_penalites * taux_penalite_majoration_fixe

# --------------------------------------------------
# ---             INTÉRÊTS DE RETARD             ---
# --------------------------------------------------


class date_de_debut_du_decompte_interet_de_retard(Variable):
    value_type = date
    entity = Personne
    definition_period = YEAR
    default_value = date(1970, 1, 1)
    label = "Date à partir de laquelle le décompte des intérêts de retard commence"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        date_de_changement = personne('date_de_changement', period).astype(date)
        mois = parameters(period).dicp.impot_foncier.calendrier.date_de_debut_des_interets_de_retard.mois
        jour = parameters(period).dicp.impot_foncier.calendrier.date_de_debut_des_interets_de_retard.jour
        return prochaine_date(date_de_changement, mois, jour)


class penalite_interet_de_retard_appliquee(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Indique s'il faut appliquer la pénalité d'intérêt de retard suite à une déclaration"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        penalites_applicables = personne('penalites_applicables', period)
        date_de_declaration = personne('date_de_declaration', period).astype(date)
        date_de_debut_du_decompte_interet_de_retard = personne('date_de_debut_du_decompte_interet_de_retard', period).astype(date)
        return penalites_applicables\
            * (date_de_declaration >= date_de_debut_du_decompte_interet_de_retard)


class nombre_de_mois_de_retard(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "nombre de mois de retard entre la date de déclaration et la date de début du décompte des intérêts de retard"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        date_de_declaration = personne('date_de_declaration', period).astype(date)
        date_de_debut_du_decompte_interet_de_retard = personne('date_de_debut_du_decompte_interet_de_retard', period).astype(date)

        return max_(
            as_duration(
                as_date(date_de_declaration, 'D') - as_date(date_de_debut_du_decompte_interet_de_retard, 'D'),
                'M'
                ) + 1,
            0
            )


class taux_penalite_interet_de_retard(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.
    label = "Taux de la pénalité d'intérêt de retard du foncier."

    def formula_1995_08_24(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.penalite.taux_interet_de_retard


class montant_penalite_interet_de_retard(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.
    label = "Montant de la pénalité d'intérêt de retard du rôle foncier."

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        penalite_interet_de_retard_appliquee = personne('penalite_interet_de_retard_appliquee', period)
        base_de_calcul_des_penalites = personne('base_de_calcul_des_penalites', period)
        nombre_de_mois_de_retard = personne('nombre_de_mois_de_retard', period)
        taux_penalite_interet_de_retard = personne('taux_penalite_interet_de_retard', period)
        return penalite_interet_de_retard_appliquee\
            * base_de_calcul_des_penalites * nombre_de_mois_de_retard * taux_penalite_interet_de_retard
