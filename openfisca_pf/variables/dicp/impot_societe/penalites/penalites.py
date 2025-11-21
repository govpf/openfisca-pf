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

        date_cloture = personne("date_cloture_exercice", period, parameters)[0].astype('M8[M]').astype(object)
        date_depot = personne("date_de_depot", period, parameters)[0].astype('M8[M]').astype(object)
        if date_cloture.month < 2:
           dlim = datetime.date(date_cloture.year, 7, 31)
        else:
            if date_cloture.month < 8:
                dlim = datetime.date(date_cloture.year + 1, 1, 31)
            else:
                dlim = datetime.date(date_cloture.year + 1, 7, 31)
        # Si Société → 0 mois, sinon → +1 mois
        delta = np.where(
          personne('est_societe', period), 0, 1)
        return ( 12 - dlim.month + date_depot.month + ((date_depot.year - dlim.year) - 1 ) * 12 ) - delta