from openfisca_pf.base import (
    ArrayLike,
    DAY,
    ParameterNode,
    Period,
    Population,
    Variable,
    )
from openfisca_pf.entities import Personne


class is_activation(Variable):
    value_type = bool
    entity = Personne
    definition_period = DAY
    label = "Activation IS"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.impot_societe.activation
