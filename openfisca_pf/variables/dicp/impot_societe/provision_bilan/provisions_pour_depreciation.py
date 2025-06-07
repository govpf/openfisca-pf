# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.base import (
    Variable,
    YEAR
    )
from openfisca_pf.entities import Personne


class is_provision_sur_immobilisations_incorporelles_montant_au_debut_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision sur immobilisations incorporelles montant au début de l'exercice (6A)"


class is_provision_sur_immobilisations_incorporelles_augmentations_dotations_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision sur immobilisations incorporelles augmentations dotations de l'exercice (6B)"


class is_provision_sur_immobilisations_incorporelles_diminutions_reprises_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision sur immobilisations incorporelles diminutions reprises de l'exercice (6C)"


class is_provision_sur_immobilisations_incorporelles_montant_a_la_fin_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision sur immobilisations incorporelles montant à la fin de l'exercice (6D)"


class is_provision_sur_immobilisations_corporelles_montant_au_debut_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision sur immobilisations corporelles montant au début de l'exercice (6E)"


class is_provision_sur_immobilisations_corporelles_augmentations_dotations_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision sur immobilisations corporelles augmentations dotations de l'exercice (6F)"


class is_provision_sur_immobilisations_corporelles_diminutions_reprises_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision sur immobilisations corporelles diminutions reprises de l'exercice (6G)"


class is_provision_sur_immobilisations_corporelles_montant_a_la_fin_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision sur immobilisations corporelles montant à la fin de l'exercice (6H)"


class is_provision_sur_immobilisations_autres_immobilisations_financieres_montant_au_debut_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision sur immobilisations autres immobilisations financières montant au début de l'exercice (6J)"


class is_provision_sur_immobilisations_autres_immobilisations_financieres_augmentations_dotations_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision sur immobilisations autres immobilisations financières augmentations dotations de l'exercice (6K)"


class is_provision_sur_immobilisations_autres_immobilisations_financieres_diminutions_reprises_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision sur immobilisations autres immobilisations financières diminutions reprises de l'exercice (6L)"


class is_provision_sur_immobilisations_autres_immobilisations_financieres_montant_a_la_fin_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision sur immobilisations autres immobilisations financières montant à la fin de l'exercice (6M)"


class is_provision_sur_stocks_et_en_cours_montant_au_debut_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision sur stocks et en cours montant au début de l'exercice (6N)"


class is_provision_sur_stocks_et_en_cours_augmentations_dotations_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision sur stocks et en cours augmentations dotations de l'exercice (6P)"


class is_provision_sur_stocks_et_en_cours_diminutions_reprises_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision sur stocks et en cours diminutions reprises de l'exercice (6R)"


class is_provision_sur_stocks_et_en_cours_montant_a_la_fin_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision sur stocks et en cours montant à la fin de l'exercice (6S)"


class is_provision_sur_comptes_clients_montant_au_debut_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision sur comptes clients montant au début de l'exercice (6T)"


class is_provision_sur_comptes_clients_augmentations_dotations_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision sur comptes clients augmentations dotations de l'exercice (6U)"


class is_provision_sur_comptes_clients_diminutions_reprises_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision sur comptes clients diminutions reprises de l'exercice (6V)"


class is_provision_sur_comptes_clients_montant_a_la_fin_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision sur comptes clients montant à la fin de l'exercice (6W)"


class is_provision_autres_provisions_pour_depreciation_montant_au_debut_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision autres provisions pour dépréciation montant au début de l'exercice (6X)"


class is_provision_autres_provisions_pour_depreciation_augmentations_dotations_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision autres provisions pour dépréciation augmentations dotations de l'exercice (6Y)"


class is_provision_autres_provisions_pour_depreciation_diminutions_reprises_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision autres provisions pour dépréciation diminutions reprises de l'exercice (6Z)"


class is_provision_autres_provisions_pour_depreciation_montant_a_la_fin_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision autres provisions pour dépréciation montant à la fin de l'exercice (7A)"
