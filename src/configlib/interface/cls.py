# -*- coding=utf-8 -*-
r"""

"""
import typing as t
if t.TYPE_CHECKING:
    from pathlib import Path
from .util import KEY, INDEX, Convert, unify_key


__all__ = ['ConfigInterface']


MISSING = object()
_T = t.TypeVar('_T')


class ConfigInterface:
    r"""
    interface to a deep object

    todo: allow key-variants
    config.get('web', ['host', 'bind])
    """
    _obj: t.Dict[str, t.Any]

    def __init__(self, obj: t.Union['ConfigInterface', t.Dict[str, t.Any]] = None):
        self._obj = obj._obj if isinstance(obj, ConfigInterface) else (obj or {})

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

    def get(self, *keys: INDEX, fallback: t.Any = MISSING, converter: t.Callable[..., t.Any] = None, **kwargs):
        r"""get the configuration value"""
        if converter is None and kwargs:
            import warnings
            warnings.warn(f"converter arguments without converter passed", SyntaxWarning, stacklevel=2)
        try:
            value = self[keys]
            return converter(value, **kwargs) if converter is not None else value
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

    def getbool(self, *keys: INDEX, fallback: t.Any = MISSING) -> bool:
        r"""Ensures the returned type is bool"""
        return self.get(*keys, fallback=fallback, converter=Convert.to_bool)

    def getboolean(self, *args, **kwargs) -> bool:
        r"""Ensures the returned type is bool"""
        import warnings
        warnings.warn("getboolean is deprecated. Use .getbool() instead", DeprecationWarning, stacklevel=2)
        return self.getbool(*args, **kwargs)

    def getlist(self, *keys: INDEX, fallback: t.Any = MISSING, cast: t.Type[_T] = t.Any) -> t.List[_T]:
        r"""Ensures the returned type is list. (you may prefer .getsplit())"""
        return self.get(*keys, fallback=fallback, converter=Convert.to_list, cast=cast)

    def gettuple(self, *keys: INDEX, fallback: t.Any = MISSING, cast: t.Type[_T] = t.Any) -> t.Tuple[_T, ...]:
        r"""Ensures the returned type is tuple. (you may prefer `tuple(.getsplit())`)"""
        return self.get(*keys, fallback=fallback, converter=Convert.to_tuple, cast=cast)

    def getsplit(self, *keys: INDEX, fallback: t.Any = MISSING, cast: t.Type[_T] = str) -> t.List[_T]:
        r"""split (and trim) by , or ;"""
        return self.get(*keys, fallback=fallback, converter=Convert.split, cast=cast)

    def getshlex(self, *keys: INDEX, fallback: t.Any = MISSING) -> t.List[str]:
        r"""split like the command line"""
        return self.get(*keys, fallback=fallback, converter=Convert.split_shlex)

    def getpath(self, *keys: INDEX, fallback: t.Any = MISSING) -> 'Path':
        r"""get as pathlib.Path"""
        return self.get(*keys, fallback=fallback, converter=Convert.to_path)

    @t.overload
    def getpaths(self, *keys: INDEX, fallback: t.Any = MISSING, as_path: t.Literal[True] = ...) -> t.List['Path']: ...
    @t.overload
    def getpaths(self, *keys: INDEX, fallback: t.Any = MISSING, as_path: t.Literal[False]) -> t.List[str]: ...

    def getpaths(self, *keys: INDEX, fallback: t.Any = MISSING, as_path: bool = True) -> t.List[t.Union[str, 'Path']]:
        r"""split by os.path.pathsep (returns: pathlib.Path if as_path else str)"""
        return self.get(*keys, fallback=fallback, converter=Convert.split_paths, as_path=as_path)

    def getinterface(self, *keys: INDEX, fallback: dict = MISSING) -> 'ConfigInterface':
        r"""returns a new ConfigInterface of given option"""
        val = self.get(*keys, fallback=MISSING if fallback is MISSING else fallback)
        if not isinstance(val, dict):
            raise TypeError(val)
        return type(self)(val)

    def gettype(self, *keys: INDEX, fallback: t.Any = MISSING) -> type:
        r"""gets the class of given configuration-option"""
        return type(self.get(*keys, fallback=fallback))

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

    def update(self, __other: t.Union['ConfigInterface', dict] = None, **kwargs):
        r"""update the configuration with replacing"""
        if isinstance(__other, ConfigInterface):
            __other = __other._obj
        other = (__other | kwargs) if __other else kwargs

        self._obj.update(other)

    def merge(self, __other: t.Union['ConfigInterface', dict] = None, **kwargs):
        r"""update the configuration with merging"""
        if isinstance(__other, ConfigInterface):
            __other = __other._obj
        other = (__other | kwargs) if __other else kwargs

        def merge_dict(d: dict, o: dict):
            for key, value in o.items():
                if key in d and isinstance(d[key], dict):
                    merge_dict(d[key], value)
                else:
                    d[key] = value

        merge_dict(self._obj, other)
