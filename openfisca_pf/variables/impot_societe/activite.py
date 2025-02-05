from openfisca_core.model_api import ETERNITY, Variable, Enum
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import Personne
from openfisca_pf.enums.impot_societe.domaine_activite import *

class domaine_activite(Variable):
    value_type = Enum
    possible_values = DomaineActivite
    default_value = DomaineActivite.EXON_SOCIETES_EXPORTATRICES
    entity = Personne
    definition_period = ETERNITY
    label = "Domaine d'activité principal de la société"
    reference = "domaine_activiteFISC"