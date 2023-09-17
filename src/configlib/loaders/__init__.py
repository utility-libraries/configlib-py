#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import os
from ..exceptions import NotSupportedError
from .baseloader import BaseLoader, extension_registry
from .conf_loader import ConfLoader
from .xml_loader import XmlLoader
from .json_loader import JsonLoader
from .jsonc_loader import JsoncLoader
try:
    from .json5_loader import Json5Loader
except NotImplementedError:
    Json5Loader = None
try:
    from .toml_loader import TomlLoader
except NotImplementedError:
    TomlLoader = None
try:
    from .yaml_loader import YamlLoader
except NotImplementedError:
    YamlLoader = None


SUPPORTED_EXTENSIONS = tuple(extension_registry.keys())
SUPPORTED_LOADERS = tuple(
    Loader.__name__ for Loader in extension_registry.values()
)


def loadConfig(fp):
    fp = os.path.abspath(fp)
    extension = os.path.splitext(fp)[1]
    if extension not in SUPPORTED_EXTENSIONS:
        raise NotSupportedError('unsupported filetype')
    loader_class = extension_registry[extension]
    loader = loader_class(fp)
    return loader.load()
