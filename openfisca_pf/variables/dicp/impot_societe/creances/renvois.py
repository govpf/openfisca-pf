# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.base import (
    Variable,
    DAY
    )
from openfisca_pf.entities import Personne


class is_creances_montant_des_pret_accordes_en_cours_d_exercice_montant_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Montant des prêts accordés en cours d'exercice (VD)"


class is_creances_montant_des_remboursements_obtenus_en_cours_d_exercice_montant_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Montant des remboursements obtenus en cours d'exercice (VE)"


class is_creances_prets_et_avances_consentis_aux_associes_montant_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Prêts et avances consentis aux associés (personnes physiques) (VF)"