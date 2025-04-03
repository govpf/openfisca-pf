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


class is_bilan_actif_total_actif_immobilise_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Bilan actif, total des actifs immobilisés bruts (BJ)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        immo_incorporelles_frais_etablissement = personne('is_bilan_actif_immobilisation_incorporelles_frais_etablissement_brut', period)
        immo_incorporelles_fonds_commercial = personne('is_bilan_actif_immobilisation_incorporelles_fonds_commercial_brut', period)
        immo_incorporelles_autres = personne('is_bilan_actif_immobilisation_incorporelles_autres_immobilisations_incorporelles_brut', period)
        immo_corporelle_terrains = personne("is_bilan_actif_immobilisation_corporelles_terrains_brut", period)
        immo_corporelle_constructions = personne("is_bilan_actif_immobilisation_corporelles_constructions_brut", period)
        immo_corporelle_installations_techniques = personne("is_bilan_actif_immobilisation_corporelles_installations_techniques_materiel_outillage_industriel_brut", period)
        immo_corporelle_autres = personne("is_bilan_actif_immobilisation_corporelles_autres_immobilisations_corporelles_brut", period)
        immo_corporelle_en_cours = personne("is_bilan_actif_immobilisation_corporelles_immobilisations_en_cours_brut", period)
        immo_financieres_participations = personne("is_bilan_actif_immobilisation_financieres_participations_brut", period)
        immo_financieres_creance_rattache = personne("is_bilan_actif_immobilisation_financieres_creance_rattachees_participations_brut", period)
        immo_financieres_autres = personne("is_bilan_actif_immobilisation_financieres_autres_titres_immobilises_brut", period)
        return immo_incorporelles_frais_etablissement + immo_incorporelles_fonds_commercial + immo_incorporelles_autres + immo_corporelle_terrains + immo_corporelle_constructions + immo_corporelle_installations_techniques + immo_corporelle_autres + immo_corporelle_en_cours + immo_financieres_participations + immo_financieres_creance_rattache + immo_financieres_autres

