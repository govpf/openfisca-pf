# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.base import (
    ArrayLike,
    DAY,
    isin,
    ParameterNode,
    Period,
    Population,
    Variable,
    )
from openfisca_pf.entities import Personne
from openfisca_pf.enums.impot_societe.activity import (
    ACTIVITE_REDUCTION_CSIS,
    ACTIVITE_REDUCTION_TAUX_A_SAISIR_CSIS
    )


class csis_net_possede_reduction(Variable):
    value_type = bool
    entity = Personne
    definition_period = DAY
    default_value = False
    label = "Activité possède une réduction CSIS ?"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        activite_principale = personne('is_activite_principale', period, parameters)
        return isin(activite_principale, ACTIVITE_REDUCTION_CSIS)


class csis_net_reduction_taux_est_a_saisir(Variable):
    value_type = bool
    entity = Personne
    definition_period = DAY
    label = "Taux Reduction CSIS doit être saisie"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        activite_principale = personne('is_activite_principale', period, parameters)
        return isin(activite_principale, ACTIVITE_REDUCTION_TAUX_A_SAISIR_CSIS)
