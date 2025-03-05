# -*- coding: utf-8 -*-
"""
description: définition de l'ensemble des constantes utilisées dans l'application
"""

from openfisca_core.model_api import Variable, ETERNITY
from openfisca_pf.constants.time import *
from openfisca_pf.entities import Personne

# TODO: RENAME nombre_de_jours_par_semaine
class nombre_de_jour_par_semaine(Variable):
    """
    Nombre de jours dans une semaine
    """
    value_type = int
    entity = Personne
    definition_period = ETERNITY
    label = "Nombre de jours dans une semaine"
    unit = "/1"
    default_value = NOMBRE_DE_JOURS_PAR_SEMAINE


# TODO: RENAME nombre_de_jours_par_mois_au_pro_rata_temporis
class nombre_de_jour_par_mois(Variable):
    """
    Nombre de jours dans un mois d'un calendier comptable prorata temporis
    """
    value_type = int
    entity = Personne
    definition_period = ETERNITY
    label = "Nombre de jours dans un mois d'un calendier comptable prorata temporis"
    unit = "/1"
    default_value = NOMBRE_DE_JOURS_PAR_MOIS_AU_PRO_RATA_TEMPORIS


# TODO: RENAME nombre_de_jours_par_an_au_pro_rata_temporis
class nombre_de_jour_par_an(Variable):
    """
    Nombre de jours dans une année d'un calendier comptable prorata temporis
    """
    value_type = int
    entity = Personne
    definition_period = ETERNITY
    label = "Nombre de jours dans une année d'un calendier comptable prorata temporis"
    unit = "/1"
    default_value = NOMBRE_DE_JOURS_PAR_AN_AU_PRO_RATA_TEMPORIS


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


# TODO RENAME nombre_d_heures_par_jour
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


# TODO RENAME nombre_d_heures_par_demi_journee_au_pro_rata_temporis
class nombre_d_heure_par_demi_journee_daf(Variable):
    """
    Nombre d'heure que la Direction des Affaires Foncière comptabilise pour une demi journée d'occupation
    """
    value_type = int
    entity = Personne
    definition_period = ETERNITY
    label = "Nombre d'heure que la Direction des Affaires Foncière comptabilise pour une demi journée d'occupation"
    unit = "/1"
    default_value = NOMBRE_D_HEURES_PAR_DEMI_JOURNEE_AU_PRO_RATA_TEMPORIS
