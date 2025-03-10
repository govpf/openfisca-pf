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
from openfisca_pf.entities import Personne
from openfisca_pf.functions.currency import arrondi_inferieur


# ##################################################
# ###  CINQ ANS POUR LES NOUVELLES CONSTRUCTIONS ###
# ##################################################


AGE_MIN_EXONERATION_TEMPORAIRE_NOUVELLE_CONSTRUCTION: int = 1
AGE_MAX_EXONERATION_TEMPORAIRE_NOUVELLE_CONSTRUCTION: int = 5


class age_min_exoneration_temporaire_nouvelle_construction(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Age minimum pour qu'une nouvelle construction soit eligible à une exonération temporaraire de cinq ans pour les nouvelles constructions [lecture seule]"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return AGE_MIN_EXONERATION_TEMPORAIRE_NOUVELLE_CONSTRUCTION


class age_max_exoneration_temporaire_nouvelle_construction(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Age maximum pour qu'une nouvelle construction soit eligible à une exonération temporaraire de cinq ans pour les nouvelles constructions [lecture seule]"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return AGE_MAX_EXONERATION_TEMPORAIRE_NOUVELLE_CONSTRUCTION


class eligible_exoneration_temporaire_nouvelle_construction(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce que le bien est eligible à une exoneration temporaraire de cinq ans pour les nouvelles constructions"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        terrain = personne('terrain', period, parameters)
        age_du_bien = personne('age_du_bien', period, parameters)
        return not_(terrain) * (AGE_MIN_EXONERATION_TEMPORAIRE_NOUVELLE_CONSTRUCTION <= age_du_bien <= AGE_MAX_EXONERATION_TEMPORAIRE_NOUVELLE_CONSTRUCTION)


class taux_exoneration_temporaire_nouvelle_construction(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Taux d'exonération temporaraire de cinq ans pour les nouvelles constructions"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.impot_foncier.avantages.exoneration_temporaire.nouvelle_construction.taux


class montant_exoneration_temporaire_nouvelle_construction(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant de l'exonération temporaraire de cinq ans pour les nouvelles constructions"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        eligible = personne('eligible_exoneration_temporaire_nouvelle_construction', period, parameters)
        base = personne('impot_foncier_part_pays_brute', period, parameters)
        taux = personne('taux_exoneration_temporaire_nouvelle_construction', period, parameters)
        return select(
            [eligible],
            [arrondi_inferieur(base * taux)],
            0
            )


# ##################################################
# ###  DIX ANS POUR LES HABITATIONS PRINCIPALES  ###
# ##################################################


AGE_MIN_EXONERATION_TEMPORAIRE_HABITATION_PRINCIPALE: int = 1
AGE_MAX_EXONERATION_TEMPORAIRE_HABITATION_PRINCIPALE: int = 10


class age_min_exoneration_temporaire_habitation_principale(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Age minimum pour qu'une habitation principale soit eligible à l'exonération temporaire de dix ans [lecture seule]"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2022_12_13(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return AGE_MIN_EXONERATION_TEMPORAIRE_HABITATION_PRINCIPALE


class age_max_exoneration_temporaire_habitation_principale(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Age maximum pour qu'une habitation principale soit eligible à l'exonération temporaire de dix ans [lecture seule]"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2022_12_13(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return AGE_MAX_EXONERATION_TEMPORAIRE_HABITATION_PRINCIPALE


class date_limite_permis_de_construire_exoneration_temporaire_habitation_principale(Variable):
    value_type = date
    entity = Personne
    definition_period = YEAR
    default_value = date(1970, 1, 1)
    label = "Date à partir de laquelle le permis de construire permet d'obtenir l'exonération de dix ans pour les habitations principale"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2022_12_13(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        annee = parameters(period).dicp.impot_foncier.avantages.exoneration_temporaire.habitation_principale.date_limite_permis_de_construire.annee
        mois = parameters(period).dicp.impot_foncier.avantages.exoneration_temporaire.habitation_principale.date_limite_permis_de_construire.mois
        jour = parameters(period).dicp.impot_foncier.avantages.exoneration_temporaire.habitation_principale.date_limite_permis_de_construire.jour
        return date(annee, mois, jour)


class date_limite_certificat_de_conformite_exoneration_temporaire_habitation_principale(Variable):
    value_type = date
    entity = Personne
    definition_period = YEAR
    default_value = date(1970, 1, 1)
    label = "Date à partir de laquelle le certificat de construire ne permet plus d'obtenir l'exonération temporaire de dix ans pour les habitations principale"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2022_12_13(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        annee = parameters(period).dicp.impot_foncier.avantages.exoneration_temporaire.habitation_principale.date_limite_certificat_de_conformite.annee
        mois = parameters(period).dicp.impot_foncier.avantages.exoneration_temporaire.habitation_principale.date_limite_certificat_de_conformite.mois
        jour = parameters(period).dicp.impot_foncier.avantages.exoneration_temporaire.habitation_principale.date_limite_certificat_de_conformite.jour
        return date(annee, mois, jour)


class eligible_exoneration_temporaire_habitation_principale(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce que le bien est eligible à une exoneration temporaraire temporaraire de dix ans pour les habitations principale"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2022_12_13(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        terrain = personne('terrain', period, parameters)
        age = personne('age_du_bien', period, parameters)
        habitation_principale = personne('habitation_principale', period, parameters)
        bien_occupe = personne('bien_occupe_avant_la_fin_des_travaux', period, parameters)
        date_pc = personne('date_du_permis_de_construire', period, parameters)
        limit_pc = personne('date_limite_permis_de_construire_exoneration_temporaire_habitation_principale', period, parameters)
        date_cc = personne('date_du_certificat_de_conformite', period, parameters)
        limit_cc = personne('date_limite_certificat_de_conformite_exoneration_temporaire_habitation_principale', period, parameters)

        return not_(terrain) \
            * habitation_principale \
            * not_(bien_occupe) \
            * (AGE_MIN_EXONERATION_TEMPORAIRE_HABITATION_PRINCIPALE <= age <= AGE_MAX_EXONERATION_TEMPORAIRE_HABITATION_PRINCIPALE) \
            * (limit_pc <= date_pc) * (date_cc <= limit_cc) \
            * not_(personne('loue', period.offset(-0, 'year'), parameters)) \
            * not_(personne('loue', period.offset(-1, 'year'), parameters)) \
            * not_(personne('loue', period.offset(-2, 'year'), parameters)) \
            * not_(personne('loue', period.offset(-3, 'year'), parameters)) \
            * not_(personne('loue', period.offset(-4, 'year'), parameters)) \
            * not_(personne('loue', period.offset(-5, 'year'), parameters)) \
            * not_(personne('loue', period.offset(-6, 'year'), parameters)) \
            * not_(personne('loue', period.offset(-7, 'year'), parameters)) \
            * not_(personne('loue', period.offset(-8, 'year'), parameters)) \
            * not_(personne('loue', period.offset(-9, 'year'), parameters))


class taux_exoneration_temporaire_habitation_principale(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Taux d'exonération temporaraire pour les nouvelles constructions en fonction de l'age du bien"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2022_12_13(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.impot_foncier.avantages.exoneration_temporaire.habitation_principale.taux


class montant_exoneration_temporaire_habitation_principale(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant de l'exonération temporaraire de cinq ans pour les nouvelles constructions"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2022_12_13(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        base = personne('impot_foncier_part_pays_brute', period, parameters)
        taux = personne('taux_exoneration_temporaire_habitation_principale', period, parameters)
        return arrondi_inferieur(base * taux)
