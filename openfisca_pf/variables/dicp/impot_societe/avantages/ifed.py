from typing import Union, Optional

from openfisca_core.types import Instant, Formula

from openfisca_pf.base import (
    ArrayLike,
    DAY,
    ParameterNode,
    Period,
    Population,
    Variable,
)
from openfisca_pf.entities import Personne

class is_avantage_ifed_valeur_augmentation(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    unit = 'currency-XFP'
    label = "Valeur d'augmentation FCFP"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.impot_societe.avantages.ifed.valeur_augmentation

class is_avantage_ifed_libelle(Variable):
    value_type = str
    entity = Personne
    definition_period = DAY
    label = "Libellé"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.impot_societe.avantages.ifed.libelle[0]

class is_avantage_ifed_duree(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Durée de l'avantage en année"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.impot_societe.avantages.ifed.duree

class is_avantage_ifed_taux_plafond(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Taux plafond"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.impot_societe.avantages.ifed.taux_plafond

class is_avantage_ifed_jour_exercice_imputation(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Jour exercice imputation"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.impot_societe.avantages.ifed.jour_exercice_imputation

class is_avantage_ifed_mois_exercice_imputation(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Mois exercice imputation"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.impot_societe.avantages.ifed.mois_exercice_imputation




