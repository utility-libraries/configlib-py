# -*- coding=utf-8 -*-
r"""

"""
import typing as t
from .util import KEY, INDEX, Convert, unify_key


__all__ = ['Interface']


MISSING = object()


class Interface:
    r"""
    interface to a deep object
    """
    _obj: t.Dict[str, t.Any]

    def __init__(self, obj: t.Dict[str, t.Any] = None):
        self._obj = obj or {}

    # ---------------------------------------------------------------------------------------------------------------- #

    def __str__(self):
        return f"<{', '.join(self)}>"

    def __repr__(self):
        return f"<{type(self).__name__}: {', '.join(self)}>"

    def __format__(self, format_spec):
        import re
        raw_keys = re.split(r'\s*[.,:;|]\s*', format_spec, flags=re.I)
        keys = [int(k) if k.isdecimal() else k for k in raw_keys if k]
        return self.getstr(*keys, fallback="<missing>")

    # ---------------------------------------------------------------------------------------------------------------- #

    def __len__(self):
        return len(self._obj)

    def __iter__(self):
        yield from self._obj

    # ---------------------------------------------------------------------------------------------------------------- #

    def __getitem__(self, item: KEY):
        obj = self._obj
        for key in unify_key(item):
            obj = obj[key]
        return obj

    def get(self, *keys: INDEX, fallback: t.Any = MISSING, converter: t.Callable[[t.Any], t.Any] = None):
        r"""get the configuration value"""
        try:
            if converter is not None:
                return converter(self[keys])
            else:
                return self[keys]
        except (KeyError, IndexError, TypeError) as exc:
            if fallback is not MISSING:
                return fallback
            raise exc

    def getstr(self, *keys: INDEX, fallback: t.Any = MISSING) -> str:
        r"""Ensures the returned type is str"""
        return self.get(*keys, fallback=fallback, converter=Convert.to_str)

    def getint(self, *keys: INDEX, fallback: t.Any = MISSING) -> int:
        r"""Ensures the returned type is int"""
        return self.get(*keys, fallback=fallback, converter=Convert.to_int)

    def getfloat(self, *keys: INDEX, fallback: t.Any = MISSING) -> float:
        r"""Ensures the returned type is float"""
        return self.get(*keys, fallback=fallback, converter=Convert.to_float)

    def getboolean(self, *keys: INDEX, fallback: t.Any = MISSING) -> bool:
        r"""Ensures the returned type is bool"""
        return self.get(*keys, fallback=fallback, converter=Convert.to_bool)

    def getsplit(self, *keys: INDEX, fallback: t.Any = MISSING) -> t.List[str]:
        r"""split (and trim) by , or ;"""
        return self.get(*keys, fallback=fallback, converter=Convert.split)

    def getshlex(self, *keys: INDEX, fallback: t.Any = MISSING) -> t.List[str]:
        r"""split like the command line"""
        return self.get(*keys, fallback=fallback, converter=Convert.split_shlex)

    def getpaths(self, *keys: INDEX, fallback: t.Any = MISSING) -> t.List[str]:
        r"""split by os.path.pathsep"""
        return self.get(*keys, fallback=fallback, converter=Convert.split_paths)

    # ---------------------------------------------------------------------------------------------------------------- #

    def __delitem__(self, key: KEY):
        *keys, del_key = unify_key(key)
        obj = self._obj
        for key in keys:
            obj = obj[key]
        del obj[del_key]

    def remove(self, *keys: INDEX, failok: bool = False):
        r"""removes a given configuration"""
        try:
            del self[keys]
        except (KeyError, IndexError, TypeError) as exc:
            if not failok:
                raise exc

    # ---------------------------------------------------------------------------------------------------------------- #

    def __contains__(self, item: KEY):
        try:
            obj = self._obj
            for key in unify_key(item):
                obj = obj[key]
        except (KeyError, IndexError, TypeError):
            return False
        else:
            return True

    def has(self, *keys: INDEX) -> bool:
        r"""checks if configuration exists"""
        return keys in self

    # ---------------------------------------------------------------------------------------------------------------- #

    def update(self, __other: dict = None, **kwargs):
        r"""update the configuration with replacing"""
        other = (__other | kwargs) if __other else kwargs
        self._obj.update(other)

    def merge(self, __other: dict = None, **kwargs):
        r"""update the configuration with merging"""
        other = (__other | kwargs) if __other else kwargs

        def merge_dict(d: dict, o: dict):
            for key, value in o.items():
                if key in d and isinstance(d[key], dict):
                    merge_dict(d[key], value)
                else:
                    d[key] = value

        merge_dict(self._obj, other)
