# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.base import (
    Variable,
    YEAR
    )
from openfisca_pf.entities import Personne


class is_creances_clients_douteux_ou_litigieux_montant_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Clients douteux ou litigieux montant brut (VA)"


class is_creances_clients_douteux_ou_litigieux_a_un_an_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Clients douteux ou litigieux à un an au plus (VA)"


class is_creances_clients_douteux_ou_litigieux_a_plus_d_un_an(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Clients douteux ou litigieux à plus d'un an (VA)"


class is_creances_autres_creances_clients_montant_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Autres créances clients montant brut (7N)"


class is_creances_autres_creances_clients_a_un_an_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Autres créances clients à un an au plus (7N)"


class is_creances_autres_creances_clients_a_plus_d_un_an(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Autres créances clients à plus d'un an (7N)"


class is_creances_personnel_et_comptes_rattaches_montant_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Personnel et comptes rattachés montant brut (7P)"


class is_creances_personnel_et_comptes_rattaches_a_un_an_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Personnel et comptes rattachés à un an au plus (7P)"


class is_creances_personnel_et_comptes_rattaches_a_plus_d_un_an(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Personnel et comptes rattachés à plus d'un an (7P)"


class is_creances_securite_social_et_autres_organismes_sociaux_montant_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Sécurité sociale et autres organismes sociaux montant brut (7R)"


class is_creances_securite_social_et_autres_organismes_sociaux_a_un_an_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Sécurité sociale et autres organismes sociaux à un an au plus (7R)"


class is_creances_securite_social_et_autres_organismes_sociaux_a_plus_d_un_an(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Sécurité sociale et autres organismes sociaux à plus d'un an (7R)"


class is_creances_etat_et_autres_collectivites_publiques_impots_sur_les_benefices_montant_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "État et autres collectivités publiques impôts sur les bénéfices montant brut (7S)"


class is_creances_etat_et_autres_collectivites_publiques_impots_sur_les_benefices_a_un_an_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "État et autres collectivités publiques impôts sur les bénéfices à un an au plus (7S)"


class is_creances_etat_et_autres_collectivites_publiques_impots_sur_les_benefices_a_plus_d_un_an(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "État et autres collectivités publiques impôts sur les bénéfices à plus d'un an (7S)"


class is_creances_etat_et_autres_collectivites_publiques_taxe_sur_la_valeur_ajoutee_montant_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "État et autres collectivités publiques taxe sur la valeur ajoutée montant brut (VB)"


class is_creances_etat_et_autres_collectivites_publiques_taxe_sur_la_valeur_ajoutee_a_un_an_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "État et autres collectivités publiques taxe sur la valeur ajoutée à un an au plus (VB)"


class is_creances_etat_et_autres_collectivites_publiques_taxe_sur_la_valeur_ajoutee_a_plus_d_un_an(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "État et autres collectivités publiques taxe sur la valeur ajoutée à plus d'un an (VB)"


class is_creances_etat_et_autres_collectivites_publiques_autres_impots_taxes_et_versements_assimiles_montant_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "État et autres collectivités publiques autres impôts taxes et versements assimilés montant brut (7T)"


class is_creances_etat_et_autres_collectivites_publiques_autres_impots_taxes_et_versements_assimiles_a_un_an_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "État et autres collectivités publiques autres impôts taxes et versements assimilés à un an au plus (7T)"


class is_creances_etat_et_autres_collectivites_publiques_autres_impots_taxes_et_versements_assimiles_a_plus_d_un_an(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "État et autres collectivités publiques autres impôts taxes et versements assimilés à plus d'un an (7T)"


class is_creances_etat_et_autres_collectivites_publiques_divers_montant_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "État et autres collectivités publiques divers montant brut (7U)"


class is_creances_etat_et_autres_collectivites_publiques_divers_a_un_an_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "État et autres collectivités publiques divers à un an au plus (7U)"


class is_creances_etat_et_autres_collectivites_publiques_divers_a_plus_d_un_an(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "État et autres collectivités publiques divers à plus d'un an (7U)"


class is_creances_groupe_et_associes_montant_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Groupe et associés montant brut (VC)"


class is_creances_groupe_et_associes_a_un_an_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Groupe et associés à un an au plus (VC)"


class is_creances_groupe_et_associes_a_plus_d_un_an(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Groupe et associés à plus d'un an (VC)"


class is_creances_debiteurs_divers_montant_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Débiteurs divers montant brut (7V)"


class is_creances_debiteurs_divers_a_un_an_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Débiteurs divers à un an au plus (7V)"


class is_creances_debiteurs_divers_a_plus_d_un_an(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Débiteurs divers à plus d'un an (7V)"
