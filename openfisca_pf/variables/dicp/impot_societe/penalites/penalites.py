import datetime

from openfisca_pf.base import (
    ArrayLike,
    date,
    ParameterNode,
    Period,
    Population,
    Variable,
    DAY
    )
from openfisca_pf.entities import Personne
import numpy as np


class is_cessation_activite(Variable):
    value_type = bool
    entity = Personne
    definition_period = DAY
    default_value = False
    label = "Indique si le contribuable est en cessation d'activité"


class is_date_de_depot(Variable):
    value_type = date
    entity = Personne
    definition_period = DAY
    default_value = date(1970, 1, 1)
    label = "Date de dépot de la déclaration d'impôt sur les sociétés"


class is_nombre_mois_retard(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    default_value = 0
    label = "Nombre de mois de retard de depot de la declaration"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:

        date_cloture = period.date
        date_depot = personne("is_date_de_depot", period, parameters)[0].astype('M8[M]').astype(object)
        cessation = personne("is_cessation_activite", period, parameters)

        if cessation:
            # En cas de cessation : date limite = 1er jour du 4ème mois après la clôture (ex: clôture en mars → limite au 1er juillet)
            new_month = date_cloture.month + 4
            # Récupère le quotient entier // pour savoir si il y a un changement d'année
            new_year = date_cloture.year + (new_month // 12)
            # Gère le cas où new_month = 0 (décembre : 12 % 12 = 0)
            new_month = (new_month % 12) or 12
            date_limite_depot = datetime.date(new_year, new_month, 1)

            # Calcul du retard en mois (sans tolérance archipel)
            nb_mois = (date_depot.year - date_limite_depot.year) * 12 + (date_depot.month - date_limite_depot.month)
        else:
            if date_cloture.month < 2:
                date_limite_depot = datetime.date(date_cloture.year, 7, 31)
            elif date_cloture.month < 8:
                date_limite_depot = datetime.date(date_cloture.year + 1, 1, 31)
            else:
                date_limite_depot = datetime.date(date_cloture.year + 1, 7, 31)

            # Si îles de la Société → 0 mois, sinon → +1 mois
            tolerance_archipel = np.where(personne('est_societe', period.this_year), 0, 1)
            nb_mois = (12 - date_limite_depot.month + date_depot.month + ((date_depot.year - date_limite_depot.year) - 1) * 12) - tolerance_archipel

        if nb_mois < 0:
            return 0

        return nb_mois
