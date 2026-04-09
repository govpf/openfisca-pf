from openfisca_pf.base import (
    DAY,
    Variable
    )
from openfisca_pf.entities import Personne

class aide_juridictionnelle(Variable):
    value_type = int
    entity = Personne
    default_value = 0
    label = "L'acte bénéficie de l'aide juridictionnelle"
    definition_period = DAY


class acte_administratif_exonere(Variable):
    value_type = int
    entity = Personne
    default_value = 0
    label = "L'acte administratif est exonéré"
    definition_period = DAY


class programme_habitat_social(Variable):
    value_type = int
    entity = Personne
    default_value = 0
    label = "L'acte bénéficie du programme d'habitat social"
    definition_period = DAY


class etablissement_public(Variable):
    value_type = int
    entity = Personne
    default_value = 0
    label = "L'acte concerne un établissement public"
    definition_period = DAY


class aisi(Variable):
    value_type = int
    entity = Personne
    default_value = 0
    label = "L'acte bénéficie d'AISI"
    definition_period = DAY


class succesorale(Variable):
    value_type = int
    entity = Personne
    default_value = 0
    label = "L'acte est de nature successorale"
    definition_period = DAY


class defiscalisation_outre_mer(Variable):
    value_type = int
    entity = Personne
    default_value = 0
    label = "L'acte bénéficie de la défiscalisation outre-mer"
    definition_period = DAY


class collectivites(Variable):
    value_type = int
    entity = Personne
    default_value = 0
    label = "L'acte concerne les collectivités"
    definition_period = DAY


class comptable_public(Variable):
    value_type = int
    entity = Personne
    default_value = 0
    label = "L'acte concerne un comptable public"
    definition_period = DAY


class autre(Variable):
    value_type = int
    entity = Personne
    default_value = 0
    label = "L'acte bénéficie d'un autre régime de faveur"
    definition_period = DAY
