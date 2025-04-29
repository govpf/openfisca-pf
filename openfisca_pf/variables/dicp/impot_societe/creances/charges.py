# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.base import (
    Variable,
    DAY
    )
from openfisca_pf.entities import Personne


class is_creances_charges_constatees_d_avance_montant_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Charges constatées d'avance montant brut (7W)"


class is_creances_charges_constatees_d_avance_a_un_an_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Charges constatées d'avance à un an au plus (7W)"


class is_creances_charges_constatees_d_avance_a_plus_d_un_an(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Charges constatées d'avance à plus d'un an (7W)"