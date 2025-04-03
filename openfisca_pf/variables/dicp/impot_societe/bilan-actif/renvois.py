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


class is_bilan_actif_renvois_dont_droit_bail(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Renvois dont droit au bail"


class is_bilan_actif_renvois_part_moins_un_an_immobilisations_financieres_nettes(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Renvois part à moins d'un an des immobilisations financières nettes"


class is_bilan_actif_renvois_part_plus_un_an(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Renvois part à plus d'un an"
