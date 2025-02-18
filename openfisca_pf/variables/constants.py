# -*- coding: utf-8 -*-
"""
description: définition de l'ensemble des constantes utilisées dans l'application
"""

from openfisca_core.model_api import Variable, ETERNITY
from openfisca_pf.entities import Personne


NOMBRE_DE_JOUR_PAR_SEMAINE = 7
"""
Nombre de jours dans une semaine
"""

NOMBRE_DE_JOUR_PAR_MOIS_PRORATA_TEMPORIS = 30
"""
Nombre de jours dans un mois d'un calendier comptable prorata temporis
"""

NOMBRE_DE_JOUR_PAR_AN_PRORATA_TEMPORIS = 360
"""
Nombre de jours dans une année d'un calendier comptable prorata temporis
"""

NOMBRE_DE_MOIS_PAR_AN = 12
"""
Nombre de mois dans une année
"""

NOMBRE_D_HEURES_PAR_JOUR = 24
"""
Nombre d'heures dans une journéee
"""

NOMBRE_D_HEURES_PAR_DEMI_JOURNEE_DAF = 8
"""
Nombre d'heure que la Direction des Affaires Foncière comptabilise pour une demi journée d'occupation
"""


class nombre_de_jour_par_semaine(Variable):
    """
    Nombre de jours dans une semaine
    """
    value_type = int
    entity = Personne
    definition_period = ETERNITY
    label = "Nombre de jours dans une semaine"
    unit = "/1"
    default_value = NOMBRE_DE_JOUR_PAR_SEMAINE


class nombre_de_jour_par_mois(Variable):
    """
    Nombre de jours dans un mois d'un calendier comptable prorata temporis
    """
    value_type = int
    entity = Personne
    definition_period = ETERNITY
    label = "Nombre de jours dans un mois d'un calendier comptable prorata temporis"
    unit = "/1"
    default_value = NOMBRE_DE_JOUR_PAR_MOIS_PRORATA_TEMPORIS


class nombre_de_jour_par_an(Variable):
    """
    Nombre de jours dans une année d'un calendier comptable prorata temporis
    """
    value_type = int
    entity = Personne
    definition_period = ETERNITY
    label = "Nombre de jours dans une année d'un calendier comptable prorata temporis"
    unit = "/1"
    default_value = NOMBRE_DE_JOUR_PAR_AN_PRORATA_TEMPORIS


class nombre_de_mois_par_an(Variable):
    """
    Nombre de mois dans une année
    """
    value_type = int
    entity = Personne
    definition_period = ETERNITY
    label = "Nombre de mois dans une année"
    unit = "/1"
    default_value = NOMBRE_DE_MOIS_PAR_AN


class nombre_d_heure_par_jour(Variable):
    """
    Nombre d'heures dans une journéee
    """
    value_type = int
    entity = Personne
    definition_period = ETERNITY
    label = "Nombre d'heures dans une journéee"
    unit = "/1"
    default_value = NOMBRE_D_HEURES_PAR_JOUR


class nombre_d_heure_par_demi_journee_daf(Variable):
    """
    Nombre d'heure que la Direction des Affaires Foncière comptabilise pour une demi journée d'occupation
    """
    value_type = int
    entity = Personne
    definition_period = ETERNITY
    label = "Nombre d'heure que la Direction des Affaires Foncière comptabilise pour une demi journée d'occupation"
    unit = "/1"
    default_value = NOMBRE_D_HEURES_PAR_DEMI_JOURNEE_DAF
