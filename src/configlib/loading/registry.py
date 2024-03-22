#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import os
import typing as t
import warnings


T_LOADER: t.TypeAlias = t.Callable[[t.Union[str, os.PathLike]], t.Dict]
T = t.TypeVar('T')


REGISTRY: t.Dict[str, T_LOADER] = {}


def register_loader(*extensions: str) -> t.Callable[[T], T]:
    r"""
    register function as loader for 1+ extensions

    @register_loader('ext')
    def load_exc(fp: str) -> Any:
        ...
    """
    if not extensions:
        raise ValueError("Please provide at least on extension")

    def add_to_registry(fn: T) -> T:
        for extension in extensions:
            ext = extension.removeprefix('.')
            if ext in REGISTRY:
                warnings.warn(f"replace loader for .{ext} files")
            REGISTRY[ext] = fn
        return fn

    return add_to_registry
