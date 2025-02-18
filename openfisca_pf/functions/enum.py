from typing import Type
from openfisca_pf.base import asarray, Enum, EnumArray


def enum_set(t: Type[Enum], *args: Enum) -> EnumArray:
    """
    Créé un array qui contient les valeurs d'enum données en paramètre.

    :param t: Type de l'enum
    :param args: Valeurs à mettre dans l'array.
    :return: Array contenant les valeurs d'enum données en paramètre.
    """
    return t.encode(asarray(args))
