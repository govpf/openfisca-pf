# -*- coding: utf-8 -*-


__all__ = [
    'EPSILON_TIMEDELTA',
    'NOMBRE_D_HEURES_PAR_DEMI_JOURNEE_AU_PRO_RATA_TEMPORIS',
    'NOMBRE_D_HEURE_PAR_JOUR',
    'NOMBRE_DE_JOURS_PAR_SEMAINE',
    'NOMBRE_DE_JOURS_PAR_MOIS_AU_PRO_RATA_TEMPORIS',
    'NOMBRE_DE_JOURS_PAR_AN_AU_PRO_RATA_TEMPORIS',
    'NOMBRE_DE_MOIS_PAR_AN',
    ]


from openfisca_pf.base import timedelta64


EPSILON_TIMEDELTA = timedelta64(1)
"""
Plus petit deltat de temps representable en machine
"""

NOMBRE_D_HEURES_PAR_DEMI_JOURNEE_AU_PRO_RATA_TEMPORIS: int = 8
"""
Nombre d'heures pour une demi-journée au pro rata temporis
"""

NOMBRE_D_HEURE_PAR_JOUR: int = 24
"""
Nombre d'heures par jour
"""

NOMBRE_DE_JOURS_PAR_SEMAINE: int = 7
"""
Nombre de jour par semaines
"""

NOMBRE_DE_JOURS_PAR_MOIS_AU_PRO_RATA_TEMPORIS: int = 30
"""
Nombre de jours par mois au pro rata temporis
"""

NOMBRE_DE_JOURS_PAR_AN_AU_PRO_RATA_TEMPORIS: int = 360
"""
Nombre de jours par ans au pro rata temporis
"""

NOMBRE_DE_MOIS_PAR_AN: int = 12
"""
Nombre de jours dans une année
"""
