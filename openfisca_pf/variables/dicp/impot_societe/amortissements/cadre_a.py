# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.base import (
    Variable,
    YEAR
    )
from openfisca_pf.entities import Personne


class is_amortissements_frais_d_etablissements_de_recherche_et_de_developpement_total_montant_au_debut_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Frais d'établissement de recherche et de développement - TOTAL I - Montant au début de l'exercice (PA)"


class is_amortissements_frais_d_etablissements_de_recherche_et_de_developpement_total_augmentations_dotations_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Frais d'établissement de recherche et de développement - TOTAL I - Augmentations dotations de l'exercice (PB)"


class is_amortissements_frais_d_etablissements_de_recherche_et_de_developpement_total_diminutions_amortissements_afferents_aux_elements_sortis_de_l_actif_et_reprises(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Frais d'établissement de recherche et de développement - TOTAL I - Diminutions amortissements afférents aux éléments sortis de l'actif et reprises (PC)"


class is_amortissements_frais_d_etablissements_de_recherche_et_de_developpement_total_montant_a_la_fin_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Frais d'établissement de recherche et de développement - TOTAL I - Montant à la fin de l'exercice (PD)"


class is_amortissements_autres_immobilisations_incorporelles_montant_au_debut_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Autres immobilisations incorporelles - TOTAL II - Montant au début de l'exercice (PE)"


class is_amortissements_autres_immobilisations_incorporelles_augmentations_dotations_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Autres immobilisations incorporelles - TOTAL II - Augmentations dotations de l'exercice (PF)"


class is_amortissements_autres_immobilisations_incorporelles_diminutions_amortissements_afferents_aux_elements_sortis_de_l_actif_et_reprises(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Autres immobilisations incorporelles - TOTAL II - Diminutions amortissements afférents aux éléments sortis de l'actif et reprises (PG)"


class is_amortissements_autres_immobilisations_incorporelles_montant_a_la_fin_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Autres immobilisations incorporelles - TOTAL II - Montant à la fin de l'exercice (PH)"


class is_amortissements_terrains_montant_au_debut_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Terrains - Montant à la fin de l'exercice (PI)"


class is_amortissements_terrains_augmentations_dotations_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Terrains - Augmentations dotations de l'exercice (PJ)"


class is_amortissements_terrains_diminutions_amortissements_afferents_aux_elements_sortis_de_l_actif_et_reprises(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Terrains - Diminutions amortissements afférents aux éléments sortis de l'actif et reprises (PK)"


class is_amortissements_terrains_montant_a_la_fin_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Terrains - Montant à la fin de l'exercice (PL)"


class is_amortissements_constructions_sur_sol_propre_montant_au_debut_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Constructions sur sol propre - Montant au début de l'exercice (PM)"


class is_amortissements_constructions_sur_sol_propre_augmentations_dotations_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Constructions sur sol propre - Augmentations dotations de l'exercice (PN)"


class is_amortissements_constructions_sur_sol_propre_diminutions_amortissements_afferents_aux_elements_sortis_de_l_actif_et_reprises(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Constructions sur sol propre - Diminutions amortissements afférents aux éléments sortis de l'actif et reprises (PO)"


class is_amortissements_constructions_sur_sol_propre_montant_a_la_fin_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Constructions sur sol propre - Montant à la fin de l'exercice (PQ)"


class is_amortissements_constructions_sur_sol_autrui_montant_au_debut_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Constructions sur sol autrui - Montant au début de l'exercice (PR)"


class is_amortissements_constructions_sur_sol_autrui_augmentations_dotations_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Constructions sur sol autrui - Augmentations dotations de l'exercice (PS)"


class is_amortissements_constructions_sur_sol_autrui_diminutions_amortissements_afferents_aux_elements_sortis_de_l_actif_et_reprises(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Constructions sur sol autrui - Diminutions amortissements afférents aux éléments sortis de l'actif et reprises (PT)"


class is_amortissements_constructions_sur_sol_autrui_montant_a_la_fin_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Constructions sur sol autrui - Montant à la fin de l'exercice (PU)"


class is_amortissements_installations_generales_agencements_et_amenagements_des_constructions_montant_au_debut_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Installations générales, agencements et aménagements des constructions - Montant au début de l'exercice (PV)"


class is_amortissements_installations_generales_agencements_et_amenagements_des_constructions_augmentations_dotations_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Installations générales, agencements et aménagements des constructions - Augmentations dotations de l'exercice (PW)"


class is_amortissements_installations_generales_agencements_et_amenagements_des_constructions_diminutions_amortissements_afferents_aux_elements_sortis_de_l_actif_et_reprises(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Installations générales, agencements et aménagements des constructions - Diminutions amortissements afférents aux éléments sortis de l'actif et reprises (PX)"


class is_amortissements_installations_generales_agencements_et_amenagements_des_constructions_montant_a_la_fin_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Installations générales, agencements et aménagements des constructions - Montant à la fin de l'exercice (PY)"


class is_amortissements_installations_techniques_materiels_et_outillages_industriels_montant_au_debut_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Installations techniques, matériels et outillages industriels - Montant au début de l'exercice (PZ)"


class is_amortissements_installations_techniques_materiels_et_outillages_industriels_augmentations_dotations_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Installations techniques, matériels et outillages industriels - Augmentations dotations de l'exercice (QA)"


class is_amortissements_installations_techniques_materiels_et_outillages_industriels_diminutions_amortissements_afferents_aux_elements_sortis_de_l_actif_et_reprises(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Installations techniques, matériels et outillages industriels - Diminutions amortissements afférents aux éléments sortis de l'actif et reprises (QB)"


class is_amortissements_installations_techniques_materiels_et_outillages_industriels_montant_a_la_fin_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Installations techniques, matériels et outillages industriels - Montant à la fin de l'exercice (QC)"


class is_amortissements_autres_immobilisations_corporelles_installations_generales_agencements_et_amenagements_divers_montant_au_debut_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Autres immobilisations corporelles - Installations générales, agencements et aménagements divers - Montant au début de l'exercice (QD)"


class is_amortissements_autres_immobilisations_corporelles_installations_generales_agencements_et_amenagements_divers_augmentations_dotations_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Autres immobilisations corporelles - Installations générales, agencements et aménagements divers - Augmentations dotations de l'exercice (QE)"


class is_amortissements_autres_immobilisations_corporelles_installations_generales_agencements_et_amenagements_divers_diminutions_amortissements_afferents_aux_elements_sortis_de_l_actif_et_reprises(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Autres immobilisations corporelles - Installations générales, agencements et aménagements divers - Diminutions amortissements afférents aux éléments sortis de l'actif et reprises (QF)"


class is_amortissements_autres_immobilisations_corporelles_installations_generales_agencements_et_amenagements_divers_montant_a_la_fin_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Autres immobilisations corporelles - Installations générales, agencements et aménagements divers - Montant à la fin de l'exercice (QG)"


class is_amortissements_autres_immobilisations_corporelles_materiel_de_transport_montant_au_debut_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Autres immobilisations corporelles - Matériel de transport - Montant au début de l'exercice (QH)"


class is_amortissements_autres_immobilisations_corporelles_materiel_de_transport_augmentations_dotations_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Autres immobilisations corporelles - Matériel de transport - Augmentations dotations de l'exercice (QI)"


class is_amortissements_autres_immobilisations_corporelles_materiel_de_transport_diminutions_amortissements_afferents_aux_elements_sortis_de_l_actif_et_reprises(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Autres immobilisations corporelles - Matériel de transport - Diminutions amortissements afférents aux éléments sortis de l'actif et reprises (QJ)"


class is_amortissements_autres_immobilisations_corporelles_materiel_de_transport_montant_a_la_fin_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Autres immobilisations corporelles - Matériel de transport - Montant à la fin de l'exercice (QK)"


class is_amortissements_autres_immobilisations_corporelles_materiel_de_bureau_et_informatique_et_mobilier_montant_au_debut_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Autres immobilisations corporelles - Matériel de bureau et informatique et mobilier - Montant au début de l'exercice (QL)"


class is_amortissements_autres_immobilisations_corporelles_materiel_de_bureau_et_informatique_et_mobilier_augmentations_dotations_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Autres immobilisations corporelles - Matériel de bureau et informatique et mobilier - Augmentations dotations de l'exercice (QM)"


class is_amortissements_autres_immobilisations_corporelles_materiel_de_bureau_et_informatique_et_mobilier_diminutions_amortissements_afferents_aux_elements_sortis_de_l_actif_et_reprises(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Autres immobilisations corporelles - Matériel de bureau et informatique et mobilier - Diminutions amortissements afférents aux éléments sortis de l'actif et reprises (QN)"


class is_amortissements_autres_immobilisations_corporelles_materiel_de_bureau_et_informatique_et_mobilier_montant_a_la_fin_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Autres immobilisations corporelles - Matériel de bureau et informatique et mobilier - Montant à la fin de l'exercice (QO)"


class is_amortissements_autres_immobilisations_corporelles_emballages_recuperables_et_divers_montant_au_debut_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Autres immobilisations corporelles - Emballages récupérables et divers - Montant au début de l'exercice (QP)"


class is_amortissements_autres_immobilisations_corporelles_emballages_recuperables_et_divers_augmentations_dotations_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Autres immobilisations corporelles - Emballages récupérables et divers - Augmentations dotations de l'exercice (QR)"


class is_amortissements_autres_immobilisations_corporelles_emballages_recuperables_et_divers_diminutions_amortissements_afferents_aux_elements_sortis_de_l_actif_et_reprises(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Autres immobilisations corporelles - Emballages récupérables et divers - Diminutions amortissements afférents aux éléments sortis de l'actif et reprises (QS)"


class is_amortissements_autres_immobilisations_corporelles_emballages_recuperables_et_divers_montant_a_la_fin_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisation Amortissables Autres immobilisations corporelles - Emballages récupérables et divers - Montant à la fin de l'exercice (QT)"
