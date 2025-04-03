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

class is_bilan_actif_comptes_regularation_charges_constatees_avance_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Comptes de régularisation des charges constatées d'avance brut (CH)"

class is_bilan_actif_comptes_regularation_charges_constatees_avance_amortissements_provisions(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Comptes de régularisation des charges constatées d'avance amortissements, provisions (CI)"

class is_bilan_actif_comptes_regularation_charges_repartir_plusieurs_exercices_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Comptes de régularisation des charges à répartir sur plusieurs exercices brut (CL)"

