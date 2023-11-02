#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import os
import typing as t
from ..exceptions import NotSupportedError
from ..interface import ConfigInterface
from .registry import REGISTRY, register_loader
from .environ import load_env
from . import loaders


__all__ = ["NotSupportedError", "REGISTRY", "register_loader",
           "get_supported_loaders", "get_supported_extensions", "load"]


def get_supported_extensions() -> t.Iterable[str]:
    r"""
    return currently supported file extensions

    eg: ini, conf, json
    """
    return tuple(REGISTRY.keys())


def get_supported_loaders() -> t.Iterable[str]:
    r"""
    return the names of the currently supported loaders

    eg: json_loader, toml_loader
    """
    return tuple(
        loader.__name__ for loader in REGISTRY.values()
    )


def load(fp: t.Union[str, os.PathLike]) -> ConfigInterface:
    r"""
    find the correct loader for the passed file, parses it and returns the result

    :param fp: path of the config-file
    :return: depends on the file-extension
    """
    import os.path as p
    ext = p.splitext(fp)[1][1:]
    if ext not in REGISTRY:
        raise NotSupportedError(f"files of type .{ext} are not supported")
    loader = REGISTRY[ext]
    return ConfigInterface(loader(fp))
