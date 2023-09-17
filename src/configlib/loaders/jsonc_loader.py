#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import re
import json
from ..loader import register_loader
from .json_loader import ReturnType


_REGEX = re.compile(r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)", re.MULTILINE | re.DOTALL)


@register_loader('jsonc')
def load_jsonc(self) -> ReturnType:
    def __replace(match):
        return "" if match.group(2) is not None else match.group(1)

    with open(self.fp, 'r') as file:
        content = file.read()

    content = _REGEX.sub(__replace, content)

    return json.loads(content)
