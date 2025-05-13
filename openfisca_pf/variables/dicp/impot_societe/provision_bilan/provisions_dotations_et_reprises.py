# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.base import (
    Variable,
    YEAR
    )
from openfisca_pf.entities import Personne


class is_provision_dont_dotations_et_reprises_d_exploitation_augmentations_dotations_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision dont dotations et reprises d'exploitation augmentations dotations de l'exercice (7D)"


class is_provision_dont_dotations_et_reprises_d_exploitation_diminutions_reprises_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision dont dotations et reprises d'exploitation diminutions reprises de l'exercice (7E)"


class is_provision_dont_dotations_et_reprises_financieres_augmentations_dotations_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision dont dotations et reprises financières augmentations dotations de l'exercice (7F)"


class is_provision_dont_dotations_et_reprises_financieres_diminutions_reprises_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision dont dotations et reprises financières diminutions reprises de l'exercice (7G)"


class is_provision_dont_dotations_et_reprises_exceptionnelles_augmentations_dotations_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision dont dotations et reprises exceptionnelles augmentations dotations de l'exercice (7H)"


class is_provision_dont_dotations_et_reprises_exceptionnelles_diminutions_reprises_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision dont dotations et reprises exceptionnelles diminutions reprises de l'exercice (7J)"
