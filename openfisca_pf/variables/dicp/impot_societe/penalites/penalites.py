import datetime

from openfisca_pf.base import (
    ArrayLike,
    date,
    max_,
    ParameterNode,
    Period,
    Population,
    select,
    Variable,
    YEAR
    )
from openfisca_pf.entities import Personne
from openfisca_pf.enums.geographie import *
from openfisca_pf.functions.currency import arrondi_inferieur
from dateutil.relativedelta import relativedelta
import numpy as np
from openfisca_pf.functions.time import (
    annee_de_la_date,
    as_date,
    as_duration,
    relative_delta_months,
    relative_delta_days
    )

class date_de_depot(Variable):
    value_type = date
    entity = Personne
    definition_period = YEAR
    default_value = date(1970, 1, 1)
    label = "Date de dépot de la déclaration d'impôt sur les sociétés"


class date_cloture_exercice(Variable):
    value_type = date
    entity = Personne
    definition_period = YEAR
    default_value = date(1970, 1, 1)
    label = "Date de clôture de l'exercice comptable"


class nombre_mois_retard_is(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Nombre de mois de retard de depot de la declaration"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:

        monthDateCloture = personne("date_cloture_exercice", period, parameters)[0].astype('M8[M]').astype(object).month
        yearDateCloture = personne("date_cloture_exercice", period, parameters)[0].astype('M8[Y]').astype(object).year
        monthDateDepot = personne("date_de_depot", period, parameters)[0].astype('M8[M]').astype(object).month
        yearDateDepot = personne("date_de_depot", period, parameters)[0].astype('M8[M]').astype(object).year
        if monthDateCloture < 2:
           dlim = datetime.date(yearDateCloture, 7, 31)
        else:
            if monthDateCloture < 8:
                dlim = datetime.date(yearDateCloture + 1, 1, 31)
            else:
                dlim = datetime.date(yearDateCloture + 1, 7, 31)
        # Si Société → 0 mois, sinon → +1 mois
        # On fabrique un array de relativedelta (objet) compatible avec l'addition OpenFisca
        delta = np.where(
          personne('est_societe', period),
          0,  # +0 mois
          1  # +1 mois
          )
        return ( 12 - dlim.month + monthDateDepot + ((yearDateDepot - dlim.year) - 1 ) * 12 ) - delta