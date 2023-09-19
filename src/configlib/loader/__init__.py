#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import os
import typing as t
from ..exceptions import NotSupportedError
from .registry import REGISTRY, register_loader


__all__ = ["NotSupportedError", "REGISTRY", "register_loader",
           "get_supported_loaders", "get_supported_extensions", "autoload"]


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


def autoload(fp: t.Union[str, os.PathLike]):
    r"""
    find the correct loader for the passed file, parses it and returns the result

    :param fp: path of the config-file
    :return:
    """
    import os.path as p
    ext = p.splitext(fp)[1][1:]
    if ext not in REGISTRY:
        raise NotSupportedError(f"files of type .{ext} are not supported")
    loader = REGISTRY[ext]
    return loader(fp)
