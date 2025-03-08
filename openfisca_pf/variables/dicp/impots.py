# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    Enum,
    Variable,
    YEAR
    )
from openfisca_pf.entities import Personne
from openfisca_pf.enums.impots import TypePersonne


class forme_legale(Variable):
    value_type = Enum
    possible_values = TypePersonne
    entity = Personne
    definition_period = YEAR
    default_value = TypePersonne.M
    label = "Forme legale de la personne"
