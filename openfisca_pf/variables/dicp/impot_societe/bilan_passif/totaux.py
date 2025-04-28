from openfisca_pf.base import (
    ArrayLike,
    ParameterNode,
    Period,
    Population,
    Variable,
    YEAR
)
from openfisca_pf.entities import Personne


class is_bilan_passif_total_capitaux_propres(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Bilan Passif, total  des captaux propres (DL)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        capital_social_ou_individuel = personne(
            'is_bilan_passif_capital_social_ou_individuel', period)
        primes_emission_de_fusion_apports = personne(
            'is_bilan_passif_primes_emission_de_fusion_apports', period)
        ecart_de_reevaluation = personne(
            'is_bilan_passif_ecart_de_reevaluation', period)
        reserve_legale = personne(
            'is_bilan_passif_reserve_legal', period)
        reserve_statutaire_ou_contractuelles = personne(
            'is_bilan_passif_reserve_statutaire_ou_contractuelles', period)
        autres_reserves = personne(
            'is_bilan_passif_autres_reserves', period)
        report_a_nouveau = personne(
            'is_bilan_passif_report_a_nouveau', period)
        resultat_de_l_exercice = personne(
            'is_bilan_passif_resultat_de_l_exercice', period)
        subventions_d_investissement = personne(
            'is_bilan_passif_subventions_d_investissement', period)
        provisions_reglementees = personne(
            'is_bilan_passif_provisions_reglementees', period)
        return capital_social_ou_individuel + primes_emission_de_fusion_apports + ecart_de_reevaluation + reserve_legale + reserve_statutaire_ou_contractuelles + autres_reserves + report_a_nouveau + resultat_de_l_exercice + subventions_d_investissement + provisions_reglementees


class is_bilan_passif_total_autres_fonds_propres(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Bilan Passif, total des autres fonds propres (DM)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return personne('is_bilan_passif_avances_conditionnees', period)


class is_bilan_passif_total_provision_pour_risque_et_charges(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Bilan Passif, total des provisions pour risques et charges (DN)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        provisions_pour_risques = personne(
            'is_bilan_passif_provisions_pour_risques', period)
        provisions_pour_charges = personne(
            'is_bilan_passif_provisions_pour_charges', period)
        return provisions_pour_risques + provisions_pour_charges


class is_bilan_passif_total_dettes_et_compte_regularisation(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Bilan Passif, total des dettes et compte de régularisation (EC)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        emprunt_dettes = personne(
            'is_bilan_passif_emprunts_et_dettes_aupres_des_etablissements_de_credit', period)
        emprunts_dettes_financieres_diverses = personne(
            'is_bilan_passif_emprunts_et_dettes_financieres_diverses', period)
        avances_et_acomptes_recus_sur_commandes_en_cours = personne(
            'is_bilan_passif_avances_et_acomptes_recus_sur_commandes_en_cours', period)
        dettes_fournisseurs_et_comptes_rattaches = personne(
            'is_bilan_passif_dettes_fournisseurs_et_comptes_rattaches', period)
        dettes_fiscales_et_sociales = personne(
            'is_bilan_passif_dettes_fiscales_et_sociales', period)
        dettes_immo_et_comptes_rattaches = personne(
            'is_bilan_passif_dettes_sur_immobilisations_et_comptes_rattaches', period)
        autres_dettes = personne(
            'is_bilan_passif_autres_dettes', period)
        produit_constates_avance = personne(
            'is_bilan_passif_produit_constates_avance', period)
        return emprunt_dettes + emprunts_dettes_financieres_diverses + avances_et_acomptes_recus_sur_commandes_en_cours + dettes_fournisseurs_et_comptes_rattaches + dettes_fiscales_et_sociales + dettes_immo_et_comptes_rattaches + autres_dettes + produit_constates_avance


class is_bilan_passif_total_general(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Bilan Passif, total général (EE)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        total_capitaux_propres = personne(
            'is_bilan_passif_total_capitaux_propres', period)
        total_autres_fonds_propres = personne(
            'is_bilan_passif_total_autres_fonds_propres', period)
        total_provision_pour_risque_et_charges = personne(
            'is_bilan_passif_total_provision_pour_risque_et_charges', period)
        total_dettes_et_compte_regularisation = personne(
            'is_bilan_passif_total_dettes_et_compte_regularisation', period)
        return total_capitaux_propres + total_autres_fonds_propres + total_provision_pour_risque_et_charges + total_dettes_et_compte_regularisation