class is_bilan_actif_total_actif_immobilise_amortissements_provisions(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Bilan actif, total des actifs immobilisés amortissements et provisions (BK)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        immo_incorporelles_frais_etablissement = personne('is_bilan_actif_immobilisation_incorporelles_frais_etablissement_amortissements_provisions', period)
        immo_incorporelles_fonds_commercial = personne('is_bilan_actif_immobilisation_incorporelles_fonds_commercial_amortissements_provisions', period)
        immo_incorporelles_autres = personne('is_bilan_actif_immobilisation_incorporelles_autres_immobilisations_incorporelles_amortissements_provisions', period)
        immo_corporelle_terrains = personne("is_bilan_actif_immobilisation_corporelles_terrains_amortissements_provisions", period)
        immo_corporelle_constructions = personne("is_bilan_actif_immobilisation_corporelles_constructions_amortissements_provisions", period)
        immo_corporelle_installations_techniques = personne("is_bilan_actif_immobilisation_corporelles_installations_techniques_materiel_outillage_industriel_amortissements_provisions", period)
        immo_corporelle_autres = personne("is_bilan_actif_immobilisation_corporelles_autres_immobilisations_corporelles_amortissements_provisions", period)
        immo_corporelle_en_cours = personne("is_bilan_actif_immobilisation_corporelles_immobilisations_en_cours_amortissements_provisions", period)
        immo_financieres_participations = personne("is_bilan_actif_immobilisation_financieres_participations_amortissements_provisions", period)
        immo_financieres_creance_rattache = personne("is_bilan_actif_immobilisation_financieres_creance_rattachees_participations_amortissements_provisions", period)
        immo_financieres_autres = personne("is_bilan_actif_immobilisation_financieres_autres_titres_immobilises_amortissements_provisions", period)
        return immo_incorporelles_frais_etablissement + immo_incorporelles_fonds_commercial + immo_incorporelles_autres + immo_corporelle_terrains + immo_corporelle_constructions + immo_corporelle_installations_techniques + immo_corporelle_autres + immo_corporelle_en_cours + immo_financieres_participations + immo_financieres_creance_rattache + immo_financieres_autres

class is_bilan_actif_total_actif_circulant_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Bilan actif, total des actifs circulants bruts (CJ)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        stock = personne('is_bilan_actif_stocks_matieres_premieres_approvisionnements_brut', period)
        en_cous_production_biens = personne('is_bilan_actif_stocks_en_cours_production_biens_brut', period)
        en_cous_production_services = personne('is_bilan_actif_stocks_en_cours_production_services_brut', period)
        produits_intermediaires = personne('is_bilan_actif_stocks_produits_intermediaires_finis_brut', period)
        marchandises = personne('is_bilan_actif_stocks_marchandises_brut', period)
        avances_et_acomptes = personne('is_bilan_actif_avances_acomptes_verses_commandes_brut', period)
        comptes_rattaches = personne('is_bilan_actif_creances_clients_comptes_rattaches_brut', period)
        autres_creances = personne('is_bilan_actif_creances_autres_creances_brut', period)
        capital_souscrit = personne('is_bilan_actif_creances_capital_souscrit_appele_non_verse_brut', period)
        disponibilites = personne('is_bilan_actif_divers_disponibilites_brut', period)
        charges_constatees_avance = personne('is_bilan_actif_comptes_regularation_charges_constatees_avance_brut', period)
        return stock + en_cous_production_biens + en_cous_production_services + produits_intermediaires + marchandises + avances_et_acomptes + comptes_rattaches + autres_creances + capital_souscrit + disponibilites + charges_constatees_avance

class is_bilan_actif_total_actif_circulant_amortissements_provisions(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Bilan actif, total des actifs circulants amortissements et provisions (CK)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        stock = personne('is_bilan_actif_stocks_matieres_premieres_approvisionnements_amortissements_provisions', period)
        en_cous_production_biens = personne('is_bilan_actif_stocks_en_cours_production_biens_amortissements_provisions', period)
        en_cous_production_services = personne('is_bilan_actif_stocks_en_cours_production_services_amortissements_provisions', period)
        produits_intermediaires = personne('is_bilan_actif_stocks_produits_intermediaires_finis_amortissements_provisions', period)
        marchandises = personne('is_bilan_actif_stocks_marchandises_amortissements_provisions', period)
        avances_et_acomptes = personne('is_bilan_actif_avances_acomptes_verses_commandes_amortissements_provisions', period)
        comptes_rattaches = personne('is_bilan_actif_creances_clients_comptes_rattaches_amortissements_provisions', period)
        autres_creances = personne('is_bilan_actif_creances_autres_creances_amortissements_provisions', period)
        capital_souscrit = personne('is_bilan_actif_creances_capital_souscrit_appele_non_verse_amortissements_provisions', period)
        disponibilites = personne('is_bilan_actif_divers_disponibilites_amortissements_provisions', period)
        charges_constatees_avance = personne('is_bilan_actif_comptes_regularation_charges_constatees_avance_amortissements_provisions', period)
        return stock + en_cous_production_biens + en_cous_production_services + produits_intermediaires + marchandises + avances_et_acomptes + comptes_rattaches + autres_creances + capital_souscrit + disponibilites + charges_constatees_avance

class is_bilan_actif_total_general_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Bilan actif, total général brut (CO)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        capital_souscrit = personne('is_bilan_actif_capital_souscrit_non_appele_brut', period)
        actif_immobilise = personne('is_bilan_actif_total_actif_immobilise_brut', period)
        actif_circulant = personne('is_bilan_actif_total_actif_circulant_brut', period)
        charges = personne('is_bilan_actif_comptes_regularation_charges_repartir_plusieurs_exercices_brut', period)
        return capital_souscrit + actif_immobilise + actif_circulant + charges

class is_bilan_actif_total_general_amortissements_provisions(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Bilan actif, total général amortissements et provisions (1A)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        actif_immobilise = personne('is_bilan_actif_total_actif_immobilise_amortissements_provisions', period)
        actif_circulant = personne('is_bilan_actif_total_actif_circulant_amortissements_provisions', period)
        return actif_immobilise + actif_circulant