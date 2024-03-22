# -*- coding=utf-8 -*-
r"""

"""
import typing as t
from .typing import KEY, INDEX
if t.TYPE_CHECKING:
    import pathlib


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
        if isinstance(value, (str, int, float)):
            return str(value)
        else:
            raise ValueError(f"can't safely ensure str for {value!r} of type {type(value).__name__}")

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
    def to_list(value: t.Any, cast: t.Type = None):
        if isinstance(value, (list, tuple)):
            return list(value) if cast in {None, t.Any} else list(map(cast, value))
        else:
            raise ValueError(f"can't safely ensure list for {value!r} of type {type(value).__name__}")

    @staticmethod
    def to_tuple(value: t.Any, cast: t.Type = None):
        if isinstance(value, (list, tuple)):
            return list(value) if cast in {None, t.Any} else list(map(cast, value))
        else:
            raise ValueError(f"can't safely ensure tuple for {value!r} of type {type(value).__name__}")

    @staticmethod
    def split(value: t.Any, cast: t.Type = str):
        if isinstance(value, str):
            import re
            value = re.split(r'\s*[,;]\s*', value)

        if isinstance(value, (tuple, list)):
            return list(map(cast, value))
        else:
            raise ValueError(f"can't split value of type {type(value).__name__}")

    @staticmethod
    def to_path(value: t.Any) -> 'pathlib.Path':
        from os import PathLike
        from pathlib import Path
        if isinstance(value, (str, Path, PathLike)):
            return Path(value)
        else:
            raise ValueError(f"can't safely ensure Path for {value!r} of type {type(value).__name__}")

    @staticmethod
    def split_paths(value: t.Any, as_path: bool):
        from pathlib import Path
        cast = Path if as_path else str

        if isinstance(value, str):
            import os.path as p
            value = value.split(p.pathsep)

        if isinstance(value, (tuple, list)):
            return list(map(cast, value))
        else:
            raise ValueError(f"can't path-split value of type {type(value).__name__}")

    @staticmethod
    def split_shlex(value: t.Any):
        import shlex
        return shlex.split(str(value))
