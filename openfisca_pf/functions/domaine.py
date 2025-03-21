# -*- coding: utf-8 -*-


__all__ = [
    'aggreger_variables',
    'figer_emprise',
    'indexer_zone_commune'
    ]


from typing import List
from openfisca_pf.base import (
    array,
    ArrayLike,
    ndarray,
    ParameterNodeAtInstant,
    Period,
    Population,
    where
    )


def aggreger_variables(entitee: Population, period: Period, prefix: str, variables: List[str] | ArrayLike) -> ArrayLike:
    """
    Calcule et aggrège les valeurs des variables demandés dans un vecteur.
    Par exemple étant donné les variables `['x', 'y', 'z']`, le préfix `'a_'` la fonction calcule `[entitee('a_x', period)[0], entitee('a_y', period)[1], entitee('a_z', period)[2]]`

    :param entitee:   Entitée sur laquelle réaliser l'aggrégation des variables.
    :param period:    Periode durant laquelle réaliser les calculs.
    :param prefix:    Prefix à ajouter devant les noms des variables.
    :param variables: Noms des variables à aggréger.
    :return:          Vecteur contenant les valeurs aggrégées des variables.
    """
    result = []
    index = 0
    for identifiant in variables:
        value = entitee(prefix + identifiant, period)[index]
        result.append(value)
        index = index + 1
    return array(result)


def figer_emprise(mask: ndarray, emprise: ArrayLike, default: str) -> ndarray:
    """
    Lors de demandes multiples avec des types de calculs différents,
    il est nécessaire de figer l'emprise sur une donnée existante pour le type associé.

    :param mask: Masque binaire contenant des 1 et des 0
    :param emprise: Array de valeur d'emprise dont les valeurs seront utilisé là ou le masque est égale à 1.
    :param default: Emprise attendue là où le masque est égale 0
    :return: Array de valeurs d'emprise sous forme de texte.
    """
    return where(
        mask,
        emprise.decode_to_str(),
        default
        )


def indexer_zone_commune(parameter: ParameterNodeAtInstant, commune: ArrayLike, zone: ArrayLike, valeur: str) -> ArrayLike:
    """
    Index le parametre donnée avec le nom de la commune, puis avec le nom de la zone et enfin avec la valeur souhaitée.

    :param parameter: Paramètre à indexer
    :param commune: Commune
    :param zone: Zone
    :param valeur: Valeur à récupérer.
    :return: Valeur du paramètre dans la commune et dans la zone.
    """
    communes = commune.decode()
    zones = zone.decode()
    values = []
    for i in range(len(communes)):
        nom_commune = communes[i].name
        nom_zone = zones[i].name
        valeur_venale = parameter[nom_commune][nom_zone][valeur]
        values.append(valeur_venale)
    return array(values)
