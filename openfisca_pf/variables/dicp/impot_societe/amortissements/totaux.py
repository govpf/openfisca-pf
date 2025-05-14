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


class is_amortissements_cadre_a_total_iii_montant_au_debut_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables - cadre a - Total III (QU)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        terrains = personne('is_amortissements_terrains_montant_au_debut_de_l_exercice', period)
        constructions_sol_propre = personne('is_amortissements_constructions_sur_sol_propre_montant_au_debut_de_l_exercice', period)
        constructions_sol_autrui = personne('is_amortissements_constructions_sur_sol_autrui_montant_au_debut_de_l_exercice', period)
        constructions_instal_gene = personne('is_amortissements_installations_generales_agencements_et_amenagements_des_constructions_montant_au_debut_de_l_exercice', period)
        installations_industrielles = personne('is_amortissements_installations_techniques_materiels_et_outillages_industriels_montant_au_debut_de_l_exercice', period)
        autre_immo_instal_general = personne('is_amortissements_autres_immobilisations_corporelles_installations_generales_agencements_et_amenagements_divers_montant_au_debut_de_l_exercice', period)
        autres_imo_materiel_transport = personne('is_amortissements_autres_immobilisations_corporelles_materiel_de_transport_montant_au_debut_de_l_exercice', period)
        autres_imo_materiel_bureau = personne('is_amortissements_autres_immobilisations_corporelles_materiel_de_bureau_et_informatique_et_mobilier_montant_au_debut_de_l_exercice', period)
        autres_imo_emballages = personne('is_amortissements_autres_immobilisations_corporelles_emballages_recuperables_et_divers_montant_au_debut_de_l_exercice', period)
        return terrains + constructions_sol_propre + constructions_sol_autrui + constructions_instal_gene + installations_industrielles + autre_immo_instal_general + autres_imo_materiel_transport + autres_imo_materiel_bureau + autres_imo_emballages


class is_amortissements_cadre_a_total_iii_augmentations_dotations_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables - cadre a - Total III (QV)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        terrains = personne('is_amortissements_terrains_augmentations_dotations_de_l_exercice', period)
        constructions_sol_propre = personne('is_amortissements_constructions_sur_sol_propre_augmentations_dotations_de_l_exercice', period)
        constructions_sol_autrui = personne('is_amortissements_constructions_sur_sol_autrui_augmentations_dotations_de_l_exercice', period)
        constructions_instal_gene = personne('is_amortissements_installations_generales_agencements_et_amenagements_des_constructions_augmentations_dotations_de_l_exercice', period)
        installations_industrielles = personne('is_amortissements_installations_techniques_materiels_et_outillages_industriels_augmentations_dotations_de_l_exercice', period)
        autre_immo_instal_general = personne('is_amortissements_autres_immobilisations_corporelles_installations_generales_agencements_et_amenagements_divers_augmentations_dotations_de_l_exercice', period)
        autres_imo_materiel_transport = personne('is_amortissements_autres_immobilisations_corporelles_materiel_de_transport_augmentations_dotations_de_l_exercice', period)
        autres_imo_materiel_bureau = personne('is_amortissements_autres_immobilisations_corporelles_materiel_de_bureau_et_informatique_et_mobilier_augmentations_dotations_de_l_exercice', period)
        autres_imo_emballages = personne('is_amortissements_autres_immobilisations_corporelles_emballages_recuperables_et_divers_augmentations_dotations_de_l_exercice', period)
        return terrains + constructions_sol_propre + constructions_sol_autrui + constructions_instal_gene + installations_industrielles + autre_immo_instal_general + autres_imo_materiel_transport + autres_imo_materiel_bureau + autres_imo_emballages


