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


class is_dettes_total_montant_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Total (7X)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        emprunts_obligatoires_convertibles = personne("is_dettes_emprunts_obligatoires_convertibles_montant_brut", period)
        autres_emprunts_obligatoires = personne("is_dettes_autres_emprunts_obligatoires_montant_brut", period)
        emprunts_et_dettes_aupres_etablissements_de_credit_a_2_max = personne("is_dettes_emprunts_et_dettes_aupres_des_etablissements_de_credit_a_deux_ans_maximum_a_l_origine_montant_brut", period)
        emprunts_et_dettes_aupres_etablissements_de_credit_a_plus_de_2_ans = personne("is_dettes_emprunts_et_dettes_aupres_des_etablissements_de_credit_a_plus_de_deux_ans_a_l_origine_montant_brut", period)
        emprunts_dettes_financieres_diverses = personne("is_dettes_emprunts_et_dettes_financieres_diverses_montant_brut", period)
        fournisseurs_comptes_rattaches = personne("is_dettes_fournisseurs_et_comptes_rattaches_montant_brut", period)
        personel_et_comptes_rattaches = personne("is_dettes_personnel_et_comptes_rattaches_montant_brut", period)
        securite_sociale = personne("is_dettes_securite_sociale_et_autres_organismes_sociaux_montant_brut", period)
        impots_sur_les_benefices = personne("is_dettes_etat_et_autres_collectivites_publiques_impots_sur_les_benefices_montant_brut", period)
        taxe_sur_la_valeur_ajoutee = personne("is_dettes_etat_et_autres_collectivites_publiques_taxe_sur_la_valeur_ajoutee_montant_brut", period)
        obligations_cautionnees = personne("is_dettes_etat_et_autres_collectivites_publiques_obligations_cautionnees_montant_brut", period)
        autres_impots_taxes_et_assimiles = personne("is_dettes_etat_et_autres_collectivites_publiques_taxes_autres_impots_taxes_et_assimiles_montant_brut", period)
        dettes_sur_immobilisations = personne("is_dettes_dettes_sur_immobilisations_et_comptes_rattaches_montant_brut", period)
        groupe_associes = personne("is_dettes_groupe_et_associes_montant_brut", period)
        autres_dettes = personne("is_dettes_autres_dettes_montant_brut", period)
        produits_constate_d_avance = personne("is_dettes_produits_constates_d_avances_montant_brut", period)
        return emprunts_obligatoires_convertibles + autres_emprunts_obligatoires + emprunts_et_dettes_aupres_etablissements_de_credit_a_2_max + emprunts_et_dettes_aupres_etablissements_de_credit_a_plus_de_2_ans + emprunts_dettes_financieres_diverses + fournisseurs_comptes_rattaches + personel_et_comptes_rattaches + securite_sociale + impots_sur_les_benefices + taxe_sur_la_valeur_ajoutee + obligations_cautionnees + autres_impots_taxes_et_assimiles + dettes_sur_immobilisations + groupe_associes + autres_dettes + produits_constate_d_avance


