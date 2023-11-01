#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
from configlib.exceptions import NotSupportedError
from .conf_loader import load_conf
from .xml_loader import load_xml
from .json_loader import load_json
from .jsonc_loader import load_jsonc
try:
    from .json5_loader import load_json5
except NotSupportedError:
    def load_json5(*_, **__):
        raise NotSupportedError()
try:
    from .toml_loader import load_toml
except NotSupportedError:
    def load_toml(*_, **__):
        raise NotSupportedError()
try:
    from .yaml_loader import load_yaml
except NotSupportedError:
    def load_yaml(*_, **__):
        raise NotSupportedError()
