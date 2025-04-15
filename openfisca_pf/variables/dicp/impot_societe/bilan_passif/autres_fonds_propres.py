# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.base import (
    Variable,
    YEAR
    )
from openfisca_pf.entities import Personne

class is_bilan_passif_avances_conditionnees(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Avances conditionnées (DN)"