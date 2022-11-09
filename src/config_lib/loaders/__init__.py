#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import os
from .baseloader import BaseLoader, extension_registry
from .json_loader import JsonLoader
try:
    from .toml_loader import TomlLoader
except NotImplementedError:
    pass


def loadConfig(fp):
    fp = os.path.abspath(fp)
    extension = os.path.splitext(fp)[1]
    loader_class = extension_registry.get(extension, None)
    if loader_class is None:
        raise TypeError('unsupported filetype')
    loader = loader_class(fp)
    return loader.load()
