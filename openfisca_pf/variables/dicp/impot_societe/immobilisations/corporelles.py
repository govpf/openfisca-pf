from openfisca_core.model_api import YEAR, Variable
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import Personne


# TERRAINS
class is_immobilisations_corporelles_terrains_brute_debut_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Terrains, Valeur brute des immobilisations au début de l'exercice (KG)"


class is_immobilisations_corporelles_terrains_augmentation_reevaluation(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Terrains, Augmentations Consécutives à une réévaluation pratiquée au cours de l'exercice (KH)"


class is_immobilisations_corporelles_terrains_augmentation_nouveaux(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Terrains, Augmentations Acquisitions, créations, apports et virements de poste à poste  (KI)"


class is_immobilisations_corporelles_terrains_diminution_poste_a_poste(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Terrains, Diminutions par virement de poste à poste (IP)"


class is_immobilisations_corporelles_terrains_diminution_cession_hors_services(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Terrains, Diminutions par cession à des tiers ou mises hors services (LX)"


class is_immobilisations_corporelles_terrains_brute_fin_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Terrains, Valeur brute des immobilisations à la fin de l'exercice (LY)"


class is_immobilisations_corporelles_terrains_origine_reevaluees_fin_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Terrains, Valeur d'origine des immobilisations réévaluées en fin d'exercice (LZ)"


# Constructions Sur sol propre
class is_immobilisations_corporelles_constructions_sur_sol_propre_brute_debut_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Constructions Sur sol propre, Valeur brute des immobilisations au début de l'exercice (KJ)"


class is_immobilisations_corporelles_constructions_sur_sol_propre_augmentation_reevaluation(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Constructions Sur sol propre, Augmentations Consécutives à une réévaluation pratiquée au cours de l'exercice (KK)"


class is_immobilisations_corporelles_constructions_sur_sol_propre_augmentation_nouveaux(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Constructions Sur sol propre, Augmentations Acquisitions, créations, apports et virements de poste à poste  (KL)"


class is_immobilisations_corporelles_constructions_sur_sol_propre_diminution_poste_a_poste(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Constructions Sur sol propre, Diminutions par virement de poste à poste (IQ)"


class is_immobilisations_corporelles_constructions_sur_sol_propre_diminution_cession_hors_services(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Constructions Sur sol propre, Diminutions par cession à des tiers ou mises hors services (MA)"


class is_immobilisations_corporelles_constructions_sur_sol_propre_brute_fin_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Constructions Sur sol propre, Valeur brute des immobilisations à la fin de l'exercice (MB)"


class is_immobilisations_corporelles_constructions_sur_sol_propre_origine_reevaluees_fin_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Constructions Sur sol propre, Valeur d'origine des immobilisations réévaluées en fin d'exercice (MC)"


# Constructions Sur sol d'autrui
class is_immobilisations_corporelles_constructions_sur_sol_autrui_brute_debut_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Constructions Sur sol d'autrui, Valeur brute des immobilisations au début de l'exercice (KM)"


class is_immobilisations_corporelles_constructions_sur_sol_autrui_augmentation_reevaluation(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Constructions Sur sol d'autrui, Augmentations Consécutives à une réévaluation pratiquée au cours de l'exercice (KN)"


class is_immobilisations_corporelles_constructions_sur_sol_autrui_augmentation_nouveaux(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Constructions Sur sol d'autrui, Augmentations Acquisitions, créations, apports et virements de poste à poste  (KO)"


class is_immobilisations_corporelles_constructions_sur_sol_autrui_diminution_poste_a_poste(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Constructions Sur sol d'autrui, Diminutions par virement de poste à poste (IR)"


class is_immobilisations_corporelles_constructions_sur_sol_autrui_diminution_cession_hors_services(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Constructions Sur sol d'autrui, Diminutions par cession à des tiers ou mises hors services (MD)"


class is_immobilisations_corporelles_constructions_sur_sol_autrui_brute_fin_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Constructions Sur sol d'autrui, Valeur brute des immobilisations à la fin de l'exercice (ME)"


class is_immobilisations_corporelles_constructions_sur_sol_autrui_origine_reevaluees_fin_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Constructions Sur sol d'autrui, Valeur d'origine des immobilisations réévaluées en fin d'exercice (MF)"


# Installations générales, agencements et aménagements des constructions
class is_immobilisations_corporelles_constructions_installations_amenagements_brute_debut_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Installations générales, agencements et aménagements des constructions, Valeur brute des immobilisations au début de l'exercice (KP)"


class is_immobilisations_corporelles_constructions_installations_amenagements_augmentation_reevaluation(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Installations générales, agencements et aménagements des constructions, Augmentations Consécutives à une réévaluation pratiquée au cours de l'exercice (KQ)"


class is_immobilisations_corporelles_constructions_installations_amenagements_augmentation_nouveaux(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Installations générales, agencements et aménagements des constructions, Augmentations Acquisitions, créations, apports et virements de poste à poste  (KR)"


class is_immobilisations_corporelles_constructions_installations_amenagements_diminution_poste_a_poste(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Installations générales, agencements et aménagements des constructions, Diminutions par virement de poste à poste (IS)"


class is_immobilisations_corporelles_constructions_installations_amenagements_diminution_cession_hors_services(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Installations générales, agencements et aménagements des constructions, Diminutions par cession à des tiers ou mises hors services (MG)"


class is_immobilisations_corporelles_constructions_installations_amenagements_brute_fin_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Installations générales, agencements et aménagements des constructions, Valeur brute des immobilisations à la fin de l'exercice (MH)"


class is_immobilisations_corporelles_constructions_installations_amenagements_origine_reevaluees_fin_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Installations générales, agencements et aménagements des constructions, Valeur d'origine des immobilisations réévaluées en fin d'exercice (MI)"


# Installations techniques, matériel et outillages industriels
class is_immobilisations_corporelles_installations_materiel_industriel_brute_debut_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Installations techniques, matériel et outillages industriels, Valeur brute des immobilisations au début de l'exercice (KS)"


class is_immobilisations_corporelles_installations_materiel_industriel_augmentation_reevaluation(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Installations techniques, matériel et outillages industriels, Augmentations Consécutives à une réévaluation pratiquée au cours de l'exercice (KT)"


class is_immobilisations_corporelles_installations_materiel_industriel_augmentation_nouveaux(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Installations techniques, matériel et outillages industriels, Augmentations Acquisitions, créations, apports et virements de poste à poste  (KU)"


class is_immobilisations_corporelles_installations_materiel_industriel_diminution_poste_a_poste(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Installations techniques, matériel et outillages industriels, Diminutions par virement de poste à poste (IT)"


class is_immobilisations_corporelles_installations_materiel_industriel_diminution_cession_hors_services(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Installations techniques, matériel et outillages industriels, Diminutions par cession à des tiers ou mises hors services (MJ)"


class is_immobilisations_corporelles_installations_materiel_industriel_brute_fin_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Installations techniques, matériel et outillages industriels, Valeur brute des immobilisations à la fin de l'exercice (MK)"


class is_immobilisations_corporelles_installations_materiel_industriel_origine_reevaluees_fin_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Installations techniques, matériel et outillages industriels, Valeur d'origine des immobilisations réévaluées en fin d'exercice (ML)"


# Autres, Installations générales, agencements et aménagements divers
class is_immobilisations_corporelles_autres_installations_amenagements_brute_debut_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Autres, Installations générales, agencements et aménagements divers, Valeur brute des immobilisations au début de l'exercice (KV)"


class is_immobilisations_corporelles_autres_installations_amenagements_augmentation_reevaluation(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Autres, Installations générales, agencements et aménagements divers, Augmentations Consécutives à une réévaluation pratiquée au cours de l'exercice (KW)"


class is_immobilisations_corporelles_autres_installations_amenagements_augmentation_nouveaux(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Autres, Installations générales, agencements et aménagements divers, Augmentations Acquisitions, créations, apports et virements de poste à poste  (KX)"


class is_immobilisations_corporelles_autres_installations_amenagements_diminution_poste_a_poste(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Autres, Installations générales, agencements et aménagements divers, Diminutions par virement de poste à poste (IU)"


class is_immobilisations_corporelles_autres_installations_amenagements_diminution_cession_hors_services(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Autres, Installations générales, agencements et aménagements divers, Diminutions par cession à des tiers ou mises hors services (MM)"


class is_immobilisations_corporelles_autres_installations_amenagements_brute_fin_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Autres, Installations générales, agencements et aménagements divers, Valeur brute des immobilisations à la fin de l'exercice (MN)"


class is_immobilisations_corporelles_autres_installations_amenagements_origine_reevaluees_fin_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Autres, Installations générales, agencements et aménagements divers, Valeur d'origine des immobilisations réévaluées en fin d'exercice (MO)"


# Autres, Matériel de transport
class is_immobilisations_corporelles_autres_materiel_transport_brute_debut_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Autres, Matériel de transport, Valeur brute des immobilisations au début de l'exercice (KY)"


class is_immobilisations_corporelles_autres_materiel_transport_augmentation_reevaluation(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Autres, Matériel de transport, Augmentations Consécutives à une réévaluation pratiquée au cours de l'exercice (KZ)"


class is_immobilisations_corporelles_autres_materiel_transport_augmentation_nouveaux(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Autres, Matériel de transport, Augmentations Acquisitions, créations, apports et virements de poste à poste  (LA)"


class is_immobilisations_corporelles_autres_materiel_transport_diminution_poste_a_poste(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Autres, Matériel de transport, Diminutions par virement de poste à poste (IV)"


class is_immobilisations_corporelles_autres_materiel_transport_diminution_cession_hors_services(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Autres, Matériel de transport, Diminutions par cession à des tiers ou mises hors services (MP)"


class is_immobilisations_corporelles_autres_materiel_transport_brute_fin_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Autres, Matériel de transport, Valeur brute des immobilisations à la fin de l'exercice (MQ)"


class is_immobilisations_corporelles_autres_materiel_transport_origine_reevaluees_fin_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Autres, Matériel de transport, Valeur d'origine des immobilisations réévaluées en fin d'exercice (MR)"


# Autres, Matériel de bureau et informatique, mobilier
class is_immobilisations_corporelles_autres_materiel_bureau_brute_debut_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Autres, Matériel de bureau et informatique, mobilier, Valeur brute des immobilisations au début de l'exercice (LB)"


class is_immobilisations_corporelles_autres_materiel_bureau_augmentation_reevaluation(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Autres, Matériel de bureau et informatique, mobilier, Augmentations Consécutives à une réévaluation pratiquée au cours de l'exercice (LC)"


class is_immobilisations_corporelles_autres_materiel_bureau_augmentation_nouveaux(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Autres, Matériel de bureau et informatique, mobilier, Augmentations Acquisitions, créations, apports et virements de poste à poste  (LD)"


class is_immobilisations_corporelles_autres_materiel_bureau_diminution_poste_a_poste(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Autres, Matériel de bureau et informatique, mobilier, Diminutions par virement de poste à poste (IW)"


class is_immobilisations_corporelles_autres_materiel_bureau_diminution_cession_hors_services(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Autres, Matériel de bureau et informatique, mobilier, Diminutions par cession à des tiers ou mises hors services (MS)"


class is_immobilisations_corporelles_autres_materiel_bureau_brute_fin_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Autres, Matériel de bureau et informatique, mobilier, Valeur brute des immobilisations à la fin de l'exercice (MT)"


class is_immobilisations_corporelles_autres_materiel_bureau_origine_reevaluees_fin_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Autres, Matériel de bureau et informatique, mobilier, Valeur d'origine des immobilisations réévaluées en fin d'exercice (MU)"


# Autres, Emballages récupérables et divers
class is_immobilisations_corporelles_autres_emballages_brute_debut_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Autres, Emballages récupérables et divers, Valeur brute des immobilisations au début de l'exercice (LE)"


class is_immobilisations_corporelles_autres_emballages_augmentation_reevaluation(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Autres, Emballages récupérables et divers, Augmentations Consécutives à une réévaluation pratiquée au cours de l'exercice (LF)"


class is_immobilisations_corporelles_autres_emballages_augmentation_nouveaux(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Autres, Emballages récupérables et divers, Augmentations Acquisitions, créations, apports et virements de poste à poste  (LG)"


class is_immobilisations_corporelles_autres_emballages_diminution_poste_a_poste(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Autres, Emballages récupérables et divers, Diminutions par virement de poste à poste (IX)"


class is_immobilisations_corporelles_autres_emballages_diminution_cession_hors_services(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Autres, Emballages récupérables et divers, Diminutions par cession à des tiers ou mises hors services (MV)"


class is_immobilisations_corporelles_autres_emballages_brute_fin_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Autres, Emballages récupérables et divers, Valeur brute des immobilisations à la fin de l'exercice (MW)"


class is_immobilisations_corporelles_autres_emballages_origine_reevaluees_fin_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Autres, Emballages récupérables et divers, Valeur d'origine des immobilisations réévaluées en fin d'exercice (MX)"


# Immobilisations corporelles en cours
class is_immobilisations_corporelles_en_cours_brute_debut_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations corporelles en cours, Valeur brute des immobilisations au début de l'exercice (LH)"


class is_immobilisations_corporelles_en_cours_augmentation_reevaluation(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations corporelles en cours, Augmentations Consécutives à une réévaluation pratiquée au cours de l'exercice (LI)"


class is_immobilisations_corporelles_en_cours_augmentation_nouveaux(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations corporelles en cours, Augmentations Acquisitions, créations, apports et virements de poste à poste  (LJ)"


class is_immobilisations_corporelles_en_cours_diminution_poste_a_poste(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations corporelles en cours, Diminutions par virement de poste à poste (MY)"


class is_immobilisations_corporelles_en_cours_diminution_cession_hors_services(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations corporelles en cours, Diminutions par cession à des tiers ou mises hors services (MZ)"


class is_immobilisations_corporelles_en_cours_brute_fin_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations corporelles en cours, Valeur brute des immobilisations à la fin de l'exercice (NA)"


class is_immobilisations_corporelles_en_cours_origine_reevaluees_fin_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations corporelles en cours, Valeur d'origine des immobilisations réévaluées en fin d'exercice (NB)"


# Avances et acomptes
class is_immobilisations_corporelles_avances_brute_debut_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Avances et acomptes, Valeur brute des immobilisations au début de l'exercice (LK)"


class is_immobilisations_corporelles_avances_augmentation_reevaluation(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Avances et acomptes, Augmentations Consécutives à une réévaluation pratiquée au cours de l'exercice (LL)"


class is_immobilisations_corporelles_avances_augmentation_nouveaux(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Avances et acomptes, Augmentations Acquisitions, créations, apports et virements de poste à poste  (LM)"


class is_immobilisations_corporelles_avances_diminution_poste_a_poste(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Avances et acomptes, Diminutions par virement de poste à poste (NC)"


class is_immobilisations_corporelles_avances_diminution_cession_hors_services(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Avances et acomptes, Diminutions par cession à des tiers ou mises hors services (ND)"


class is_immobilisations_corporelles_avances_brute_fin_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Avances et acomptes, Valeur brute des immobilisations à la fin de l'exercice (NE)"


class is_immobilisations_corporelles_avances_origine_reevaluees_fin_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Avances et acomptes, Valeur d'origine des immobilisations réévaluées en fin d'exercice (NF)"


# Total III
class is_immobilisations_total_corporelles_brute_debut_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Total immobilisations corporelles, Valeur brute des immobilisations au début de l'exercice (LN)"

    def formula(person, period):
        immo_terrains = person('is_immobilisations_corporelles_terrains_brute_debut_exercice', period)
        immo_sol_propre = person('is_immobilisations_corporelles_constructions_sur_sol_propre_brute_debut_exercice', period)
        immo_sol_autrui = person('is_immobilisations_corporelles_constructions_sur_sol_autrui_brute_debut_exercice', period)
        immo_installations = person('is_immobilisations_corporelles_constructions_installations_amenagements_brute_debut_exercice', period)
        immo_materiel_industriel = person('is_immobilisations_corporelles_installations_materiel_industriel_brute_debut_exercice', period)
        immo_autres_installations = person('is_immobilisations_corporelles_autres_installations_amenagements_brute_debut_exercice', period)
        immo_autres_transport = person('is_immobilisations_corporelles_autres_materiel_transport_brute_debut_exercice', period)
        immo_autres_bureau = person('is_immobilisations_corporelles_autres_materiel_bureau_brute_debut_exercice', period)
        immo_autres_emballage = person('is_immobilisations_corporelles_autres_emballages_brute_debut_exercice', period)
        immo_en_cours = person('is_immobilisations_corporelles_en_cours_brute_debut_exercice', period)
        immo_avances = person('is_immobilisations_corporelles_avances_brute_debut_exercice', period)
        return immo_terrains + immo_sol_propre + immo_sol_autrui + immo_installations + immo_materiel_industriel + immo_autres_installations + immo_autres_transport + immo_autres_bureau + immo_autres_emballage + immo_en_cours + immo_avances


class is_immobilisations_total_corporelles_augmentation_reevaluation(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Total immobilisations corporelles, Augmentations Consécutives à une réévaluation pratiquée au cours de l'exercice (LO)"

    def formula(person, period):
        immo_terrains = person('is_immobilisations_corporelles_terrains_augmentation_reevaluation', period)
        immo_sol_propre = person('is_immobilisations_corporelles_constructions_sur_sol_propre_augmentation_reevaluation', period)
        immo_sol_autrui = person('is_immobilisations_corporelles_constructions_sur_sol_autrui_augmentation_reevaluation', period)
        immo_installations = person('is_immobilisations_corporelles_constructions_installations_amenagements_augmentation_reevaluation', period)
        immo_materiel_industriel = person('is_immobilisations_corporelles_installations_materiel_industriel_augmentation_reevaluation', period)
        immo_autres_installations = person('is_immobilisations_corporelles_autres_installations_amenagements_augmentation_reevaluation', period)
        immo_autres_transport = person('is_immobilisations_corporelles_autres_materiel_transport_augmentation_reevaluation', period)
        immo_autres_bureau = person('is_immobilisations_corporelles_autres_materiel_bureau_augmentation_reevaluation', period)
        immo_autres_emballage = person('is_immobilisations_corporelles_autres_emballages_augmentation_reevaluation', period)
        immo_en_cours = person('is_immobilisations_corporelles_en_cours_augmentation_reevaluation', period)
        immo_avances = person('is_immobilisations_corporelles_avances_augmentation_reevaluation', period)
        return immo_terrains + immo_sol_propre + immo_sol_autrui + immo_installations + immo_materiel_industriel + immo_autres_installations + immo_autres_transport + immo_autres_bureau + immo_autres_emballage + immo_en_cours + immo_avances


class is_immobilisations_total_corporelles_augmentation_nouveaux(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Total immobilisations corporelles, Augmentations Acquisitions, créations, apports et virements de poste à poste (LP)"

    def formula(person, period):
        immo_terrains = person('is_immobilisations_corporelles_terrains_augmentation_nouveaux', period)
        immo_sol_propre = person('is_immobilisations_corporelles_constructions_sur_sol_propre_augmentation_nouveaux', period)
        immo_sol_autrui = person('is_immobilisations_corporelles_constructions_sur_sol_autrui_augmentation_nouveaux', period)
        immo_installations = person('is_immobilisations_corporelles_constructions_installations_amenagements_augmentation_nouveaux', period)
        immo_materiel_industriel = person('is_immobilisations_corporelles_installations_materiel_industriel_augmentation_nouveaux', period)
        immo_autres_installations = person('is_immobilisations_corporelles_autres_installations_amenagements_augmentation_nouveaux', period)
        immo_autres_transport = person('is_immobilisations_corporelles_autres_materiel_transport_augmentation_nouveaux', period)
        immo_autres_bureau = person('is_immobilisations_corporelles_autres_materiel_bureau_augmentation_nouveaux', period)
        immo_autres_emballage = person('is_immobilisations_corporelles_autres_emballages_augmentation_nouveaux', period)
        immo_en_cours = person('is_immobilisations_corporelles_en_cours_augmentation_nouveaux', period)
        immo_avances = person('is_immobilisations_corporelles_avances_augmentation_nouveaux', period)
        return immo_terrains + immo_sol_propre + immo_sol_autrui + immo_installations + immo_materiel_industriel + immo_autres_installations + immo_autres_transport + immo_autres_bureau + immo_autres_emballage + immo_en_cours + immo_avances


class is_immobilisations_total_corporelles_diminution_poste_a_poste(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Total immobilisations corporelles, Diminutions par virement de poste à poste (IY)"

    def formula(person, period):
        immo_terrains = person('is_immobilisations_corporelles_terrains_diminution_poste_a_poste', period)
        immo_sol_propre = person('is_immobilisations_corporelles_constructions_sur_sol_propre_diminution_poste_a_poste', period)
        immo_sol_autrui = person('is_immobilisations_corporelles_constructions_sur_sol_autrui_diminution_poste_a_poste', period)
        immo_installations = person('is_immobilisations_corporelles_constructions_installations_amenagements_diminution_poste_a_poste', period)
        immo_materiel_industriel = person('is_immobilisations_corporelles_installations_materiel_industriel_diminution_poste_a_poste', period)
        immo_autres_installations = person('is_immobilisations_corporelles_autres_installations_amenagements_diminution_poste_a_poste', period)
        immo_autres_transport = person('is_immobilisations_corporelles_autres_materiel_transport_diminution_poste_a_poste', period)
        immo_autres_bureau = person('is_immobilisations_corporelles_autres_materiel_bureau_diminution_poste_a_poste', period)
        immo_autres_emballage = person('is_immobilisations_corporelles_autres_emballages_diminution_poste_a_poste', period)
        immo_en_cours = person('is_immobilisations_corporelles_en_cours_diminution_poste_a_poste', period)
        immo_avances = person('is_immobilisations_corporelles_avances_diminution_poste_a_poste', period)
        return immo_terrains + immo_sol_propre + immo_sol_autrui + immo_installations + immo_materiel_industriel + immo_autres_installations + immo_autres_transport + immo_autres_bureau + immo_autres_emballage + immo_en_cours + immo_avances


class is_immobilisations_total_corporelles_diminution_cession_hors_services(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Total immobilisations corporelles, Diminutions par cession à des tiers ou mises hors services (NG)"

    def formula(person, period):
        immo_terrains = person('is_immobilisations_corporelles_terrains_diminution_cession_hors_services', period)
        immo_sol_propre = person('is_immobilisations_corporelles_constructions_sur_sol_propre_diminution_cession_hors_services', period)
        immo_sol_autrui = person('is_immobilisations_corporelles_constructions_sur_sol_autrui_diminution_cession_hors_services', period)
        immo_installations = person('is_immobilisations_corporelles_constructions_installations_amenagements_diminution_cession_hors_services', period)
        immo_materiel_industriel = person('is_immobilisations_corporelles_installations_materiel_industriel_diminution_cession_hors_services', period)
        immo_autres_installations = person('is_immobilisations_corporelles_autres_installations_amenagements_diminution_cession_hors_services', period)
        immo_autres_transport = person('is_immobilisations_corporelles_autres_materiel_transport_diminution_cession_hors_services', period)
        immo_autres_bureau = person('is_immobilisations_corporelles_autres_materiel_bureau_diminution_cession_hors_services', period)
        immo_autres_emballage = person('is_immobilisations_corporelles_autres_emballages_diminution_cession_hors_services', period)
        immo_en_cours = person('is_immobilisations_corporelles_en_cours_diminution_cession_hors_services', period)
        immo_avances = person('is_immobilisations_corporelles_avances_diminution_cession_hors_services', period)
        return immo_terrains + immo_sol_propre + immo_sol_autrui + immo_installations + immo_materiel_industriel + immo_autres_installations + immo_autres_transport + immo_autres_bureau + immo_autres_emballage + immo_en_cours + immo_avances


class is_immobilisations_total_corporelles_brute_fin_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Total immobilisations corporelles, Valeur brute des immobilisations à la fin de l'exercice (NH)"

    def formula(person, period):
        immo_terrains = person('is_immobilisations_corporelles_terrains_brute_fin_exercice', period)
        immo_sol_propre = person('is_immobilisations_corporelles_constructions_sur_sol_propre_brute_fin_exercice', period)
        immo_sol_autrui = person('is_immobilisations_corporelles_constructions_sur_sol_autrui_brute_fin_exercice', period)
        immo_installations = person('is_immobilisations_corporelles_constructions_installations_amenagements_brute_fin_exercice', period)
        immo_materiel_industriel = person('is_immobilisations_corporelles_installations_materiel_industriel_brute_fin_exercice', period)
        immo_autres_installations = person('is_immobilisations_corporelles_autres_installations_amenagements_brute_fin_exercice', period)
        immo_autres_transport = person('is_immobilisations_corporelles_autres_materiel_transport_brute_fin_exercice', period)
        immo_autres_bureau = person('is_immobilisations_corporelles_autres_materiel_bureau_brute_fin_exercice', period)
        immo_autres_emballage = person('is_immobilisations_corporelles_autres_emballages_brute_fin_exercice', period)
        immo_en_cours = person('is_immobilisations_corporelles_en_cours_brute_fin_exercice', period)
        immo_avances = person('is_immobilisations_corporelles_avances_brute_fin_exercice', period)
        return immo_terrains + immo_sol_propre + immo_sol_autrui + immo_installations + immo_materiel_industriel + immo_autres_installations + immo_autres_transport + immo_autres_bureau + immo_autres_emballage + immo_en_cours + immo_avances


class is_immobilisations_total_corporelles_origine_reevaluees_fin_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Total immobilisations corporelles, Valeur d'origine des immobilisations réévaluées en fin d'exercice (NI)"

    def formula(person, period):
        immo_terrains = person('is_immobilisations_corporelles_terrains_origine_reevaluees_fin_exercice', period)
        immo_sol_propre = person('is_immobilisations_corporelles_constructions_sur_sol_propre_origine_reevaluees_fin_exercice', period)
        immo_sol_autrui = person('is_immobilisations_corporelles_constructions_sur_sol_autrui_origine_reevaluees_fin_exercice', period)
        immo_installations = person('is_immobilisations_corporelles_constructions_installations_amenagements_origine_reevaluees_fin_exercice', period)
        immo_materiel_industriel = person('is_immobilisations_corporelles_installations_materiel_industriel_origine_reevaluees_fin_exercice', period)
        immo_autres_installations = person('is_immobilisations_corporelles_autres_installations_amenagements_origine_reevaluees_fin_exercice', period)
        immo_autres_transport = person('is_immobilisations_corporelles_autres_materiel_transport_origine_reevaluees_fin_exercice', period)
        immo_autres_bureau = person('is_immobilisations_corporelles_autres_materiel_bureau_origine_reevaluees_fin_exercice', period)
        immo_autres_emballage = person('is_immobilisations_corporelles_autres_emballages_origine_reevaluees_fin_exercice', period)
        immo_en_cours = person('is_immobilisations_corporelles_en_cours_origine_reevaluees_fin_exercice', period)
        immo_avances = person('is_immobilisations_corporelles_avances_origine_reevaluees_fin_exercice', period)
        return immo_terrains + immo_sol_propre + immo_sol_autrui + immo_installations + immo_materiel_industriel + immo_autres_installations + immo_autres_transport + immo_autres_bureau + immo_autres_emballage + immo_en_cours + immo_avances
