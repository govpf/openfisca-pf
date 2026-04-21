from openfisca_pf.base import (
    ArrayLike,
    DAY,
    ParameterNode,
    Period,
    Population,
    Variable,
    )
from openfisca_pf.entities import Personne


class is_avantage_sisae_montant(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    unit = 'currency-XFP'
    label = "Montant attestation SISAE en FCFP"


class is_avantage_sisae_taux_exoneration(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Taux d'exonération"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.impot_societe.avantages.sisae.taux_exoneration


class is_avantage_sisae_credit_ouvert(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    unit = 'currency-XFP'
    label = "Crédit ouvert attestation SISAE en FCFP"

    def formula(personne: Population, period: Period) -> ArrayLike:
        taux_exoneration = personne('is_avantage_sisae_taux_exoneration', period)
        montant = personne('is_avantage_sisae_montant', period)
        return montant * taux_exoneration
