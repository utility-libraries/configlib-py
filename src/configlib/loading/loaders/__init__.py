#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
from configlib.exceptions import NotSupportedError as __NotSupportedError
from .conf_loader import load_conf
from .xml_loader import load_xml
from .json_loader import load_json
from .jsonc_loader import load_jsonc
try:
    from .json5_loader import load_json5
except __NotSupportedError:
    def load_json5(*_, **__):
        raise __NotSupportedError("json5-support is not installed")
try:
    from .toml_loader import load_toml
except __NotSupportedError:
    def load_toml(*_, **__):
        raise __NotSupportedError("toml-support is not installed")
try:
    from .yaml_loader import load_yaml
except __NotSupportedError:
    def load_yaml(*_, **__):
        raise __NotSupportedError("yaml-support is not installed")
