# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.base import (
    Variable,
    YEAR
    )
from openfisca_pf.entities import Personne


class is_amortissements_charges_a_repartir_sur_plusieurs_exercices_montant_net_au_debut_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Mouvements de l'exercice affectant les charges réparties sur plusieurs exercices Charges à répartir sur plusieurs exercices montant net au debut de l'exercice"


class is_amortissements_charges_a_repartir_sur_plusieurs_exercices_augmentations(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Mouvements de l'exercice affectant les charges réparties sur plusieurs exercices Charges à répartir sur plusieurs exercices augmentations"


class is_amortissements_charges_a_repartir_sur_plusieurs_exercices_dotations_de_l_exercice_aux_amortissements(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Mouvements de l'exercice affectant les charges réparties sur plusieurs exercices Charges à répartir sur plusieurs exercices dotations de l'exercice aux amortissements (SM)"


class is_amortissements_charges_a_repartir_sur_plusieurs_exercices_montant_net_a_la_fin_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Mouvements de l'exercice affectant les charges réparties sur plusieurs exercices Charges à répartir sur plusieurs exercices montant net à la fin de l'exercice (SN)"