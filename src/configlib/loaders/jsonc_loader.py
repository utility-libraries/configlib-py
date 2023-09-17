#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import json
import re
from . import baseloader


class JsoncLoader(baseloader.BaseLoader):
    _FILE_EXTENSIONS = ('.jsonc',)

    _REGEX = re.compile(r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)", re.MULTILINE | re.DOTALL)

    def load(self):
        def __replace(match):
            return "" if match.group(2) is not None else match.group(1)

        with open(self.fp, 'r') as file:
            content = file.read()

        content = JsoncLoader._REGEX.sub(__replace, content)

        return json.loads(content)
