# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.base import (
    Variable,
    YEAR
    )
from openfisca_pf.entities import Personne


class is_bilan_passif_ecart_de_reevaluation_incorpore_au_capital(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Ecart de réévaluation incorporé au capital (1B)"


class is_bilan_passif_dont_ecart_de_reevaluation_libre(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Dont écart de réévaluation libre (1D)"


class is_bilan_passif_dettes_et_produits_constate_avance_a_moins_un_an(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Dettes et produits constatés d'avance à moins d'un an (EG)"


class is_bilan_passif_dont_concours_bancaires_courant_et_soldes_crediteurs_de_banques_et_ccp(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Dont concours bancaires courants et soldes créditeurs de banques et CCP (EH)"
