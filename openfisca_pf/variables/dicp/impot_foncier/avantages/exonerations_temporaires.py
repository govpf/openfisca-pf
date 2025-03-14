# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    date,
    not_,
    Parameters,
    Period,
    select,
    Variable,
    YEAR
    )
from openfisca_pf.entities import Pays, Personne
from openfisca_pf.functions.currency import arrondi_inferieur
from openfisca_pf.functions.time import annee_de_la_date

# ##################################################
# ###  CINQ ANS POUR LES NOUVELLES CONSTRUCTIONS ###
# ##################################################


AGE_MIN_EXONERATION_TEMPORAIRE_NOUVELLE_CONSTRUCTION: int = 1
AGE_MAX_EXONERATION_TEMPORAIRE_NOUVELLE_CONSTRUCTION: int = 5


class age_min_exoneration_temporaire_nouvelle_construction_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    default_value = 0
    label = "Age minimum pour qu'une nouvelle construction soit eligible à une exonération temporaraire de cinq ans pour les nouvelles constructions [lecture seule]"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return AGE_MIN_EXONERATION_TEMPORAIRE_NOUVELLE_CONSTRUCTION


class age_max_exoneration_temporaire_nouvelle_construction_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    default_value = 0
    label = "Age maximum pour qu'une nouvelle construction soit eligible à une exonération temporaraire de cinq ans pour les nouvelles constructions [lecture seule]"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return AGE_MAX_EXONERATION_TEMPORAIRE_NOUVELLE_CONSTRUCTION


