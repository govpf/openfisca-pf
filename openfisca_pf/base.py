# -*- coding: utf-8 -*-

# This file defines the base enum needed by our legislation.
from openfisca_core.model_api import *


class TypePersonne(Enum):
    P = u'Personne physique'
    M = u'Personne morale'


class OuiNon(Enum):
    O = u'Oui'
    N = u'N'
