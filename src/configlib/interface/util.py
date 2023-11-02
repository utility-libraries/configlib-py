# -*- coding=utf-8 -*-
r"""

"""
import shlex
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
        if isinstance(value, bool):
            return value
        elif isinstance(value, str):
            return Convert.BOOLEAN_STATES[value]
        elif value in {0, 1}:
            return bool(value)
        else:
            raise ValueError(f"can't safely ensure bool for {value!r} of type {type(value).__name__}")

    @staticmethod
    def split(value: t.Any):
        if isinstance(value, (tuple, list)):
            return list(map(str, value))
        elif isinstance(value, str):
            import re
            return re.split(r'\s*[,;]\s*', value)
        else:
            raise TypeError(f"can't split value of type {type(value).__name__}")

    @staticmethod
    def split_paths(value: t.Any):
        if isinstance(value, (tuple, list)):
            return list(map(str, value))
        elif isinstance(value, str):
            import os.path as p
            return value.split(p.pathsep)
        else:
            raise TypeError(f"can't path-split value of type {type(value).__name__}")

    @staticmethod
    def split_shlex(value: t.Any):
        return shlex.split(str(value))