class is_dettes_total_a_un_an_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Total (7X) à un an au plus"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        emprunts_obligatoires_convertibles = personne("is_dettes_emprunts_obligatoires_convertibles_a_un_an_au_plus", period)
        autres_emprunts_obligatoires = personne("is_dettes_autres_emprunts_obligatoires_a_un_an_au_plus", period)
        emprunts_et_dettes_aupres_etablissements_de_credit_a_2_max = personne("is_dettes_emprunts_et_dettes_aupres_des_etablissements_de_credit_a_deux_ans_maximum_a_l_origine_a_un_an_au_plus", period)
        emprunts_et_dettes_aupres_etablissements_de_credit_a_plus_de_2_ans = personne("is_dettes_emprunts_et_dettes_aupres_des_etablissements_de_credit_a_plus_de_deux_ans_a_l_origine_a_un_an_au_plus", period)
        emprunts_dettes_financieres_diverses = personne("is_dettes_emprunts_et_dettes_financieres_diverses_a_un_an_au_plus", period)
        fournisseurs_comptes_rattaches = personne("is_dettes_fournisseurs_et_comptes_rattaches_a_un_an_au_plus", period)
        personel_et_comptes_rattaches = personne("is_dettes_personnel_et_comptes_rattaches_a_un_an_au_plus", period)
        securite_sociale = personne("is_dettes_securite_sociale_et_autres_organismes_sociaux_a_un_an_au_plus", period)
        impots_sur_les_benefices = personne("is_dettes_etat_et_autres_collectivites_publiques_impots_sur_les_benefices_a_un_an_au_plus", period)
        taxe_sur_la_valeur_ajoutee = personne("is_dettes_etat_et_autres_collectivites_publiques_taxe_sur_la_valeur_ajoutee_a_un_an_au_plus", period)
        obligations_cautionnees = personne("is_dettes_etat_et_autres_collectivites_publiques_obligations_cautionnees_a_un_an_au_plus", period)
        autres_impots_taxes_et_assimiles = personne("is_dettes_etat_et_autres_collectivites_publiques_taxes_autres_impots_taxes_et_assimiles_a_un_an_au_plus", period)
        dettes_sur_immobilisations = personne("is_dettes_dettes_sur_immobilisations_et_comptes_rattaches_a_un_an_au_plus", period)
        groupe_associes = personne("is_dettes_groupe_et_associes_a_un_an_au_plus", period)
        autres_dettes = personne("is_dettes_autres_dettes_a_un_an_au_plus", period)
        produits_constate_d_avance = personne("is_dettes_produits_constates_d_avances_a_un_an_au_plus", period)
        return emprunts_obligatoires_convertibles + autres_emprunts_obligatoires + emprunts_et_dettes_aupres_etablissements_de_credit_a_2_max + emprunts_et_dettes_aupres_etablissements_de_credit_a_plus_de_2_ans + emprunts_dettes_financieres_diverses + fournisseurs_comptes_rattaches + personel_et_comptes_rattaches + securite_sociale + impots_sur_les_benefices + taxe_sur_la_valeur_ajoutee + obligations_cautionnees + autres_impots_taxes_et_assimiles + dettes_sur_immobilisations + groupe_associes + autres_dettes + produits_constate_d_avance


class is_dettes_total_a_plus_d_un_an_et_cinq_ans_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Total (7X) à plus d'un an et 5 ans au plus"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        emprunts_obligatoires_convertibles = personne("is_dettes_emprunts_obligatoires_convertibles_a_plus_d_un_an_et_cinq_ans_au_plus", period)
        autres_emprunts_obligatoires = personne("is_dettes_autres_emprunts_obligatoires_a_plus_d_un_an_et_cinq_ans_au_plus", period)
        emprunts_et_dettes_aupres_etablissements_de_credit_a_2_max = personne("is_dettes_emprunts_et_dettes_aupres_des_etablissements_de_credit_a_deux_ans_maximum_a_l_origine_a_plus_d_un_an_et_cinq_ans_au_plus", period)
        emprunts_et_dettes_aupres_etablissements_de_credit_a_plus_de_2_ans = personne("is_dettes_emprunts_et_dettes_aupres_des_etablissements_de_credit_a_plus_de_deux_ans_a_l_origine_a_plus_d_un_an_et_cinq_ans_au_plus", period)
        emprunts_dettes_financieres_diverses = personne("is_dettes_emprunts_et_dettes_financieres_diverses_a_plus_d_un_an_et_cinq_ans_au_plus", period)
        fournisseurs_comptes_rattaches = personne("is_dettes_fournisseurs_et_comptes_rattaches_a_plus_d_un_an_et_cinq_ans_au_plus", period)
        personel_et_comptes_rattaches = personne("is_dettes_personnel_et_comptes_rattaches_a_plus_d_un_an_et_cinq_ans_au_plus", period)
        securite_sociale = personne("is_dettes_securite_sociale_et_autres_organismes_sociaux_a_plus_d_un_an_et_cinq_ans_au_plus", period)
        impots_sur_les_benefices = personne("is_dettes_etat_et_autres_collectivites_publiques_impots_sur_les_benefices_a_plus_d_un_an_et_cinq_ans_au_plus", period)
        taxe_sur_la_valeur_ajoutee = personne("is_dettes_etat_et_autres_collectivites_publiques_taxe_sur_la_valeur_ajoutee_a_plus_d_un_an_et_cinq_ans_au_plus", period)
        obligations_cautionnees = personne("is_dettes_etat_et_autres_collectivites_publiques_obligations_cautionnees_a_plus_d_un_an_et_cinq_ans_au_plus", period)
        autres_impots_taxes_et_assimiles = personne("is_dettes_etat_et_autres_collectivites_publiques_taxes_autres_impots_taxes_et_assimiles_a_plus_d_un_an_et_cinq_ans_au_plus", period)
        dettes_sur_immobilisations = personne("is_dettes_dettes_sur_immobilisations_et_comptes_rattaches_a_plus_d_un_an_et_cinq_ans_au_plus", period)
        groupe_associes = personne("is_dettes_groupe_et_associes_a_plus_d_un_an_et_cinq_ans_au_plus", period)
        autres_dettes = personne("is_dettes_autres_dettes_a_plus_d_un_an_et_cinq_ans_au_plus", period)
        produits_constate_d_avance = personne("is_dettes_produits_constates_d_avances_a_plus_d_un_an_et_cinq_ans_au_plus", period)
        return emprunts_obligatoires_convertibles + autres_emprunts_obligatoires + emprunts_et_dettes_aupres_etablissements_de_credit_a_2_max + emprunts_et_dettes_aupres_etablissements_de_credit_a_plus_de_2_ans + emprunts_dettes_financieres_diverses + fournisseurs_comptes_rattaches + personel_et_comptes_rattaches + securite_sociale + impots_sur_les_benefices + taxe_sur_la_valeur_ajoutee + obligations_cautionnees + autres_impots_taxes_et_assimiles + dettes_sur_immobilisations + groupe_associes + autres_dettes + produits_constate_d_avance


