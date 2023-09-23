#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import typing as t
import warnings


__all__ = ["register", "unregister"]


_T = t.TypeVar("_T")
_P = t.ParamSpec("_P")
__functions: t.Dict[t.Callable[_P, _T], t.Tuple[_P.args, _P.kwargs]] = dict()


def register(fn: t.Callable[_P, _T], *args: _P.args, **kwargs: _P.kwargs):
    __functions[fn] = (args, kwargs)
    return fn


def unregister(fn: t.Callable[_P, _T]):
    del __functions[fn]


def _run_restartfuncs():
    for fn, (args, kwargs) in __functions.items():
        try:
            fn(*args, **kwargs)
        except BaseException as exc:
            warnings.warn(f"atrestart functions failed with {type(exc).__name__} ({exc})", RuntimeWarning)
