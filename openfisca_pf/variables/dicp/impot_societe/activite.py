from openfisca_pf.base import *
from openfisca_pf.entities import Personne
from openfisca_pf.enums.impot_societe.activite import *


# TODO demander au PO la reference
class is_taux_activite(Variable):
    value_type = Enum
    possible_values = ActiviteTauxIS
    default_value = ActiviteTauxIS.NORMALE
    entity = Personne
    definition_period = ETERNITY
    label = "Liste des activités pour l'impôt sur les sociétés"
    reference = "TODO"
