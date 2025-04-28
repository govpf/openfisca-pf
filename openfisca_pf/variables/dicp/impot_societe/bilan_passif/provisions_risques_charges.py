# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.base import (
    Variable,
    YEAR
)
from openfisca_pf.entities import Personne


class is_bilan_passif_provisions_pour_risques(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provisions pour risques (DP)"


class is_bilan_passif_provisions_pour_charges(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provisions pour charges (DP)"
