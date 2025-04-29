# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.base import (
    Variable,
    DAY
    )
from openfisca_pf.entities import Personne


class is_dettes_emprunts_souscrits_en_cours_d_exercice_montant_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes  Emprunts souscrits en cours d'exercice - Montant brut (VJ)"


class is_dettes_emprunts_rembourses_en_cours_d_exercice_montant_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes  Emprunts remboursés en cours d'exercice - Montant brut (VK)"


class is_dettes_montant_des_divers_emprunts_et_dettes_contractes_aupres_des_associes_personnes_physiques(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Dettes  Montant des divers emprunts et dettes contractés auprès des associés personnes physiques (VL)"