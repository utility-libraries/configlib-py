#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import typing as t
from ..exceptions import NotSupportedError
from .registry import REGISTRY, register_loader


@property
def SUPPORTED_EXTENSIONS() -> t.Iterable[str]:
    return tuple(REGISTRY.keys())


@property
def SUPPORTED_LOADERS() -> t.Iterable[str]:
    return tuple(
        loader.__name__ for loader in REGISTRY.values()
    )


def autoload(fp: str):
    import os.path as p
    ext = p.splitext(fp)[1][1:]
    if ext not in REGISTRY:
        raise NotSupportedError(f"files of type .{ext} are not supported")
    loader = REGISTRY[ext]
    return loader(fp)
