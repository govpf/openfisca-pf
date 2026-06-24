# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.base import (
    Variable,
    YEAR
    )
from openfisca_pf.entities import Personne


class is_provision_pour_charges_sociales_et_fiscales_sur_conges_a_payer_montant_au_debut_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision pour charges sociales et fiscales sur congés à payer montant au debut de l'exercice (5R)"


class is_provision_pour_charges_sociales_et_fiscales_sur_conges_a_payer_augmentations_dotation_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision pour charges sociales et fiscales sur congés à payer augmentations dotation de l'exercice (5S)"


class is_provision_pour_charges_sociales_et_fiscales_sur_conges_a_payer_diminution_reprises_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision pour charges sociales et fiscales sur congés à payer diminution reprises de l'exercice (5T)"


class is_provision_pour_charges_sociales_et_fiscales_sur_conges_a_payer_montant_a_la_fin_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision pour charges sociales et fiscales sur congés à payer montant à la fin de l'exercice (5U)"


class is_provision_autres_provisions_pour_risques_et_charges_montant_au_debut_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision autres provisions pour risques et charges montant au debut de l'exercice(5V)"


class is_provision_autres_provisions_pour_risques_et_charges_augmentations_dotation_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision autres provisions pour risques et charges augmentations dotation de l'exercice (5W)"


class is_provision_autres_provisions_pour_risques_et_charges_diminution_reprises_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision autres provisions pour risques et charges diminution reprises de l'exercice (5X)"


class is_provision_autres_provisions_pour_risques_et_charges_montant_a_la_fin_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provision autres provisions pour risques et charges montant à la fin de l'exercice (5Y)"