class is_amortissements_cadre_a_total_iii_diminutions_amortissements_afferents_aux_elements_sortis_de_l_actif_et_reprises(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables - cadre a - Total III (QW)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        terrains = personne('is_amortissements_terrains_diminutions_amortissements_afferents_aux_elements_sortis_de_l_actif_et_reprises', period)
        constructions_sol_propre = personne('is_amortissements_constructions_sur_sol_propre_diminutions_amortissements_afferents_aux_elements_sortis_de_l_actif_et_reprises', period)
        constructions_sol_autrui = personne('is_amortissements_constructions_sur_sol_autrui_diminutions_amortissements_afferents_aux_elements_sortis_de_l_actif_et_reprises', period)
        constructions_instal_gene = personne('is_amortissements_installations_generales_agencements_et_amenagements_des_constructions_diminutions_amortissements_afferents_aux_elements_sortis_de_l_actif_et_reprises', period)
        installations_industrielles = personne('is_amortissements_installations_techniques_materiels_et_outillages_industriels_diminutions_amortissements_afferents_aux_elements_sortis_de_l_actif_et_reprises', period)
        autre_immo_instal_general = personne('is_amortissements_autres_immobilisations_corporelles_installations_generales_agencements_et_amenagements_divers_diminutions_amortissements_afferents_aux_elements_sortis_de_l_actif_et_reprises', period)
        autres_imo_materiel_transport = personne('is_amortissements_autres_immobilisations_corporelles_materiel_de_transport_diminutions_amortissements_afferents_aux_elements_sortis_de_l_actif_et_reprises', period)
        autres_imo_materiel_bureau = personne('is_amortissements_autres_immobilisations_corporelles_materiel_de_bureau_et_informatique_et_mobilier_diminutions_amortissements_afferents_aux_elements_sortis_de_l_actif_et_reprises', period)
        autres_imo_emballages = personne('is_amortissements_autres_immobilisations_corporelles_emballages_recuperables_et_divers_diminutions_amortissements_afferents_aux_elements_sortis_de_l_actif_et_reprises', period)
        return terrains + constructions_sol_propre + constructions_sol_autrui + constructions_instal_gene + installations_industrielles + autre_immo_instal_general + autres_imo_materiel_transport + autres_imo_materiel_bureau + autres_imo_emballages


class is_amortissements_cadre_a_total_iii_montant_a_la_fin_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables - cadre a - Total III (QX)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        terrains = personne('is_amortissements_terrains_montant_a_la_fin_de_l_exercice', period)
        constructions_sol_propre = personne('is_amortissements_constructions_sur_sol_propre_montant_a_la_fin_de_l_exercice', period)
        constructions_sol_autrui = personne('is_amortissements_constructions_sur_sol_autrui_montant_a_la_fin_de_l_exercice', period)
        constructions_instal_gene = personne('is_amortissements_installations_generales_agencements_et_amenagements_des_constructions_montant_a_la_fin_de_l_exercice', period)
        installations_industrielles = personne('is_amortissements_installations_techniques_materiels_et_outillages_industriels_montant_a_la_fin_de_l_exercice', period)
        autre_immo_instal_general = personne('is_amortissements_autres_immobilisations_corporelles_installations_generales_agencements_et_amenagements_divers_montant_a_la_fin_de_l_exercice', period)
        autres_imo_materiel_transport = personne('is_amortissements_autres_immobilisations_corporelles_materiel_de_transport_montant_a_la_fin_de_l_exercice', period)
        autres_imo_materiel_bureau = personne('is_amortissements_autres_immobilisations_corporelles_materiel_de_bureau_et_informatique_et_mobilier_montant_a_la_fin_de_l_exercice', period)
        autres_imo_emballages = personne('is_amortissements_autres_immobilisations_corporelles_emballages_recuperables_et_divers_montant_a_la_fin_de_l_exercice', period)
        return terrains + constructions_sol_propre + constructions_sol_autrui + constructions_instal_gene + installations_industrielles + autre_immo_instal_general + autres_imo_materiel_transport + autres_imo_materiel_bureau + autres_imo_emballages


class is_amortissements_cadre_a_total_general_montant_au_debut_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables - cadre a - Total général (0N)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        frais_etablissement = personne('is_amortissements_frais_d_etablissements_de_recherche_et_de_developpement_total_montant_au_debut_de_l_exercice', period)
        autre_immo_corpo = personne('is_amortissements_autres_immobilisations_incorporelles_montant_au_debut_de_l_exercice', period)
        total_iii = personne('is_amortissements_cadre_a_total_iii_montant_au_debut_de_l_exercice', period)
        return frais_etablissement + autre_immo_corpo + total_iii


class is_amortissements_cadre_a_total_general_augmentations_dotations_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables - cadre a - Total général (0P)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        frais_etablissement = personne('is_amortissements_frais_d_etablissements_de_recherche_et_de_developpement_total_augmentations_dotations_de_l_exercice', period)
        autre_immo_corpo = personne('is_amortissements_autres_immobilisations_incorporelles_augmentations_dotations_de_l_exercice', period)
        total_iii = personne('is_amortissements_cadre_a_total_iii_augmentations_dotations_de_l_exercice', period)
        return frais_etablissement + autre_immo_corpo + total_iii


class is_amortissements_cadre_a_total_general_diminutions_amortissements_afferents_aux_elements_sortis_de_l_actif_et_reprises(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables - cadre a - Total général (0Q)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        frais_etablissement = personne('is_amortissements_frais_d_etablissements_de_recherche_et_de_developpement_total_diminutions_amortissements_afferents_aux_elements_sortis_de_l_actif_et_reprises', period)
        autre_immo_corpo = personne('is_amortissements_autres_immobilisations_incorporelles_diminutions_amortissements_afferents_aux_elements_sortis_de_l_actif_et_reprises', period)
        total_iii = personne('is_amortissements_cadre_a_total_iii_diminutions_amortissements_afferents_aux_elements_sortis_de_l_actif_et_reprises', period)
        return frais_etablissement + autre_immo_corpo + total_iii


class is_amortissements_cadre_a_total_general_montant_a_la_fin_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables - cadre a - Total général (0R)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        frais_etablissement = personne('is_amortissements_frais_d_etablissements_de_recherche_et_de_developpement_total_montant_a_la_fin_de_l_exercice', period)
        autre_immo_corpo = personne('is_amortissements_autres_immobilisations_incorporelles_montant_a_la_fin_de_l_exercice', period)
        total_iii = personne('is_amortissements_cadre_a_total_iii_montant_a_la_fin_de_l_exercice', period)
        return frais_etablissement + autre_immo_corpo + total_iii


class is_amortissements_cadre_b_total_iii_amortissements_lineaires(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables - cadre b - Total III (SB)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        terrains = personne('is_amortissements_terrains_amortissements_lineaires', period)
        constructions_sol_propre = personne('is_amortissements_constructions_sur_sol_propre_amortissements_lineaires', period)
        constructions_sol_autrui = personne('is_amortissements_constructions_sur_sol_d_autrui_amortissements_lineaires', period)
        constructions_instal_gene = personne('is_amortissements_installations_generales_agencements_et_amenagement_amortissements_lineaires', period)
        installations_industrielles = personne('is_amortissements_installations_techniques_materiels_et_outillages_amortissements_lineaires', period)
        autre_immo_instal_general = personne('is_amortissements_autres_immobilisations_corporelles_installations_generales_agencements_et_amenagement_amortissements_lineaires', period)
        autres_imo_materiel_transport = personne('is_amortissements_autres_immobilisations_corporelles_materiel_transport_amortissements_lineaires', period)
        autres_imo_materiel_bureau = personne('is_amortissements_autres_immobilisations_corporelles_materiel_bureau_et_informatique_mobilier_amortissements_lineaires', period)
        autres_imo_emballages = personne('is_amortissements_autres_immobilisations_corporelles_emballages_recuperables_et_divers_amortissements_lineaires', period)
        return terrains + constructions_sol_propre + constructions_sol_autrui + constructions_instal_gene + installations_industrielles + autre_immo_instal_general + autres_imo_materiel_transport + autres_imo_materiel_bureau + autres_imo_emballages


class is_amortissements_cadre_b_total_iii_amortissements_degressifs(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables - cadre b - Total III (SC)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        terrains = personne('is_amortissements_terrains_amortissements_degressifs', period)
        constructions_sol_propre = personne('is_amortissements_constructions_sur_sol_propre_amortissements_degressifs', period)
        constructions_sol_autrui = personne('is_amortissements_constructions_sur_sol_d_autrui_amortissements_degressifs', period)
        constructions_instal_gene = personne('is_amortissements_installations_generales_agencements_et_amenagement_amortissements_degressifs', period)
        installations_industrielles = personne('is_amortissements_installations_techniques_materiels_et_outillages_amortissements_degressifs', period)
        autre_immo_instal_general = personne('is_amortissements_autres_immobilisations_corporelles_installations_generales_agencements_et_amenagement_amortissements_degressifs', period)
        autres_imo_materiel_transport = personne('is_amortissements_autres_immobilisations_corporelles_materiel_transport_amortissements_degressifs', period)
        autres_imo_materiel_bureau = personne('is_amortissements_autres_immobilisations_corporelles_materiel_bureau_et_informatique_mobilier_amortissements_degressifs', period)
        autres_imo_emballages = personne('is_amortissements_autres_immobilisations_corporelles_emballages_recuperables_et_divers_amortissements_degressifs', period)
        return terrains + constructions_sol_propre + constructions_sol_autrui + constructions_instal_gene + installations_industrielles + autre_immo_instal_general + autres_imo_materiel_transport + autres_imo_materiel_bureau + autres_imo_emballages


class is_amortissements_cadre_b_total_iii_amortissements_exceptionnels_dont_amortissements_de_caducite(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables - cadre b - Total III (SD)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        terrains = personne('is_amortissements_terrains_amortissements_exceptionnels_dont_amortissements_de_caducite', period)
        constructions_sol_propre = personne('is_amortissements_constructions_sur_sol_propre_amortissements_exceptionnels_dont_amortissements_de_caducite', period)
        constructions_sol_autrui = personne('is_amortissements_constructions_sur_sol_d_autrui_amortissements_exceptionnels_dont_amortissements_de_caducite', period)
        constructions_instal_gene = personne('is_amortissements_installations_generales_agencements_et_amenagement_amortissements_exceptionnels_dont_amortissements_de_caducite', period)
        installations_industrielles = personne('is_amortissements_installations_techniques_materiels_et_outillages_amortissements_exceptionnels_dont_amortissements_de_caducite', period)
        autre_immo_instal_general = personne('is_amortissements_autres_immobilisations_corporelles_installations_generales_agencements_et_amenagement_amortissements_exceptionnels_dont_amortissements_de_caducite', period)
        autres_imo_materiel_transport = personne('is_amortissements_autres_immobilisations_corporelles_materiel_transport_amortissements_exceptionnels_dont_amortissements_de_caducite', period)
        autres_imo_materiel_bureau = personne('is_amortissements_autres_immobilisations_corporelles_materiel_bureau_et_informatique_mobilier_amortissements_exceptionnels_dont_amortissements_de_caducite', period)
        autres_imo_emballages = personne('is_amortissements_autres_immobilisations_corporelles_emballages_recuperables_et_divers_amortissements_exceptionnels_dont_amortissements_de_caducite', period)
        return terrains + constructions_sol_propre + constructions_sol_autrui + constructions_instal_gene + installations_industrielles + autre_immo_instal_general + autres_imo_materiel_transport + autres_imo_materiel_bureau + autres_imo_emballages


class is_amortissements_cadre_b_total_general_amortissements_lineaires(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables - cadre b - Total général (SG)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        frais_etablissement = personne('is_amortissements_frais_d_etablissement_et_recherche_total_amortissements_lineaires', period)
        autre_immo_corpo = personne('is_amortissements_immobilisations_incorporelles_total_amortissements_lineaires', period)
        total_iii = personne('is_amortissements_cadre_b_total_iii_amortissements_lineaires', period)
        return frais_etablissement + autre_immo_corpo + total_iii


class is_amortissements_cadre_b_total_general_amortissements_degressifs(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables - cadre b - Total général (SH)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        frais_etablissement = personne('is_amortissements_frais_d_etablissement_et_recherche_total_amortissements_degressifs', period)
        autre_immo_corpo = personne('is_amortissements_immobilisations_incorporelles_total_amortissements_degressifs', period)
        total_iii = personne('is_amortissements_cadre_b_total_iii_amortissements_degressifs', period)
        return frais_etablissement + autre_immo_corpo + total_iii


class is_amortissements_cadre_b_total_general_amortissements_exceptionnels_dont_amortissements_de_caducite(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables - cadre b - Total général (SJ)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        frais_etablissement = personne('is_amortissements_frais_d_etablissement_et_recherche_total_amortissements_exceptionnels_dont_amortissements_de_caducite', period)
        autre_immo_corpo = personne('is_amortissements_immobilisations_incorporelles_total_amortissements_exceptionnels_dont_amortissements_de_caducite', period)
        total_iii = personne('is_amortissements_cadre_b_total_iii_amortissements_exceptionnels_dont_amortissements_de_caducite', period)
        return frais_etablissement + autre_immo_corpo + total_iii
