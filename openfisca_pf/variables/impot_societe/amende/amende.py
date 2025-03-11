# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import Personne
from openfisca_pf.base import (DAY, Variable)


class is_nombre_annexes_non_souscrites(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Nombre d'annexes non souscrites"
    reference = "https://www.impot-polynesie.gov.pf/code/2-sanctions-fiscales"


class is_annexes_non_souscrites_amende(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    unit = 'currency-XPF'
    label = "Montant amende pour annexes non souscrites"
    reference = "https://www.impot-polynesie.gov.pf/code/2-sanctions-fiscales"

    def formula(person: Personne, period, parameters):
        nbr_annexes = person('is_nombre_annexes_non_souscrites', period)
        montant_ammende = parameters(period).dicp.impot_societe.amende.annexe_non_souscrite
        return nbr_annexes * montant_ammende
