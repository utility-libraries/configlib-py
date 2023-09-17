#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
from ..exceptions import NotSupportedError
from .conf_loader import load_conf, ReturnType as ConfReturnType
from .xml_loader import load_xml, ReturnType as XmlReturnType
from .json_loader import load_json, ReturnType as JsonReturnType
from .jsonc_loader import load_jsonc, ReturnType as JsonCReturnType
try:
    from .json5_loader import load_json5, ReturnType as Json5ReturnType
except NotSupportedError:
    def load_json5(*_, **__):
        raise NotSupportedError()
    Json5ReturnType = None
try:
    from .toml_loader import load_toml, ReturnType as TomlReturnType
except NotSupportedError:
    def load_toml(*_, **__):
        raise NotSupportedError()
    TomlReturnType = None
try:
    from .yaml_loader import load_yaml, ReturnType as YamlReturnType
except NotSupportedError:
    def load_yaml(*_, **__):
        raise NotSupportedError()
    YamlReturnType = None
