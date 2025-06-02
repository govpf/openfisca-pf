# -*- coding: utf-8 -*-


__all__ = [
    # datetime
    'date',
    # numpy
    'array',
    'asarray',
    'ceil',
    'datetime64',
    'divide',
    'floor',
    'floor_divide',
    'full',
    'isin',
    'max_',
    'min_',
    'mod',
    'ndarray',
    'nextafter',
    'not_',
    'rint',
    'round_',
    'select',
    'timedelta64',
    'vectorize',
    'where',
    # numpy.typing
    'ArrayLike',
    # openfisca_core.holders
    'set_input_dispatch_by_period',
    'set_input_divide_by_period',
    # openfisca_core.indexed_enums
    'Enum',
    'EnumArray',
    # openfisca_core.periods
    'DAY',
    'ETERNITY',
    'Instant',
    'period',
    'Period',  # Use this to type the period input of a formula
    'MONTH',
    'YEAR',
    # openfisca_core.parameters
    'Parameter',
    'ParameterAtInstant',
    'ParameterNode',  # Use this to type the parameters input of a formula
    'ParameterNodeAtInstant',
    'ParameterScale',
    'ParameterScaleBracket',
    'VectorialParameterNodeAtInstant',
    # openfisca_core.populations
    'ADD',
    'DIVIDE',
    'GroupPopulation',  # Use this to type the first input of a formula defined for a group entity
    'Population',  # Use this to type the first input of a formula defined for a person entity
    # openfisca_core.variables
    'Variable'
    ]


from datetime import date
from numpy import (
    array,
    asarray,
    ceil,
    datetime64,
    divide,
    floor,
    floor_divide,
    full,
    isin,
    logical_not as not_,
    maximum as max_,
    minimum as min_,
    mod,
    ndarray,
    nextafter,
    rint,
    round as round_,
    select,
    timedelta64,
    vectorize,
    where
    )
from numpy.typing import ArrayLike
from openfisca_core.holders import (
    set_input_dispatch_by_period,
    set_input_divide_by_period
    )
from openfisca_core.indexed_enums import Enum, EnumArray
from openfisca_core.parameters import (
    Parameter,
    ParameterAtInstant,
    ParameterNode,  # Use this to type the parameters input of a formula
    ParameterNodeAtInstant,
    ParameterScale,
    ParameterScaleBracket,
    VectorialParameterNodeAtInstant,
    )
from openfisca_core.periods import (
    DAY,
    ETERNITY,
    Instant,
    period,
    Period,  # Use this to type the period input of a formula
    MONTH,
    YEAR
    )
from openfisca_core.populations import (
    ADD,
    DIVIDE,
    GroupPopulation,  # Use this to type the first input of a formula defined for a group entity
    Population  # Use this to type the first input of a formula defined for a person entity
    )
from openfisca_core.variables import Variable
