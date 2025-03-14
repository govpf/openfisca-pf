# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    Enum,
    Variable,
    YEAR
    )
from openfisca_pf.entities import Personne
from openfisca_pf.enums.impots import FormeLegale


class forme_legale(Variable):
    value_type = Enum
    possible_values = FormeLegale
    entity = Personne
    definition_period = YEAR
    default_value = FormeLegale.MR
    label = "Forme légale de la personne"
