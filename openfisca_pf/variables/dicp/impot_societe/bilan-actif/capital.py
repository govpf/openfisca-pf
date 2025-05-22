# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.base import (
    ArrayLike,
    ParameterNode,
    Period,
    Population,
    Variable,
    YEAR
    )
from openfisca_pf.entities import Personne


class is_bilan_actif_capital_souscrit_non_appele_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Capital souscrit non appelé brut (AA)"


class is_bilan_actif_capital_souscrit_non_appele_net(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Capital souscrit non appelé net"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
       captial_souscrit_non_appele_brut = personne('is_bilan_actif_capital_souscrit_non_appele_brut', period)
       return captial_souscrit_non_appele_brut
