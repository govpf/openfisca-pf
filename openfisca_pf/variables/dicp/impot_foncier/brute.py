# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    GroupPopulation,
    ParameterNode,
    Period,
    Population,
    Variable,
    YEAR
    )
from openfisca_pf.entities import Pays, Personne
from openfisca_pf.functions.currency import arrondi_inferieur


class taux_part_pays_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0.
    label = "Taux utilisé pour calculer l'impot brut de l'impôt foncier revenant au pays"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(pays: GroupPopulation, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.impot_foncier.brute.taux  # 0.1


class taux_part_pays(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.
    label = "Taux utilisé pour calculer l'impot brut de l'impôt foncier revenant au pays"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return personne.pays('taux_part_pays_pays', period)  # 0.1


class impot_foncier_part_pays_brute(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant d'impôt foncier brute revenant au pays"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        base = personne('valeur_locative_nette', period)
        taux = personne('taux_part_pays', period)  # 0.1
        return arrondi_inferieur(base * taux)
