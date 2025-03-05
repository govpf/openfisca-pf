# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    not_,
    Parameters,
    Period,
    Variable,
    YEAR
)
from openfisca_pf.entities import Personne


class age_min_exoneration_temporaire_nouvelle_construction_huit_ans(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Age minimum pour qu'une nouvelle construction soit eligible à une exonération pour les nouvelles constructions"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.impot_foncier.avantages.exoneration_temporaire.nouvelle_construction_huit_ans.age_min


class age_intermediare_exoneration_temporaire_nouvelle_construction_huit_ans(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Age intermediare a partir duquel le taux d'exoneration nouvelle construction passe de 1 à 0.5"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.impot_foncier.avantages.exoneration_temporaire.nouvelle_construction_huit_ans.age_intermediaire


class age_max_exoneration_temporaire_nouvelle_construction_huit_ans(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Age maximum pour qu'une nouvelle construction soit eligible à une exonération pour les nouvelles constructions"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.impot_foncier.avantages.exoneration_temporaire.nouvelle_construction_huit_ans.age_max


class eligible_exoneration_temporaire_nouvelle_construction_huit_ans(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Taux de l'exonération temporaire pour les nouvelles constructions"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        terrain = personne('terrain', period, parameters)
        age_du_bien = personne('age_du_bien', period, parameters)
        age_min = personne('age_min_exoneration_temporaire_nouvelle_construction_huit_ans', period, parameters)
        age_max = personne('age_max_exoneration_temporaire_nouvelle_construction_huit_ans', period, parameters)
        return not_(terrain) * (age_min <= age_du_bien <= age_max)


class taux_exoneration_temporaire_nouvelle_construction_huit_ans(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Taux de l'exonération temporaire pour les nouvelles constructions"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        age_du_bien = personne('age_du_bien', period, parameters)
        taux = parameters(period).dicp.impot_foncier.avantages.exoneration_temporaire.nouvelle_construction_huit_ans.taux
        return taux.calc(age_du_bien)
