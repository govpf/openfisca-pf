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


class is_avantage_ifed_duree(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Durée de l'avantage en année"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.impot_societe.avantages.ifed.duree


class is_avantage_ifed_multiple(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Multiple de la somme de l'avantage"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        augmentation = parameters(period).dicp.impot_societe.avantages.ifed.valeur_augmentation
        duree = parameters(period).dicp.impot_societe.avantages.ifed.duree
        return augmentation / duree

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

