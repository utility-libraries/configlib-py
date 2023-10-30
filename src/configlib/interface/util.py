# -*- coding=utf-8 -*-
r"""

"""
import typing as t
from .typing import KEY, INDEX


def unify_key(key: KEY) -> t.Tuple[INDEX, ...]:
    if isinstance(key, slice):
        return tuple(k for k in (key.start, key.stop, key.step) if k is not None)
    elif isinstance(key, (tuple, list)):
        return tuple(key)
    else:
        return (key,)


class Convert:
    BOOLEAN_STATES = {'1': True, 'yes': True, 'true': True, 'on': True,
                      '0': False, 'no': False, 'false': False, 'off': False}

    @staticmethod
    def to_str(value: t.Any):
        return str(value)

    @staticmethod
    def to_int(value: t.Any):
        return int(value)

    @staticmethod
    def to_float(value: t.Any):
        return float(value)

    @staticmethod
    def to_bool(value: t.Any):
        if isinstance(value, str):
            return Convert.BOOLEAN_STATES[value]
        return bool(value)
