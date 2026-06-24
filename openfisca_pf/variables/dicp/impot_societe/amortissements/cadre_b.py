# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.base import (
    Variable,
    YEAR
    )
from openfisca_pf.entities import Personne


class is_amortissements_frais_d_etablissement_et_recherche_total_amortissements_lineaires(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables Frais d'établissement et de recherche - Total I - amortissements linéaires (QY)"


class is_amortissements_frais_d_etablissement_et_recherche_total_amortissements_degressifs(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables Frais d'établissement et de recherche - Total I - amortissements dégressifs (2J)"


class is_amortissements_frais_d_etablissement_et_recherche_total_amortissements_exceptionnels_dont_amortissements_de_caducite(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables Frais d'établissement et de recherche - Total I - amortissements exceptionnels dont amortissements de caducité (2K)"


class is_amortissements_immobilisations_incorporelles_total_amortissements_lineaires(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables Immobilisations incorporelles - Total II - amortissements linéaires (QZ)"


class is_amortissements_immobilisations_incorporelles_total_amortissements_degressifs(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables Immobilisations incorporelles - Total II - amortissements dégressifs (2N)"


class is_amortissements_immobilisations_incorporelles_total_amortissements_exceptionnels_dont_amortissements_de_caducite(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables Immobilisations incorporelles - Total II - amortissements exceptionnels dont amortissements de caducité (2P)"


class is_amortissements_terrains_amortissements_lineaires(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables Terrains - amortissements linéaires (RA)"


class is_amortissements_terrains_amortissements_degressifs(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables Terrains - amortissements dégressifs (RB)"


class is_amortissements_terrains_amortissements_exceptionnels_dont_amortissements_de_caducite(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables Terrains - amortissements exceptionnels dont amortissements de caducité (RC)"


class is_amortissements_constructions_sur_sol_propre_amortissements_lineaires(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables Constructions sur sol propre - amortissements linéaires (RD)"


class is_amortissements_constructions_sur_sol_propre_amortissements_degressifs(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables Constructions sur sol propre - amortissements dégressifs (RE)"


class is_amortissements_constructions_sur_sol_propre_amortissements_exceptionnels_dont_amortissements_de_caducite(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables Constructions sur sol propre - amortissements exceptionnels dont amortissements de caducité (RF)"


class is_amortissements_constructions_sur_sol_d_autrui_amortissements_lineaires(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables Constructions sur sol d'autrui - amortissements linéaires (RG)"


class is_amortissements_constructions_sur_sol_d_autrui_amortissements_degressifs(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables Constructions sur sol d'autrui - amortissements dégressifs (RH)"


class is_amortissements_constructions_sur_sol_d_autrui_amortissements_exceptionnels_dont_amortissements_de_caducite(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables Constructions sur sol d'autrui - amortissements exceptionnels dont amortissements de caducité (RI)"


class is_amortissements_installations_generales_agencements_et_amenagement_amortissements_lineaires(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables Installations générales, agencements et aménagement - amortissements linéaires (RJ)"


class is_amortissements_installations_generales_agencements_et_amenagement_amortissements_degressifs(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables Installations générales, agencements et aménagement - amortissements dégressifs (RK)"


class is_amortissements_installations_generales_agencements_et_amenagement_amortissements_exceptionnels_dont_amortissements_de_caducite(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables Installations générales, agencements et aménagement - amortissements exceptionnels dont amortissements de caducité (RL)"


class is_amortissements_installations_techniques_materiels_et_outillages_amortissements_lineaires(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables Installations techniques, matériels et outillages - amortissements linéaires (RM)"


class is_amortissements_installations_techniques_materiels_et_outillages_amortissements_degressifs(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables Installations techniques, matériels et outillages - amortissements dégressifs (RN)"


class is_amortissements_installations_techniques_materiels_et_outillages_amortissements_exceptionnels_dont_amortissements_de_caducite(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables Installations techniques, matériels et outillages - amortissements exceptionnels dont amortissements de caducité (RO)"


class is_amortissements_autres_immobilisations_corporelles_installations_generales_agencements_et_amenagement_amortissements_lineaires(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables Autres immobilisations corporelles - Installations générales, agencements et aménagement - amortissements linéaires (RP)"


class is_amortissements_autres_immobilisations_corporelles_installations_generales_agencements_et_amenagement_amortissements_degressifs(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables Autres immobilisations corporelles - Installations générales, agencements et aménagement - amortissements dégressifs (RQ)"


class is_amortissements_autres_immobilisations_corporelles_installations_generales_agencements_et_amenagement_amortissements_exceptionnels_dont_amortissements_de_caducite(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables Autres immobilisations corporelles - Installations générales, agencements et aménagement - amortissements exceptionnels dont amortissements de caducité (RR)"


class is_amortissements_autres_immobilisations_corporelles_materiel_transport_amortissements_lineaires(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables Autres immobilisations corporelles - Matériel de transport - amortissements linéaires (RS)"


class is_amortissements_autres_immobilisations_corporelles_materiel_transport_amortissements_degressifs(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables Autres immobilisations corporelles - Matériel de transport - amortissements dégressifs (RT)"


class is_amortissements_autres_immobilisations_corporelles_materiel_transport_amortissements_exceptionnels_dont_amortissements_de_caducite(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables Autres immobilisations corporelles - Matériel de transport - amortissements exceptionnels dont amortissements de caducité (RU)"


class is_amortissements_autres_immobilisations_corporelles_materiel_bureau_et_informatique_mobilier_amortissements_lineaires(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables Autres immobilisations corporelles - Matériel de bureau et informatique, mobilier - amortissements linéaires (RV)"


class is_amortissements_autres_immobilisations_corporelles_materiel_bureau_et_informatique_mobilier_amortissements_degressifs(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables Autres immobilisations corporelles - Matériel de bureau et informatique, mobilier - amortissements dégressifs (RW)"


class is_amortissements_autres_immobilisations_corporelles_materiel_bureau_et_informatique_mobilier_amortissements_exceptionnels_dont_amortissements_de_caducite(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables Autres immobilisations corporelles - Matériel de bureau et informatique, mobilier - amortissements exceptionnels dont amortissements de caducité (RX)"


class is_amortissements_autres_immobilisations_corporelles_emballages_recuperables_et_divers_amortissements_lineaires(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables Autres immobilisations corporelles - Emballages récupérables et divers - amortissements linéaires (RY)"


class is_amortissements_autres_immobilisations_corporelles_emballages_recuperables_et_divers_amortissements_degressifs(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables Autres immobilisations corporelles - Emballages récupérables et divers - amortissements dégressifs (RZ)"


class is_amortissements_autres_immobilisations_corporelles_emballages_recuperables_et_divers_amortissements_exceptionnels_dont_amortissements_de_caducite(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations amortissables Autres immobilisations corporelles - Emballages récupérables et divers - amortissements exceptionnels dont amortissements de caducité (SA)"
