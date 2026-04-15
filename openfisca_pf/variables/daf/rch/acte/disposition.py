from openfisca_pf.base import (
    DAY,
    Variable
    )
from openfisca_pf.entities import Personne

class rectification(Variable):
    value_type = int
    entity = Personne
    default_value = 0
    label = "La disposition est une rectification"
    definition_period = DAY


class renonciation(Variable):
    value_type = int
    entity = Personne
    default_value = 0
    label = "La disposition est une renonciation"
    definition_period = DAY


class acte_complementaire(Variable):
    value_type = int
    entity = Personne
    default_value = 0
    label = "La disposition est un acte complémentaire"
    definition_period = DAY


class constitution_servitude(Variable):
    value_type = int
    entity = Personne
    default_value = 0
    label = "La disposition est une constitution de servitude"
    definition_period = DAY


class droit_acces(Variable):
    value_type = int
    entity = Personne
    default_value = 0
    label = "La disposition est un droit d'accès"
    definition_period = DAY


class depot_piece(Variable):
    value_type = int
    entity = Personne
    default_value = 0
    label = "La disposition est un dépôt de pièce"
    definition_period = DAY


class pacte_preference(Variable):
    value_type = int
    entity = Personne
    default_value = 0
    label = "La disposition est un pacte de préférence"
    definition_period = DAY


class etat_descriptif_division_reglement_copropriete(Variable):
    value_type = int
    entity = Personne
    default_value = 0
    label = "La disposition est un état descriptif de division et règlement de copropriété"
    definition_period = DAY


class modification_etat_descriptif_division_reglement_copropriete(Variable):
    value_type = int
    entity = Personne
    default_value = 0
    label = "La disposition est une modification de l'état descriptif de division et règlement de copropriété"
    definition_period = DAY


class cahier_charges(Variable):
    value_type = int
    entity = Personne
    default_value = 0
    label = "La disposition est un cahier des charges"
    definition_period = DAY


class modification_cahier_charges(Variable):
    value_type = int
    entity = Personne
    default_value = 0
    label = "La disposition est une modification du cahier des charges"
    definition_period = DAY


class avenant(Variable):
    value_type = int
    entity = Personne
    default_value = 0
    label = "La disposition est un avenant"
    definition_period = DAY


class echange(Variable):
    value_type = int
    entity = Personne
    default_value = 0
    label = "La disposition est un échange"
    definition_period = DAY


class renouvellement_autorisation_occupation_temporaire(Variable):
    value_type = int
    entity = Personne
    default_value = 0
    label = "La disposition est un renouvellement d'autorisation d'occupation temporaire"
    definition_period = DAY


class constatation_realisation_condition_suspensive(Variable):
    value_type = int
    entity = Personne
    default_value = 0
    label = "La disposition est une constatation de réalisation de condition suspensive"
    definition_period = DAY


class constatation(Variable):
    value_type = int
    entity = Personne
    default_value = 0
    label = "La disposition est une constatation"
    definition_period = DAY


class remploi(Variable):
    value_type = int
    entity = Personne
    default_value = 0
    label = "La disposition est un remploi"
    definition_period = DAY


class convention(Variable):
    value_type = int
    entity = Personne
    default_value = 0
    label = "La disposition est une convention"
    definition_period = DAY


class certificat_conformite(Variable):
    value_type = int
    entity = Personne
    default_value = 0
    label = "La disposition est un certificat de conformité"
    definition_period = DAY


class pacte_tontinier(Variable):
    value_type = int
    entity = Personne
    default_value = 0
    label = "La disposition est un pacte tontinier"
    definition_period = DAY


class reserve_droit_usage_habitation(Variable):
    value_type = int
    entity = Personne
    default_value = 0
    label = "La disposition est une réserve de droit d'usage et d'habitation"
    definition_period = DAY


class decision_justice(Variable):
    value_type = int
    entity = Personne
    default_value = 0
    label = "La disposition est une décision de justice"
    definition_period = DAY


class convention_divorce(Variable):
    value_type = int
    entity = Personne
    default_value = 0
    label = "La disposition est une convention de divorce"
    definition_period = DAY