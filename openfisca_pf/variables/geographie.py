# -*- coding: utf-8 -*-

from openfisca_pf.base import (
    isin,
    Parameters,
    Period,
    select,
    Variable,
    YEAR
    )
from openfisca_pf.entities import Personne
from openfisca_pf.enums.geographie import *
from openfisca_pf.functions.enum import enum_set


class commune_fiscale(Variable):
    value_type = Enum
    possible_values = CommuneFiscale
    entity = Personne
    definition_period = YEAR
    default_value = CommuneFiscale.PAPEETE
    label = 'Commune fiscale a laquelle le local est rattaché'
    reference = 'https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595'


class archipel(Variable):
    value_type = Enum
    possible_values = Archipel
    entity = Personne
    definition_period = YEAR
    default_value = Archipel.ILES_SOUS_LE_VENT
    label = 'Archipel auquel le local appartient'
    reference = 'https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595'

    def formula(local: Personne, period: Period, parameters: Parameters):
        commune_fiscale = local('commune_fiscale', period, parameters)
        return select(
            [
                isin(commune_fiscale, COMMUNES_DES_AUSTRALES),
                isin(commune_fiscale, COMMUNES_DES_GAMBIERS),
                isin(commune_fiscale, COMMUNES_DES_ILES_DU_VENT),
                isin(commune_fiscale, COMMUNES_DES_ILES_SOUS_LE_VENT),
                isin(commune_fiscale, COMMUNES_DES_MARQUISES),
                isin(commune_fiscale, COMMUNES_DES_TUAMOTUS)
                ],
            enum_set(
                Archipel,
                Archipel.AUSTRALES,
                Archipel.GAMBIERS,
                Archipel.ILES_DU_VENT,
                Archipel.ILES_SOUS_LE_VENT,
                Archipel.MARQUISES,
                Archipel.TUAMOTUS
                )
            )
