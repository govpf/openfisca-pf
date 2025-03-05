# -*- coding: utf-8 -*-

from openfisca_pf.base import (
    ArrayLike,
    date,
    ETERNITY,
    max_,
    Parameters,
    Period,
    Variable,
    YEAR
)
from openfisca_pf.entities import Personne
from openfisca_pf.functions.time import annee_de_la_date


class terrain(Variable):
    value_type = bool
    entity = Personne
    definition_period = ETERNITY
    default_value = False
    label = "True si le bien immobilier est un terrain, sinon False."


class date_du_permis_de_construire(Variable):
    value_type = date
    entity = Personne
    definition_period = ETERNITY
    default_value = date(1970, 1, 1)
    label = "Date du permis de construire."


class date_du_certificat_de_conformite(Variable):
    value_type = date
    entity = Personne
    definition_period = ETERNITY
    default_value = date(1970, 1, 1)
    label = "Date du certificat de conformité."


class date_de_fin_des_travaux(Variable):
    value_type = date
    entity = Personne
    definition_period = ETERNITY
    default_value = date(1970, 1, 1)
    label = "Date de la fin des travaux de construction du bien immobilier. Elle est égale à la date du certificat de conformité si cette dernière est connue."

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return personne('date_du_certificat_de_conformite', period, parameters)


class age_du_bien(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Age du bien immobilier calculé à partir de la date de fin des travaux et la periode"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        date_de_fin_des_travaux = personne('date_de_fin_des_travaux', period, parameters)
        return max_(
            period.date.year - annee_de_la_date(date_de_fin_des_travaux),
            0
            )