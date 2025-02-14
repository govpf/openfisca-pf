# -*- coding: utf-8 -*-

from openfisca_pf.base import (
    ArrayLike,
    Enum,
    not_,
    OuiNon,
    Parameters,
    Period,
    TypeSociete,
    Variable,
    YEAR
    )
from openfisca_pf.entities import Pays, Personne


class option_is(Variable):
    value_type = Enum
    entity = Personne
    possible_values = OuiNon
    default_value = OuiNon.N
    definition_period = YEAR
    label = "Défini si l'entreprise à opté pour l'impôt sur les sociétés plutot que l'impôt sur les transactions (applicable aux Société en Nom Collectif)"
    reference = []


class option_is_possible(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    label = "Indique que l'entreprise peut opter pour l'impôt sur les sociétés plutot que l'impôt sur les transactions"
    reference = []

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        type_societe = personne('type_societe', period, parameters)
        return (type_societe == TypeSociete.SNC)


class redevable_is(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    label = "Défini si l'entreprise est éligible à l'impôt sur les sociétés"
    reference = []

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        redevable_tpe = personne('redevable_tpe', period, parameters)
        redevable_it = personne('redevable_it', period, parameters)
        return not_(redevable_tpe + redevable_it)


class nombre_entreprises_redevables_is_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = "Nombre d'entreprises du pays redevable de l'impôt sur les sociétés"
    reference = []

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        redevable_is = pays.members('redevable_is', period, parameters)
        return pays.sum(redevable_is * 1)
