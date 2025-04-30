# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.base import (
    ArrayLike,
    YEAR,
    ParameterNode,
    Period,
    Population,
    Variable
    )
from openfisca_pf.entities import Personne


class is_creances_total_montant_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Total (7X)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        creances_rattaches_a_des_participations = personne('is_creances_creances_rattachees_a_des_participations_montant_brut', period)
        prets = personne('is_creances_prets_montant_brut', period)
        autres_immobilisations_financieres = personne('is_creances_autres_immobilisations_financieres_montant_brut', period)
        clients_douteux_ou_litigieux = personne('is_creances_clients_douteux_ou_litigieux_montant_brut', period)
        autres_creances_clients = personne('is_creances_autres_creances_clients_montant_brut', period)
        personnel_et_comptes_rattaches = personne('is_creances_personnel_et_comptes_rattaches_montant_brut', period)
        securite_social_et_autres_organismes_sociaux = personne('is_creances_securite_social_et_autres_organismes_sociaux_montant_brut', period)
        impots_benefice = personne('is_creances_etat_et_autres_collectivites_publiques_impots_sur_les_benefices_montant_brut', period)
        taxe_valeur_ajoutee = personne('is_creances_etat_et_autres_collectivites_publiques_taxe_sur_la_valeur_ajoutee_montant_brut', period)
        autre_impots_taxes_versement_assimilies = personne('is_creances_etat_et_autres_collectivites_publiques_autres_impots_taxes_et_versements_assimiles_montant_brut', period)
        divers = personne('is_creances_etat_et_autres_collectivites_publiques_divers_montant_brut', period)
        groupe_associes = personne('is_creances_groupe_et_associes_montant_brut', period)
        debiteurs_divers = personne('is_creances_debiteurs_divers_montant_brut', period)
        charges_constate_d_avances = personne('is_creances_charges_constatees_d_avance_montant_brut', period)
        return creances_rattaches_a_des_participations + prets + autres_immobilisations_financieres + clients_douteux_ou_litigieux + autres_creances_clients + personnel_et_comptes_rattaches + securite_social_et_autres_organismes_sociaux + impots_benefice + taxe_valeur_ajoutee + autre_impots_taxes_versement_assimilies + divers + groupe_associes + debiteurs_divers + charges_constate_d_avances


class is_creances_total_a_un_an_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Total à un an au plus (7X)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        creances_rattaches_a_des_participations = personne('is_creances_creances_rattachees_a_des_participations_a_un_an_au_plus', period)
        prets = personne('is_creances_prets_a_un_an_au_plus', period)
        autres_immobilisations_financieres = personne('is_creances_autres_immobilisations_financieres_a_un_an_au_plus', period)
        clients_douteux_ou_litigieux = personne('is_creances_clients_douteux_ou_litigieux_a_un_an_au_plus', period)
        autres_creances_clients = personne('is_creances_autres_creances_clients_a_un_an_au_plus', period)
        personnel_et_comptes_rattaches = personne('is_creances_personnel_et_comptes_rattaches_a_un_an_au_plus', period)
        securite_social_et_autres_organismes_sociaux = personne('is_creances_securite_social_et_autres_organismes_sociaux_a_un_an_au_plus', period)
        impots_benefice = personne('is_creances_etat_et_autres_collectivites_publiques_impots_sur_les_benefices_a_un_an_au_plus', period)
        taxe_valeur_ajoutee = personne('is_creances_etat_et_autres_collectivites_publiques_taxe_sur_la_valeur_ajoutee_a_un_an_au_plus', period)
        autre_impots_taxes_versement_assimilies = personne('is_creances_etat_et_autres_collectivites_publiques_autres_impots_taxes_et_versements_assimiles_a_un_an_au_plus', period)
        divers = personne('is_creances_etat_et_autres_collectivites_publiques_divers_a_un_an_au_plus', period)
        groupe_associes = personne('is_creances_groupe_et_associes_a_un_an_au_plus', period)
        debiteurs_divers = personne('is_creances_debiteurs_divers_a_un_an_au_plus', period)
        charges_constate_d_avances = personne('is_creances_charges_constatees_d_avance_a_un_an_au_plus', period)
        return creances_rattaches_a_des_participations + prets + autres_immobilisations_financieres + clients_douteux_ou_litigieux + autres_creances_clients + personnel_et_comptes_rattaches + securite_social_et_autres_organismes_sociaux + impots_benefice + taxe_valeur_ajoutee + autre_impots_taxes_versement_assimilies + divers + groupe_associes + debiteurs_divers + charges_constate_d_avances


class is_creances_total_a_plus_d_un_an(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Total à plus d'un an (7X)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        creances_rattaches_a_des_participations = personne('is_creances_creances_rattachees_a_des_participations_a_plus_d_un_an', period)
        prets = personne('is_creances_prets_a_plus_d_un_an', period)
        autres_immobilisations_financieres = personne('is_creances_autres_immobilisations_financieres_a_plus_d_un_an', period)
        clients_douteux_ou_litigieux = personne('is_creances_clients_douteux_ou_litigieux_a_plus_d_un_an', period)
        autres_creances_clients = personne('is_creances_autres_creances_clients_a_plus_d_un_an', period)
        personnel_et_comptes_rattaches = personne('is_creances_personnel_et_comptes_rattaches_a_plus_d_un_an', period)
        securite_social_et_autres_organismes_sociaux = personne('is_creances_securite_social_et_autres_organismes_sociaux_a_plus_d_un_an', period)
        impots_benefice = personne('is_creances_etat_et_autres_collectivites_publiques_impots_sur_les_benefices_a_plus_d_un_an', period)
        taxe_valeur_ajoutee = personne('is_creances_etat_et_autres_collectivites_publiques_taxe_sur_la_valeur_ajoutee_a_plus_d_un_an', period)
        autre_impots_taxes_versement_assimilies = personne('is_creances_etat_et_autres_collectivites_publiques_autres_impots_taxes_et_versements_assimiles_a_plus_d_un_an', period)
        divers = personne('is_creances_etat_et_autres_collectivites_publiques_divers_a_plus_d_un_an', period)
        groupe_associes = personne('is_creances_groupe_et_associes_a_plus_d_un_an', period)
        debiteurs_divers = personne('is_creances_debiteurs_divers_a_plus_d_un_an', period)
        charges_constate_d_avances = personne('is_creances_charges_constatees_d_avance_a_plus_d_un_an', period)
        return creances_rattaches_a_des_participations + prets + autres_immobilisations_financieres + clients_douteux_ou_litigieux + autres_creances_clients + personnel_et_comptes_rattaches + securite_social_et_autres_organismes_sociaux + impots_benefice + taxe_valeur_ajoutee + autre_impots_taxes_versement_assimilies + divers + groupe_associes + debiteurs_divers + charges_constate_d_avances
