# -*- coding: utf-8 -*-

from openfisca_core.model_api import YEAR, Variable

from openfisca_pf.entities import Personne
from openfisca_pf.enums.geographie import *


class commune_fiscale(Variable):
    value_type = Enum
    possible_values = CommuneFiscale
    entity = Personne
    definition_period = YEAR
    default_value = CommuneFiscale.PAPEETE
    label = "Commune fiscale a laquelle le local est rattaché"
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
        commune_fiscale = local('commune_fiscale', period, parameters)
        return numpy.select(
            [
                numpy.isin(commune_fiscale, COMMUNES_DES_AUSTRALES),
                numpy.isin(commune_fiscale, COMMUNES_DES_GAMBIERS),
                numpy.isin(commune_fiscale, COMMUNES_DES_ILES_DU_VENT),
                numpy.isin(commune_fiscale, COMMUNES_DES_ILES_SOUS_LE_VENT),
                numpy.isin(commune_fiscale, COMMUNES_DES_MARQUISES),
                numpy.isin(commune_fiscale, COMMUNES_DES_TUAMOTUS)
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
