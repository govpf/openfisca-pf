# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.base import (
    Variable,
    YEAR
    )
from openfisca_pf.entities import Personne


# Frais d'établissement, de recherche et de développements
class is_immobilisations_incorporelles_frais_etablissement_r_et_d_brute_debut_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Frais d'établissement, de recherche et de développements, Valeur brute des immobilisations au début de l'exercice (KA)"


class is_immobilisations_incorporelles_frais_etablissement_r_et_d_augmentation_reevaluation(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Frais d'établissement, de recherche et de développements, Augmentations Consécutives à une réévaluation pratiquée au cours de l'exercice (KB)"


class is_immobilisations_incorporelles_frais_etablissement_r_et_d_augmentation_nouveaux(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Frais d'établissement, de recherche et de développements, Augmentations Acquisitions, créations, apports et virements de poste à poste  (KC)"


class is_immobilisations_incorporelles_frais_etablissement_r_et_d_diminution_poste_a_poste(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Frais d'établissement, Diminutions par virement de poste à poste (IN)"


class is_immobilisations_incorporelles_frais_etablissement_r_et_d_diminution_cession_hors_services(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Frais d'établissement, Diminutions par cession à des tiers ou mises hors services (LT)"


class is_immobilisations_incorporelles_frais_etablissement_r_et_d_brute_fin_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Frais d'établissement, Valeur brute des immobilisations à la fin de l'exercice (LU)"


class is_immobilisations_incorporelles_frais_etablissement_r_et_d_origine_reevaluees_fin_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Frais d'établissement, Valeur d'origine des immobilisations réévaluées en fin d'exercice (1W)"


# Autres postes d'immobilisations incorporelles
class is_immobilisations_incorporelles_autres_brute_debut_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Autres postes d'immobilisations incorporelles, Valeur brute des immobilisations au début de l'exercice (KD)"


class is_immobilisations_incorporelles_autres_augmentation_reevaluation(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Autres postes d'immobilisations incorporelles, Augmentations Consécutives à une réévaluation pratiquée au cours de l'exercice (KE)"


class is_immobilisations_incorporelles_autres_augmentation_nouveaux(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Autres postes d'immobilisations incorporelles, Augmentations Acquisitions, créations, apports et virements de poste à poste (KF)"


class is_immobilisations_incorporelles_autres_diminution_poste_a_poste(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Autres postes d'immobilisations incorporelles, Diminutions par virement de poste à poste (IO)"


class is_immobilisations_incorporelles_autres_diminution_cession_hors_services(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Autres postes d'immobilisations incorporelles, Diminutions par cession à des tiers ou mises hors services (LV)"


class is_immobilisations_incorporelles_autres_brute_fin_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Autres postes d'immobilisations incorporelles, Valeur brute des immobilisations à la fin de l'exercice (LW)"


class is_immobilisations_incorporelles_autres_origine_reevaluees_fin_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Autres postes d'immobilisations incorporelles, Valeur d'origine des immobilisations réévaluées en fin d'exercice (1X)"