class is_dettes_total_a_plus_de_cinq_ans(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Total (7X) à plus de 5 ans"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        emprunts_obligatoires_convertibles = personne("is_dettes_emprunts_obligatoires_convertibles_a_plus_de_cinq_ans", period)
        autres_emprunts_obligatoires = personne("is_dettes_autres_emprunts_obligatoires_a_plus_de_cinq_ans", period)
        emprunts_et_dettes_aupres_etablissements_de_credit_a_2_max = personne("is_dettes_emprunts_et_dettes_aupres_des_etablissements_de_credit_a_deux_ans_maximum_a_l_origine_a_plus_de_cinq_ans", period)
        emprunts_et_dettes_aupres_etablissements_de_credit_a_plus_de_2_ans = personne("is_dettes_emprunts_et_dettes_aupres_des_etablissements_de_credit_a_plus_de_deux_ans_a_l_origine_a_plus_de_cinq_ans", period)
        emprunts_dettes_financieres_diverses = personne("is_dettes_emprunts_et_dettes_financieres_diverses_a_plus_de_cinq_ans", period)
        fournisseurs_comptes_rattaches = personne("is_dettes_fournisseurs_et_comptes_rattaches_a_plus_de_cinq_ans", period)
        personel_et_comptes_rattaches = personne("is_dettes_personnel_et_comptes_rattaches_a_plus_de_cinq_ans", period)
        securite_sociale = personne("is_dettes_securite_sociale_et_autres_organismes_sociaux_a_plus_de_cinq_ans", period)
        impots_sur_les_benefices = personne("is_dettes_etat_et_autres_collectivites_publiques_impots_sur_les_benefices_a_plus_de_cinq_ans", period)
        taxe_sur_la_valeur_ajoutee = personne("is_dettes_etat_et_autres_collectivites_publiques_taxe_sur_la_valeur_ajoutee_a_plus_de_cinq_ans", period)
        obligations_cautionnees = personne("is_dettes_etat_et_autres_collectivites_publiques_obligations_cautionnees_a_plus_de_cinq_ans", period)
        autres_impots_taxes_et_assimiles = personne("is_dettes_etat_et_autres_collectivites_publiques_taxes_autres_impots_taxes_et_assimiles_a_plus_de_cinq_ans", period)
        dettes_sur_immobilisations = personne("is_dettes_dettes_sur_immobilisations_et_comptes_rattaches_a_plus_de_cinq_ans", period)
        groupe_associes = personne("is_dettes_groupe_et_associes_a_plus_de_cinq_ans", period)
        autres_dettes = personne("is_dettes_autres_dettes_a_plus_de_cinq_ans", period)
        produits_constate_d_avance = personne("is_dettes_produits_constates_d_avances_a_plus_de_cinq_ans", period)
        return emprunts_obligatoires_convertibles + autres_emprunts_obligatoires + emprunts_et_dettes_aupres_etablissements_de_credit_a_2_max + emprunts_et_dettes_aupres_etablissements_de_credit_a_plus_de_2_ans + emprunts_dettes_financieres_diverses + fournisseurs_comptes_rattaches + personel_et_comptes_rattaches + securite_sociale + impots_sur_les_benefices + taxe_sur_la_valeur_ajoutee + obligations_cautionnees + autres_impots_taxes_et_assimiles + dettes_sur_immobilisations + groupe_associes + autres_dettes + produits_constate_d_avance