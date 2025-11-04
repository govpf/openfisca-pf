# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.base import (ArrayLike, Period, DAY, Enum, max_, Variable, where, ParameterNode, Population)
from openfisca_pf.entities import Personne
from openfisca_pf.enums.impot_societe.impot_type import ImpotType


class impot_brut_due_retenu_type(Variable):
    value_type = Enum
    possible_values = ImpotType
    entity = Personne
    definition_period = DAY
    default_value = ImpotType.IS
    label = "Type de l'impot brut retenu"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        is_due = personne('is_brut_due', period)
        imf_due = personne('imf_brut_due', period)
        return where(is_due >= imf_due, ImpotType.IS, ImpotType.IMF)


class impot_brut_due_retenu(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Montant de l'impot brut retenu"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        is_due = personne('is_brut_due', period)
        imf_due = personne('imf_brut_due', period)
        return max_(is_due, imf_due)