class age_min_exoneration_temporaire_nouvelle_construction(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Age minimum pour qu'une nouvelle construction soit eligible à une exonération temporaraire de cinq ans pour les nouvelles constructions [lecture seule]"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return personne.pays('age_min_exoneration_temporaire_nouvelle_construction_pays', period, parameters)


class age_max_exoneration_temporaire_nouvelle_construction(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Age maximum pour qu'une nouvelle construction soit eligible à une exonération temporaraire de cinq ans pour les nouvelles constructions [lecture seule]"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return personne.pays('age_max_exoneration_temporaire_nouvelle_construction_pays', period, parameters)


class eligible_exoneration_temporaire_nouvelle_construction(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce que le bien est eligible à une exoneration temporaraire de cinq ans pour les nouvelles constructions"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        terrain = personne('terrain', period, parameters)
        return not_(terrain)


class exoneration_temporaire_nouvelle_construction_appliquee(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce que le bien est eligible à une exoneration temporaraire de cinq ans pour les nouvelles constructions"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        exoneration_permanente = personne('exoneration_permanente_appliquee', period, parameters)
        exoneration_temporaire_dix_ans = personne('exoneration_temporaire_habitation_principale_eligible_et_appliquee', period, parameters)
        eligible = personne('eligible_exoneration_temporaire_nouvelle_construction', period, parameters)
        age_min = personne('age_min_exoneration_temporaire_nouvelle_construction', period, parameters)
        age_max = personne('age_max_exoneration_temporaire_nouvelle_construction', period, parameters)
        age_du_bien = personne('age_du_bien', period, parameters)

        # L'exonération de cinq ans ne peut s'applique que si :
        # – Le bien n'est pas déjà définitivement exonéré
        # – Le bien ne bénéficie pas déjà de l'exonération temporaire de dix ans pour les habitations principales.
        # – Le bien est eligible à l'exonération temporaire de cinq ans.
        # – L'âge du bien est comprise dans la période d'exonération.
        return not_(exoneration_permanente) \
            * not_(exoneration_temporaire_dix_ans) \
            * eligible \
            * (age_min <= age_du_bien <= age_max)


class exoneration_temporaire_nouvelle_construction_eligible_et_appliquee(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce que le bien est eligible à l'exoneration temporaraire temporaraire de cinq ans pour les nouvelles constructons, et est ce que celle-ci s'applique sur ce bien"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        eligible = personne('eligible_exoneration_temporaire_nouvelle_construction', period, parameters)
        appliquee = personne('exoneration_temporaire_nouvelle_construction_appliquee', period, parameters)
        return eligible * appliquee


class taux_exoneration_temporaire_nouvelle_construction_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0
    label = "Taux d'exonération temporaraire de cinq ans pour les nouvelles constructions"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.impot_foncier.avantages.exoneration_temporaire.nouvelle_construction.taux  # 1.0


class taux_exoneration_temporaire_nouvelle_construction(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Taux d'exonération temporaraire de cinq ans pour les nouvelles constructions"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return personne.pays('taux_exoneration_temporaire_nouvelle_construction_pays', period, parameters)


class montant_exoneration_temporaire_nouvelle_construction(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant de l'exonération temporaraire de cinq ans pour les nouvelles constructions"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        eligible_et_applique = personne('exoneration_temporaire_nouvelle_construction_eligible_et_appliquee', period, parameters)
        base = personne('impot_foncier_part_pays_brute', period, parameters)
        taux = personne('taux_exoneration_temporaire_nouvelle_construction', period, parameters)
        return select(
            [eligible_et_applique],
            [arrondi_inferieur(base * taux)],
            0
            )


class duree_restante_exoneration_temporaire_nouvelle_construction(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Durée restante de l'exonération temporaraire de cinq ans pour cette nouvelle construction"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        eligible = personne('eligible_exoneration_temporaire_nouvelle_construction', period, parameters)
        age = personne('age_du_bien', period, parameters)
        age_min = personne('age_min_exoneration_temporaire_nouvelle_construction', period, parameters)
        age_max = personne('age_max_exoneration_temporaire_nouvelle_construction', period, parameters)

        return select(
            [eligible * (age < age_min), eligible * (age_min <= age <= age_max)],
            [age_max - age_min + 1, age_max - age],
            0
            )


# ##################################################
# ###  DIX ANS POUR LES HABITATIONS PRINCIPALES  ###
# ##################################################


AGE_MIN_EXONERATION_TEMPORAIRE_HABITATION_PRINCIPALE: int = 1
AGE_MAX_EXONERATION_TEMPORAIRE_HABITATION_PRINCIPALE: int = 10


class age_min_exoneration_temporaire_habitation_principale_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    default_value = 0
    label = "Age minimum pour qu'une habitation principale soit eligible à l'exonération temporaire de dix ans [lecture seule]"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2022_12_13(personne: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return AGE_MIN_EXONERATION_TEMPORAIRE_HABITATION_PRINCIPALE


class age_max_exoneration_temporaire_habitation_principale_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    default_value = 0
    label = "Age maximum pour qu'une habitation principale soit eligible à l'exonération temporaire de dix ans [lecture seule]"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2022_12_13(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return AGE_MAX_EXONERATION_TEMPORAIRE_HABITATION_PRINCIPALE


class date_limite_permis_de_construire_exoneration_temporaire_habitation_principale_pays(Variable):
    value_type = date
    entity = Pays
    definition_period = YEAR
    default_value = date(1970, 1, 1)
    label = "Date à partir de laquelle le permis de construire permet d'obtenir l'exonération de dix ans pour les habitations principale"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2022_12_13(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        annee = parameters(period).dicp.impot_foncier.avantages.exoneration_temporaire.habitation_principale.date_limite_permis_de_construire.annee
        mois = parameters(period).dicp.impot_foncier.avantages.exoneration_temporaire.habitation_principale.date_limite_permis_de_construire.mois
        jour = parameters(period).dicp.impot_foncier.avantages.exoneration_temporaire.habitation_principale.date_limite_permis_de_construire.jour
        return date(annee, mois, jour)


class date_limite_permis_de_construire_exoneration_temporaire_habitation_principale(Variable):
    value_type = date
    entity = Personne
    definition_period = YEAR
    default_value = date(1970, 1, 1)
    label = "Date à partir de laquelle le permis de construire permet d'obtenir l'exonération de dix ans pour les habitations principale"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2022_12_13(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return personne.pays('date_limite_permis_de_construire_exoneration_temporaire_habitation_principale_pays', period, parameters)


class date_limite_certificat_de_conformite_exoneration_temporaire_habitation_principale_pays(Variable):
    value_type = date
    entity = Pays
    definition_period = YEAR
    default_value = date(1970, 1, 1)
    label = "Date à partir de laquelle le certificat de conformité ne permet plus d'obtenir l'exonération temporaire de dix ans pour les habitations principale"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2022_12_13(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        annee = parameters(period).dicp.impot_foncier.avantages.exoneration_temporaire.habitation_principale.date_limite_certificat_de_conformite.annee
        mois = parameters(period).dicp.impot_foncier.avantages.exoneration_temporaire.habitation_principale.date_limite_certificat_de_conformite.mois
        jour = parameters(period).dicp.impot_foncier.avantages.exoneration_temporaire.habitation_principale.date_limite_certificat_de_conformite.jour
        return date(annee, mois, jour)


class date_limite_certificat_de_conformite_exoneration_temporaire_habitation_principale(Variable):
    value_type = date
    entity = Personne
    definition_period = YEAR
    default_value = date(1970, 1, 1)
    label = "Date à partir de laquelle le certificat de conformité ne permet plus d'obtenir l'exonération temporaire de dix ans pour les habitations principale"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2022_12_13(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return personne.pays('date_limite_certificat_de_conformite_exoneration_temporaire_habitation_principale_pays', period, parameters)


class demande_exoneration_temporaire_habitation_principale(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce que le propriétaire demande l'exoneration temporaraire de dix ans pour les habitations principale pour ce bien"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class date_demande_exoneration_temporaire_habitation_principale(Variable):
    value_type = date
    entity = Personne
    definition_period = YEAR
    default_value = date(1970, 1, 1)
    label = "Date à laquelle le propriétaire à demandé l'exoneration temporaraire de dix ans pour les habitations principale pour ce bien"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class eligible_exoneration_temporaire_habitation_principale(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce que le bien est eligible à une exoneration temporaraire temporaraire de dix ans pour les habitations principale"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2022_12_13(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        age_min = personne.pays('age_min_exoneration_temporaire_habitation_principale_pays', period, parameters)[0]  # identique à toutes les personnes
        age_max = personne.pays('age_max_exoneration_temporaire_habitation_principale_pays', period, parameters)[0]  # identique à toutes les personnes
        terrain = personne('terrain', period, parameters)
        bien_occupe = personne('bien_occupe_avant_la_fin_des_travaux', period, parameters)
        date_pc = personne('date_du_permis_de_construire', period, parameters)
        date_cc = personne('date_du_certificat_de_conformite', period, parameters)
        limit_pc = personne('date_limite_permis_de_construire_exoneration_temporaire_habitation_principale', period, parameters)
        limit_cc = personne('date_limite_certificat_de_conformite_exoneration_temporaire_habitation_principale', period, parameters)
        demande = personne('demande_exoneration_temporaire_habitation_principale', period, parameters)
        date_demande = personne('date_demande_exoneration_temporaire_habitation_principale', period, parameters)
        annee_actuelle = period.start.year

        loue = personne('loue', period, parameters)
        habitation_principale = personne('habitation_principale', period, parameters)
        for i in range(age_min, age_max):
            p = period.offset(-i + 1, 'year')
            loue = loue + personne('loue', p, parameters)
            habitation_principale = habitation_principale * personne('habitation_principale', p, parameters)

        # TODO LA DEMANDE DOIT ÊTRE REALISE DANS UN CERTAIN DÉLAIS
        return not_(terrain) \
            * habitation_principale \
            * not_(bien_occupe) \
            * (limit_pc <= date_pc) * (date_cc <= limit_cc) \
            * demande \
            * (annee_de_la_date(date_demande) < annee_actuelle) \
            * not_(loue)


class exoneration_temporaire_habitation_principale_appliquee(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce que l'exoneration temporaraire temporaraire de dix ans pour les habitations principale s'applique sur ce bien"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    # L'exonération de dix ans ne peut s'applique que si :
    # – Le bien ne bénéficie pas d'une exonération permanente
    # – Le bien est éligible
    # – Son âge est compris dans la période d'application.
    def formula_2022_12_13(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        age_min = personne.pays('age_min_exoneration_temporaire_habitation_principale_pays', period, parameters)[0]  # identique à toutes les personnes
        age_max = personne.pays('age_max_exoneration_temporaire_habitation_principale_pays', period, parameters)[0]  # identique à toutes les personnes
        exoneration_permanente = personne('exoneration_permanente_appliquee', period, parameters)
        eligible = personne('eligible_exoneration_temporaire_habitation_principale', period, parameters)
        age = personne('age_du_bien', period, parameters)
        return not_(exoneration_permanente) \
            * eligible \
            * (age_min <= age <= age_max)


class exoneration_temporaire_habitation_principale_eligible_et_appliquee(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce que le bien est eligible à l'exoneration temporaraire temporaraire de dix ans pour les habitations principale, et est ce que celle-ci s'applique sur ce bien"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2022_12_13(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        eligible = personne('eligible_exoneration_temporaire_habitation_principale', period, parameters)
        appliquee = personne('exoneration_temporaire_habitation_principale_appliquee', period, parameters)
        return eligible * appliquee


class taux_exoneration_temporaire_habitation_principale_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0
    label = "Taux d'exonération temporaraire de dix ans pour cette habitation principale"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2022_12_13(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.impot_foncier.avantages.exoneration_temporaire.habitation_principale.taux  # 1.0


class taux_exoneration_temporaire_habitation_principale(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Taux d'exonération temporaraire de dix ans pour cette habitation principale"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2022_12_13(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return personne.pays('taux_exoneration_temporaire_habitation_principale_pays', period, parameters)


class montant_exoneration_temporaire_habitation_principale(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant de l'exonération temporaraire de dix ans pour cette habitation principale"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2022_12_13(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        eligible_et_appliquee = personne('exoneration_temporaire_habitation_principale_eligible_et_appliquee', period, parameters)
        base = personne('impot_foncier_part_pays_brute', period, parameters)
        taux = personne('taux_exoneration_temporaire_habitation_principale', period, parameters)

        return select(
            [eligible_et_appliquee],
            [arrondi_inferieur(base * taux)],
            0
            )


class duree_restante_exoneration_temporaire_habitation_principale(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Durée restante de l'exonération temporaraire de dix ans pour cette habitation principale"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2022_12_13(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        age_min = personne.pays('age_min_exoneration_temporaire_habitation_principale_pays', period, parameters)
        age_max = personne.pays('age_max_exoneration_temporaire_habitation_principale_pays', period, parameters)
        eligible = personne('eligible_exoneration_temporaire_habitation_principale', period, parameters)
        age = personne('age_du_bien', period, parameters)

        return select(
            [eligible * (age < age_min), eligible * (age_min <= age <= age_max)],
            [age_max - age_min + 1, age_max - age],
            0
            )


# ##################################################
# ###     APPLICATION EXONERATION PERMANENTE     ###
# ##################################################


class eligible_exoneration_temporaire(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce que le bien est eligible à une exonération temporaire"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        eligible_exoneration_temporaire_nouvelle_construction = personne('eligible_exoneration_temporaire_nouvelle_construction', period, parameters)
        eligible_exoneration_temporaire_habitation_principale = personne('eligible_exoneration_temporaire_habitation_principale', period, parameters)
        return eligible_exoneration_temporaire_nouvelle_construction \
            + eligible_exoneration_temporaire_habitation_principale


class exoneration_temporaire_appliquee(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce qu'une exoneration temporaire s'applique au bien"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        exoneration_temporaire_nouvelle_construction_eligible_et_appliquee = personne('exoneration_temporaire_nouvelle_construction_eligible_et_appliquee', period, parameters)
        exoneration_temporaire_habitation_principale_eligible_et_appliquee = personne('exoneration_temporaire_habitation_principale_eligible_et_appliquee', period, parameters)
        return exoneration_temporaire_nouvelle_construction_eligible_et_appliquee \
            + exoneration_temporaire_habitation_principale_eligible_et_appliquee


class montant_exoneration_temporaire(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant d'exonération permanente"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        montant_exoneration_temporaire_nouvelle_construction = personne('montant_exoneration_temporaire_nouvelle_construction', period, parameters)
        montant_exoneration_temporaire_habitation_principale = personne('montant_exoneration_temporaire_habitation_principale', period, parameters)
        return montant_exoneration_temporaire_nouvelle_construction \
            + montant_exoneration_temporaire_habitation_principale
