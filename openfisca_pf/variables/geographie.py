# -*- coding: utf-8 -*-

from openfisca_core.model_api import YEAR, Variable
from openfisca_pf.entities import Personne
from openfisca_pf.enums.geographie import *


class commune(Variable):
    value_type = Enum
    possible_values = Commune
    entity = Personne
    definition_period = YEAR
    default_value = Commune.PAPEETE
    label = "Commune a laquelle le local est rataché"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class archipel(Variable):
    value_type = Enum
    possible_values = Archipel
    entity = Personne
    definition_period = YEAR
    default_value = Archipel.ILES_SOUS_LE_VENT
    label = "Archipel auquel le local appartient"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        commune = local('commune', period, parameters)
        return numpy.select(
            [
                numpy.isin(commune, COMMUNES_DES_AUSTRALES),
                numpy.isin(commune, COMMUNES_DES_GAMBIERS),
                numpy.isin(commune, COMMUNES_DES_ILES_DU_VENT),
                numpy.isin(commune, COMMUNES_DES_ILES_SOUS_LE_VENT),
                numpy.isin(commune, COMMUNES_DES_MARQUISES),
                numpy.isin(commune, COMMUNES_DES_TUAMOTUS)
                ],
            [
                Archipel.AUSTRALES,
                Archipel.GAMBIERS,
                Archipel.ILES_DU_VENT,
                Archipel.ILES_SOUS_LE_VENT,
                Archipel.MARQUISES,
                Archipel.TUAMOTUS
                ]
            )
