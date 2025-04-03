# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.base import (
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
