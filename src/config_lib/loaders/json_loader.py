#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import json
from . import baseloader


class JsonLoader(baseloader.BaseLoader):
    _FILE_EXTENSIONS = ('.json',)

    def load(self):
        with open(self.fp, 'r') as file:
            return json.load(file)
