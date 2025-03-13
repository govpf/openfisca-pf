# -*- coding: utf-8 -*-


from openfisca_pf.base import Enum
from openfisca_pf.functions.enum import enum_set


__all__ = [
    'CategoryBien',
    'MEUBLE_OU_NON_MEUBLE',
    'TypeLocation'
    ]


class CategoryBien(Enum):
    """
    Catégorie du bien servant à préciser comment le bien est utilisé
    """

    ADMINISTRATIF = 'ADMINISTRATIF'
    """
    Le bien est une administration
    """

    AGRICOLE = 'AGRICOLE'
    """
    Le bien est utilisé pour de l'agriculture
    """

    ASSOCIATIF = 'ASSOCIATIF'
    """
    Le bien est utilisé à des fins associatives
    """

    AUTRE = 'AUTRE'
    """
    L'utilisation du bien ne rentre dans aucune catégorie
    """

    COMMERCE = 'COMMERCE'
    """
    Le bien est un commerce
    """

    CONSULAT = 'CONSULAT'
    """
    Le bien est un consulat
    """

    CULTE = 'CULTE'
    """
    Le bien est utilisé comme lieu de culte
    """

    ENSEIGNEMENT = 'ENSEIGNEMENT'
    """
    Le bien est une ecole, un collège, un lycé ou une université
    """

    INDUSTRIEL = 'INDUSTRIEL'
    """
    Le bien est utilisé pour une activiété industriel
    """

    LOGEMENT = 'LOGEMENT'
    """
    Le bien est un logement
    """

    MIXTE = 'MIXTE'
    """
    Le bien fait l'objet d'une utilisation mixte
    """

    PROFESSIONNEL = 'PROFESSIONNEL'
    """
    Le bien est utilisé professionnelement
    """


class TypeLocation(Enum):
    NON_MEUBLE = "NON_MEUBLE"
    MEUBLE = "MEUBLE"
    MEUBLE_DE_TOURISME = "MEUBLE_DE_TOURISME"
    VILLA_DE_LUXE = "VILLA_DE_LUXE"


MEUBLE_OU_NON_MEUBLE = enum_set(
    TypeLocation,
    TypeLocation.NON_MEUBLE,
    TypeLocation.MEUBLE
    )
