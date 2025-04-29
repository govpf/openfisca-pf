# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.base import (
    Variable,
    DAY
    )
from openfisca_pf.entities import Personne


class is_dettes_emprunts_obligatoires_convertibles_montant_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes emprunts obligatoires convertibles montant brut (7Y)"


class is_dettes_emprunts_obligatoires_convertibles_a_un_an_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes emprunts obligatoires convertibles a 1 an au plus (7Y)"


class is_dettes_emprunts_obligatoires_convertibles_a_plus_d_un_an_et_cinq_ans_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes emprunts obligatoires convertibles a plus d'un an et cinq ans au plus (7Y)"


class is_dettes_emprunts_obligatoires_convertibles_a_plus_de_cinq_ans(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes emprunts obligatoires convertibles a plus de cinq ans (7Y)"


class is_dettes_autres_emprunts_obligatoires_montant_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes autres emprunts obligatoires montant brut (7Z)"


class is_dettes_autres_emprunts_obligatoires_a_un_an_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes autres emprunts obligatoires a 1 an au plus (7Z)"


class is_dettes_autres_emprunts_obligatoires_a_plus_d_un_an_et_cinq_ans_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes autres emprunts obligatoires a plus d'un an et cinq ans au plus (7Z)"


class is_dettes_autres_emprunts_obligatoires_a_plus_de_cinq_ans(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes autres emprunts obligatoires a plus de cinq ans (7Z)"


class is_dettes_emprunts_et_dettes_aupres_des_etablissements_de_credit_a_deux_ans_maximum_a_l_origine_montant_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes emprunts et dettes au pres des etablissements de credit a deux ans maximum a l'origine montant brut (VG)"


class is_dettes_emprunts_et_dettes_aupres_des_etablissements_de_credit_a_deux_ans_maximum_a_l_origine_a_un_an_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes emprunts et dettes au pres des etablissements de credit a deux ans maximum a l'origine a 1 an au plus (VG)"


class is_dettes_emprunts_et_dettes_aupres_des_etablissements_de_credit_a_deux_ans_maximum_a_l_origine_a_plus_d_un_an_et_cinq_ans_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes emprunts et dettes au pres des etablissements de credit a deux ans maximum a l'origine a plus d'un an et cinq ans au plus (VG)"


class is_dettes_emprunts_et_dettes_aupres_des_etablissements_de_credit_a_deux_ans_maximum_a_l_origine_a_plus_de_cinq_ans(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes emprunts et dettes au pres des etablissements de credit a deux ans maximum a l'origine a plus de cinq ans (VG)"


class is_dettes_emprunts_et_dettes_aupres_des_etablissements_de_credit_a_plus_de_deux_ans_a_l_origine_montant_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes emprunts et dettes au pres des etablissements de credit a plus de deux ans a l'origine montant brut (VH)"


class is_dettes_emprunts_et_dettes_aupres_des_etablissements_de_credit_a_plus_de_deux_ans_a_l_origine_a_un_an_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes emprunts et dettes au pres des etablissements de credit a plus de deux ans a l'origine a 1 an au plus (VH)"


class is_dettes_emprunts_et_dettes_aupres_des_etablissements_de_credit_a_plus_de_deux_ans_a_l_origine_a_plus_d_un_an_et_cinq_ans_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes emprunts et dettes au pres des etablissements de credit a plus de deux ans a l'origine a plus d'un an et cinq ans au plus (VH)"


class is_dettes_emprunts_et_dettes_aupres_des_etablissements_de_credit_a_plus_de_deux_ans_a_l_origine_a_plus_de_cinq_ans(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes emprunts et dettes au pres des etablissements de credit a plus de deux ans a l'origine a plus de cinq ans (VH)"


class is_dettes_emprunts_et_dettes_financieres_diverses_montant_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes emprunts et dettes financieres diverses montant brut (8A)"


class is_dettes_emprunts_et_dettes_financieres_diverses_a_un_an_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes emprunts et dettes financieres diverses a 1 an au plus (8A)"


class is_dettes_emprunts_et_dettes_financieres_diverses_a_plus_d_un_an_et_cinq_ans_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes emprunts et dettes financieres diverses a plus d'un an et cinq ans au plus (8A)"


class is_dettes_emprunts_et_dettes_financieres_diverses_a_plus_de_cinq_ans(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes emprunts et dettes financieres diverses a plus de cinq ans (8A)"


class is_dettes_fournisseurs_et_comptes_rattaches_montant_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes fournisseurs et comptes rattaches montant brut (8B)"


class is_dettes_fournisseurs_et_comptes_rattaches_a_un_an_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes fournisseurs et comptes rattaches a 1 an au plus (8B)"


class is_dettes_fournisseurs_et_comptes_rattaches_a_plus_d_un_an_et_cinq_ans_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes fournisseurs et comptes rattaches a plus d'un an et cinq ans au plus (8B)"


class is_dettes_fournisseurs_et_comptes_rattaches_a_plus_de_cinq_ans(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes fournisseurs et comptes rattaches a plus de cinq ans (8B)"


class is_dettes_personnel_et_comptes_rattaches_montant_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes personnel et comptes rattaches montant brut (8C)"


class is_dettes_personnel_et_comptes_rattaches_a_un_an_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes personnel et comptes rattaches a 1 an au plus (8C)"


class is_dettes_personnel_et_comptes_rattaches_a_plus_d_un_an_et_cinq_ans_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes personnel et comptes rattaches a plus d'un an et cinq ans au plus (8C)"


class is_dettes_personnel_et_comptes_rattaches_a_plus_de_cinq_ans(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes personnel et comptes rattaches a plus de cinq ans (8C)"


class is_dettes_securite_sociale_et_autres_organismes_sociaux_montant_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes Sécurité sociale et autres organismes sociaux montant brut (8D)"


class is_dettes_securite_sociale_et_autres_organismes_sociaux_a_un_an_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes Sécurité sociale et autres organismes sociaux a 1 an au plus (8D)"


class is_dettes_securite_sociale_et_autres_organismes_sociaux_a_plus_d_un_an_et_cinq_ans_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes Sécurité sociale et autres organismes sociaux a plus d'un an et cinq ans au plus (8D)"


class is_dettes_securite_sociale_et_autres_organismes_sociaux_a_plus_de_cinq_ans(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes Sécurité sociale et autres organismes sociaux a plus de cinq ans (8D)"


class is_dettes_etat_et_autres_collectivites_publiques_impots_sur_les_benefices_montant_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes Etat et autres collectivités publiques impôts sur les bénéfices montant brut (8E)"


class is_dettes_etat_et_autres_collectivites_publiques_impots_sur_les_benefices_a_un_an_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes Etat et autres collectivités publiques impôts sur les bénéfices a 1 an au plus (8E)"


class is_dettes_etat_et_autres_collectivites_publiques_impots_sur_les_benefices_a_plus_d_un_an_et_cinq_ans_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes Etat et autres collectivités publiques impôts sur les bénéfices a plus d'un an et cinq ans au plus (8E)"


class is_dettes_etat_et_autres_collectivites_publiques_impots_sur_les_benefices_a_plus_de_cinq_ans(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes Etat et autres collectivités publiques impôts sur les bénéfices a plus de cinq ans (8E)"


class is_dettes_etat_et_autres_collectivites_publiques_taxe_sur_la_valeur_ajoutee_montant_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes Etat et autres collectivités publiques taxe sur la valeur ajoutée montant brut (8F)"


class is_dettes_etat_et_autres_collectivites_publiques_taxe_sur_la_valeur_ajoutee_a_un_an_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes Etat et autres collectivités publiques taxe sur la valeur ajoutée a 1 an au plus (8F)"


class is_dettes_etat_et_autres_collectivites_publiques_taxe_sur_la_valeur_ajoutee_a_plus_d_un_an_et_cinq_ans_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes Etat et autres collectivités publiques taxe sur la valeur ajoutée a plus d'un an et cinq ans au plus (8F)"


class is_dettes_etat_et_autres_collectivites_publiques_taxe_sur_la_valeur_ajoutee_a_plus_de_cinq_ans(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes Etat et autres collectivités publiques taxe sur la valeur ajoutée a plus de cinq ans (8F)"


class is_dettes_etat_et_autres_collectivites_publiques_obligations_cautionnees_montant_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes Etat et autres collectivités publiques obligations cautionnees montant brut (8G)"


class is_dettes_etat_et_autres_collectivites_publiques_obligations_cautionnees_a_un_an_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes Etat et autres collectivités publiques obligations cautionnees a 1 an au plus (8G)"


class is_dettes_etat_et_autres_collectivites_publiques_obligations_cautionnees_a_plus_d_un_an_et_cinq_ans_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes Etat et autres collectivités publiques obligations cautionnees a plus d'un an et cinq ans au plus (8G)"


class is_dettes_etat_et_autres_collectivites_publiques_obligations_cautionnees_a_plus_de_cinq_ans(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes Etat et autres collectivités publiques obligations cautionnees a plus de cinq ans (8G)"


class is_dettes_etat_et_autres_collectivites_publiques_taxes_autres_impots_taxes_et_assimiles_montant_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes Etat et autres collectivités publiques taxes autres impôts taxes et assimilés  montant brut (8H)"


class is_dettes_etat_et_autres_collectivites_publiques_taxes_autres_impots_taxes_et_assimiles_a_un_an_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes Etat et autres collectivités publiques taxes autres impôts taxes et assimilés  a 1 an au plus (8H)"


class is_dettes_etat_et_autres_collectivites_publiques_taxes_autres_impots_taxes_et_assimiles_a_plus_d_un_an_et_cinq_ans_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes Etat et autres collectivités publiques taxes autres impôts taxes et assimilés  a plus d'un an et cinq ans au plus (8H)"


class is_dettes_etat_et_autres_collectivites_publiques_taxes_autres_impots_taxes_et_assimiles_a_plus_de_cinq_ans(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes Etat et autres collectivités publiques taxes autres impôts taxes et assimilés  a plus de cinq ans (8H)"


class is_dettes_dettes_sur_immobilisations_et_comptes_rattaches_montant_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes Dettes sur immobilisations et comptes rattachés (8J)"


class is_dettes_dettes_sur_immobilisations_et_comptes_rattaches_a_un_an_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes Dettes sur immobilisations et comptes rattachés a 1 an au plus (8J)"


class is_dettes_dettes_sur_immobilisations_et_comptes_rattaches_a_plus_d_un_an_et_cinq_ans_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes Dettes sur immobilisations et comptes rattachés a plus d'un an et cinq ans au plus (8J)"


class is_dettes_dettes_sur_immobilisations_et_comptes_rattaches_a_plus_de_cinq_ans(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes Dettes sur immobilisations et comptes rattachés a plus de cinq ans (8J)"


class is_dettes_groupe_et_associes_montant_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes groupe et associés montant brut (VI)"


class is_dettes_groupe_et_associes_a_un_an_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes groupe et associés a 1 an au plus (VI)"


class is_dettes_groupe_et_associes_a_plus_d_un_an_et_cinq_ans_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes groupe et associés a plus d'un an et cinq ans au plus (VI)"


class is_dettes_groupe_et_associes_a_plus_de_cinq_ans(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes groupe et associés a plus de cinq ans (VI)"


class is_dettes_autres_dettes_montant_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes autres dettes montant brut (8K)"


class is_dettes_autres_dettes_a_un_an_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes autres dettes a 1 an au plus (8K)"


class is_dettes_autres_dettes_a_plus_d_un_an_et_cinq_ans_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes autres dettes a plus d'un an et cinq ans au plus (8K)"


class is_dettes_autres_dettes_a_plus_de_cinq_ans(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes autres dettes a plus de cinq ans (8K)"


class is_dettes_produits_constates_d_avances_montant_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes produits constates d avances montant brut (8L)"


class is_dettes_produits_constates_d_avances_a_un_an_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes produits constates d avances a 1 an au plus (8L)"


class is_dettes_produits_constates_d_avances_a_plus_d_un_an_et_cinq_ans_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes produits constates d avances a plus d'un an et cinq ans au plus (8L)"


class is_dettes_produits_constates_d_avances_a_plus_de_cinq_ans(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes produits constates d avances a plus de cinq ans (8L)"
