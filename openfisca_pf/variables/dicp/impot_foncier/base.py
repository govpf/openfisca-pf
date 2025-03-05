# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    Parameters,
    Period,
    Variable,
    where,
    YEAR
)
from openfisca_pf.entities import Personne


class base_imposable_apres_exoneration_temporaire_huit_ans(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Base imposable intermédiaire après application de l'exonération temporaire pour les nouvelles constructions"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        age_du_bien = personne('age_du_bien', period, parameters)
        valeur_locative_brute = personne('valeur_locative_brute', period, parameters)
        eligible = personne('eligible_exoneration_temporaire_nouvelle_construction_huit_ans', period, parameters)
        age_intermediare = personne('age_intermediare_exoneration_temporaire_nouvelle_construction_huit_ans', period, parameters)
        age_max = personne('age_max_exoneration_temporaire_nouvelle_construction_huit_ans', period, parameters)
        taux = personne('taux_exoneration_temporaire_nouvelle_construction_huit_ans', period, parameters)
        return where(
            eligible * (age_intermediare <= age_du_bien <= age_max),
            valeur_locative_brute * (1.0 - taux),
            valeur_locative_brute
            )
