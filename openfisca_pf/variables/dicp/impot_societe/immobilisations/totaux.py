from openfisca_core.model_api import YEAR, Variable
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import Personne


# Total GENERAL
class is_immobilisations_total_general_brute_debut_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Total immobilisations Général, Valeur brute des immobilisations au début de l'exercice (0G)"

    def formula(person, period):
        immo_incorporelle = person('is_immobilisations_incorporelles_frais_etablissement_r_et_d_brute_debut_exercice', period)
        immo_incorporelle_autres = person('is_immobilisations_incorporelles_autres_brute_debut_exercice', period)
        immo_corporelle = person('is_immobilisations_total_corporelles_brute_debut_exercice', period)
        immo_fincanciere = person('is_immobilisations_total_financieres_brute_debut_exercice', period)
        return immo_incorporelle + immo_incorporelle_autres + immo_corporelle + immo_fincanciere


class is_immobilisations_total_general_augmentation_reevaluation(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Total immobilisations Général, Augmentations Consécutives à une réévaluation pratiquée au cours de l'exercice (0H)"

    def formula(person, period):
        immo_incorporelle = person('is_immobilisations_incorporelles_frais_etablissement_r_et_d_augmentation_reevaluation', period)
        immo_incorporelle_autres = person('is_immobilisations_incorporelles_autres_augmentation_reevaluation', period)
        immo_corporelle = person('is_immobilisations_total_corporelles_augmentation_reevaluation', period)
        immo_fincanciere = person('is_immobilisations_total_financieres_augmentation_reevaluation', period)
        return immo_incorporelle + immo_incorporelle_autres + immo_corporelle + immo_fincanciere


class is_immobilisations_total_general_augmentation_nouveaux(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Total immobilisations Général, Augmentations Acquisitions, créations, apports et virements de poste à poste (0J)"

    def formula(person, period):
        immo_incorporelle = person('is_immobilisations_incorporelles_frais_etablissement_r_et_d_augmentation_nouveaux', period)
        immo_incorporelle_autres = person('is_immobilisations_incorporelles_autres_augmentation_nouveaux', period)
        immo_corporelle = person('is_immobilisations_total_corporelles_augmentation_nouveaux', period)
        immo_fincanciere = person('is_immobilisations_total_financieres_augmentation_nouveaux', period)
        return immo_incorporelle + immo_incorporelle_autres + immo_corporelle + immo_fincanciere


class is_immobilisations_total_general_diminution_poste_a_poste(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Total immobilisations Général, Diminutions par virement de poste à poste (I4)"

    def formula(person, period):
        immo_incorporelle = person('is_immobilisations_incorporelles_frais_etablissement_r_et_d_diminution_poste_a_poste', period)
        immo_incorporelle_autres = person('is_immobilisations_incorporelles_autres_diminution_poste_a_poste', period)
        immo_corporelle = person('is_immobilisations_total_corporelles_diminution_poste_a_poste', period)
        immo_fincanciere = person('is_immobilisations_total_financieres_diminution_poste_a_poste', period)
        return immo_incorporelle + immo_incorporelle_autres + immo_corporelle + immo_fincanciere


class is_immobilisations_total_general_diminution_cession_hors_services(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Total immobilisations Général, Diminutions par cession à des tiers ou mises hors services (0K)"

    def formula(person, period):
        immo_incorporelle = person('is_immobilisations_incorporelles_frais_etablissement_r_et_d_diminution_cession_hors_services', period)
        immo_incorporelle_autres = person('is_immobilisations_incorporelles_autres_diminution_cession_hors_services', period)
        immo_corporelle = person('is_immobilisations_total_corporelles_diminution_cession_hors_services', period)
        immo_fincanciere = person('is_immobilisations_total_financieres_diminution_cession_hors_services', period)
        return immo_incorporelle + immo_incorporelle_autres + immo_corporelle + immo_fincanciere


class is_immobilisations_total_general_brute_fin_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Total immobilisations Général, Valeur brute des immobilisations à la fin de l'exercice (0L)"

    def formula(person, period):
        immo_incorporelle = person('is_immobilisations_incorporelles_frais_etablissement_r_et_d_brute_fin_exercice', period)
        immo_incorporelle_autres = person('is_immobilisations_incorporelles_autres_brute_fin_exercice', period)
        immo_corporelle = person('is_immobilisations_total_corporelles_brute_fin_exercice', period)
        immo_fincanciere = person('is_immobilisations_total_financieres_brute_fin_exercice', period)
        return immo_incorporelle + immo_incorporelle_autres + immo_corporelle + immo_fincanciere


class is_immobilisations_total_general_origine_reevaluees_fin_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Total immobilisations Général, Valeur d'origine des immobilisations réévaluées en fin d'exercice (0M)"

    def formula(person, period):
        immo_incorporelle = person('is_immobilisations_incorporelles_frais_etablissement_r_et_d_origine_reevaluees_fin_exercice', period)
        immo_incorporelle_autres = person('is_immobilisations_incorporelles_autres_origine_reevaluees_fin_exercice', period)
        immo_corporelle = person('is_immobilisations_total_corporelles_origine_reevaluees_fin_exercice', period)
        immo_fincanciere = person('is_immobilisations_total_financieres_origine_reevaluees_fin_exercice', period)
        return immo_incorporelle + immo_incorporelle_autres + immo_corporelle + immo_fincanciere
