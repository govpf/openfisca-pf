# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    Parameters,
    Period,
    Variable,
    YEAR
    )
from openfisca_pf.entities import Personne


class impot_foncier_part_pays_apres_exonerations_permanentes(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant de la part pays de l'impôt foncier après déduction des exonérations permanentes"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        brute = personne('impot_foncier_part_pays_brute', period, parameters)
        montant = personne('montant_exoneration_permanente_bien_public', period, parameters)
        return brute - montant
