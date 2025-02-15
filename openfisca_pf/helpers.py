from typing import Type
from openfisca_pf.base import ArrayLike, asarray, Enum


def enum_set(type: Type[Enum], *args: Enum) -> ArrayLike:
    return type.encode(asarray(args))
