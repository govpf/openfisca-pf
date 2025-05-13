# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.base import (
    Variable,
    YEAR
    )
from openfisca_pf.entities import Personne


class is_provision_reglementees_un_montant_au_debut_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision réglementées 1 montant au début de l'exercice (3T)"


class is_provision_reglementees_un_augmentations_dotations_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision réglementées 1 augmentations dotations de l'exercice"


class is_provision_reglementees_un_diminutions_reprises_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision réglementées 1 diminutions reprises de l'exercice"


class is_provision_reglementees_un_montant_a_la_fin_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision réglementées 1 montant à la fin de l'exercice"


class is_provision_reglementees_deux_montant_au_debut_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision réglementées 2 montant au début de l'exercice (3U)"


class is_provision_reglementees_deux_augmentations_dotations_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision réglementées 2 augmentations dotations de l'exercice"


class is_provision_reglementees_deux_diminutions_reprises_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision réglementées 2 diminutions reprises de l'exercice"


class is_provision_reglementees_deux_montant_a_la_fin_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision réglementées 2 montant à la fin de l'exercice"


class is_provision_reglementees_autres_provisions_reglementees_montant_au_debut_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision réglementées autres provisions réglementées montant au début de l'exercice (3Y)"


class is_provision_reglementees_autres_provisions_reglementees_augmentations_dotations_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision réglementées autres provisions réglementées augmentations dotations de l'exercice (TP)"


class is_provision_reglementees_autres_provisions_reglementees_diminutions_reprises_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision réglementées autres provisions réglementées diminutions reprises de l'exercice (TQ)"


class is_provision_reglementees_autres_provisions_reglementees_montant_a_la_fin_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision réglementées autres provisions réglementées montant à la fin de l'exercice (TR)"