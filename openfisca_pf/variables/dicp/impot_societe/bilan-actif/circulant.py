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


# Stocks
class is_bilan_actif_stocks_matieres_premieres_approvisionnements_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Stocks, matières premières, approvisionnements brut (BL)"


class is_bilan_actif_stocks_matieres_premieres_approvisionnements_amortissements_provisions(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Stocks, matières premières, approvisionnements amortissements et provisions (BM)"


class is_bilan_actif_stocks_matieres_premieres_approvisionnements_net(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Stocks, matières premières, approvisionnements net"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        stock_brut = personne('is_bilan_actif_stocks_matieres_premieres_approvisionnements_brut', period)
        stock_amortissement_provision = personne('is_bilan_actif_stocks_matieres_premieres_approvisionnements_amortissements_provisions', period)
        return stock_brut - stock_amortissement_provision


class is_bilan_actif_stocks_en_cours_production_biens_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Stocks en cours de production de biens brut (BN)"


class is_bilan_actif_stocks_en_cours_production_biens_amortissements_provisions(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Stocks en cours de production de biens amortissements et provisions (BO)"


class is_bilan_actif_stocks_en_cours_production_biens_net(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Stocks en cours de production de biens net"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        stock_en_cours_brut = personne('is_bilan_actif_stocks_en_cours_production_biens_brut', period)
        stock_en_cours_amortissement_provision = personne('is_bilan_actif_stocks_en_cours_production_biens_amortissements_provisions', period)
        return stock_en_cours_brut - stock_en_cours_amortissement_provision


class is_bilan_actif_stocks_en_cours_production_services_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Stocks en cours de production de services brut (BP)"


class is_bilan_actif_stocks_en_cours_production_services_amortissements_provisions(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Stocks en cours de production de services amortissements et provisions (BQ)"


class is_bilan_actif_stocks_en_cours_production_services_net(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Stocks en cours de production de services net"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        stock_en_cours_production_brut = personne('is_bilan_actif_stocks_en_cours_production_services_brut', period)
        stock_en_cours_production_amortissement_provision = personne('is_bilan_actif_stocks_en_cours_production_services_amortissements_provisions', period)
        return stock_en_cours_production_brut - stock_en_cours_production_amortissement_provision


class is_bilan_actif_stocks_produits_intermediaires_finis_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Stocks, produits intermédiaires et finis brut (BR)"


class is_bilan_actif_stocks_produits_intermediaires_finis_amortissements_provisions(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Stocks, produits intermédiaires et finis amortissements et provisions (BS)"


class is_bilan_actif_stocks_produits_intermediaires_finis_net(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Stocks, produits intermédiaires et finis net"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        stock_produits_intermediaires_finis_brut = personne('is_bilan_actif_stocks_produits_intermediaires_finis_brut', period)
        stock_produits_intermediaires_finis_amortissement_provision = personne('is_bilan_actif_stocks_produits_intermediaires_finis_amortissements_provisions', period)
        return stock_produits_intermediaires_finis_brut - stock_produits_intermediaires_finis_amortissement_provision


class is_bilan_actif_stocks_marchandises_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Stocks, marchandises brut (BT)"


class is_bilan_actif_stocks_marchandises_amortissements_provisions(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Stocks, marchandises amortissements et provisions (BU)"


class is_bilan_actif_stocks_marchandises_net(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Stocks, marchandises net"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        stock_marchandises_brut = personne('is_bilan_actif_stocks_marchandises_brut', period)
        stock_marchandises_amortissement_provision = personne('is_bilan_actif_stocks_marchandises_amortissements_provisions', period)
        return stock_marchandises_brut - stock_marchandises_amortissement_provision


class is_bilan_actif_avances_acomptes_verses_commandes_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Avances et acomptes versés sur commandes brut (BV)"


class is_bilan_actif_avances_acomptes_verses_commandes_amortissements_provisions(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Avances et acomptes versés sur commandes amortissements et provisions (BW)"


class is_bilan_actif_avances_acomptes_verses_commandes_net(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Avances et acomptes versés sur commandes net"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        avances_acomptes_verses_brut = personne('is_bilan_actif_avances_acomptes_verses_commandes_brut', period)
        avances_acomptes_verses_amortissement_provision = personne('is_bilan_actif_avances_acomptes_verses_commandes_amortissements_provisions', period)
        return avances_acomptes_verses_brut - avances_acomptes_verses_amortissement_provision


# Creances
class is_bilan_actif_creances_clients_comptes_rattaches_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Créances clients et comptes rattachés brut (BX)"


class is_bilan_actif_creances_clients_comptes_rattaches_amortissements_provisions(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Créances clients et comptes rattachés amortissements et provisions (BY)"


class is_bilan_actif_creances_clients_comptes_rattaches_net(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Créances clients et comptes rattachés net"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        creances_clients_brut = personne('is_bilan_actif_creances_clients_comptes_rattaches_brut', period)
        creances_clients_amortissement_provision = personne('is_bilan_actif_creances_clients_comptes_rattaches_amortissements_provisions', period)
        return creances_clients_brut - creances_clients_amortissement_provision


class is_bilan_actif_creances_autres_creances_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Autres créances brut (BZ)"


class is_bilan_actif_creances_autres_creances_amortissements_provisions(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Autres créances amortissements et provisions (CA)"


class is_bilan_actif_creances_autres_creances_net(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Autres créances net"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        autres_creances_brut = personne('is_bilan_actif_creances_autres_creances_brut', period)
        autres_creances_amortissement_provision = personne('is_bilan_actif_creances_autres_creances_amortissements_provisions', period)
        return autres_creances_brut - autres_creances_amortissement_provision


class is_bilan_actif_creances_capital_souscrit_appele_non_verse_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Créances sur le capital souscrit et appelé, non versé brut (CB)"


class is_bilan_actif_creances_capital_souscrit_appele_non_verse_amortissements_provisions(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Créances sur le capital souscrit et appelé, non versé amortissements et provisions (CC)"


class is_bilan_actif_creances_capital_souscrit_appele_non_verse_net(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Créances sur le capital souscrit et appelé, non versé net"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        creances_capital_souscrit_brut = personne('is_bilan_actif_creances_capital_souscrit_appele_non_verse_brut', period)
        creances_capital_souscrit_amortissement_provision = personne('is_bilan_actif_creances_capital_souscrit_appele_non_verse_amortissements_provisions', period)
        return creances_capital_souscrit_brut - creances_capital_souscrit_amortissement_provision


# Divers
class is_bilan_actif_divers_disponibilites_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Divers, disponibilités brut (CF)"


class is_bilan_actif_divers_disponibilites_amortissements_provisions(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Divers, disponibilités amortissements et provisions (CG)"


class is_bilan_actif_divers_disponibilites_net(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Divers, disponibilités net"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        divers_disponibilites_brut = personne('is_bilan_actif_divers_disponibilites_brut', period)
        divers_disponibilites_amortissement_provision = personne('is_bilan_actif_divers_disponibilites_amortissements_provisions', period)
        return divers_disponibilites_brut - divers_disponibilites_amortissement_provision
