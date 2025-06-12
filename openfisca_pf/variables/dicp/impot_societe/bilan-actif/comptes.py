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


class is_bilan_actif_comptes_regularation_charges_constatees_avance_net(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Comptes de régularisation des charges constatées d'avance net"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        charges_constate_brut = personne('is_bilan_actif_comptes_regularation_charges_constatees_avance_brut', period)
        charges_constate_amortissement_provsion = personne('is_bilan_actif_comptes_regularation_charges_constatees_avance_amortissements_provisions', period)
        return charges_constate_brut - charges_constate_amortissement_provsion


class is_bilan_actif_comptes_regularation_charges_repartir_plusieurs_exercices_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Comptes de régularisation des charges à répartir sur plusieurs exercices brut (CL)"


class is_bilan_actif_comptes_regularation_charges_repartir_plusieurs_exercices_net(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Comptes de régularisation des charges à répartir sur plusieurs exercices net"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        charges_repartir_brut = personne('is_bilan_actif_comptes_regularation_charges_repartir_plusieurs_exercices_brut', period)
        return charges_repartir_brut
