# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.base import (
    ArrayLike,
    DAY,
    ParameterNode,
    Period,
    Population,
    Variable
    )
from openfisca_pf.entities import Personne


# Produits
class is_resultat_exceptionnel_produits_gestion(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Produits exceptionnels sur opérations de gestion (HA)"


class is_resultat_exceptionnel_produits_capital(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Produits exceptionnels sur opérations en capital (HB)"


class is_resultat_exceptionnel_reprises_provisions_transfert_charges(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Reprises sur provisions et transfert de charges (HC)"


class is_resultat_exceptionnel_total_produits(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Total des produits exceptionnels (HD)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        gestion = personne('is_resultat_exceptionnel_produits_gestion', period)
        capital = personne('is_resultat_exceptionnel_produits_capital', period)
        transfert = personne('is_resultat_exceptionnel_reprises_provisions_transfert_charges', period)
        return gestion + capital + transfert


# Charges
class is_resultat_exceptionnel_charges_gestion(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Charges exceptionnelles sur opérations de gestion (HE)"


class is_resultat_exceptionnel_charges_capital(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Charges exceptionnelles sur opérations en capital (HF)"


class is_resultat_exceptionnel_dotations_ammortissements_provisions(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dotations exceptionnelles aux amortissements et provisions (HG)"


class is_resultat_exceptionnel_total_charges(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Total des charges exceptionnels (HH)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        gestion = personne('is_resultat_exceptionnel_charges_gestion', period)
        capital = personne('is_resultat_exceptionnel_charges_capital', period)
        dotation = personne('is_resultat_exceptionnel_dotations_ammortissements_provisions', period)
        return gestion + capital + dotation


# Résultat
class is_resultat_exceptionnel(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Résultat Exceptionnel (HI)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        produits = personne('is_resultat_exceptionnel_total_produits', period)
        charges = personne('is_resultat_exceptionnel_total_charges', period)
        return produits - charges
