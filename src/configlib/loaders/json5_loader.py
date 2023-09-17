#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
from ..exceptions import NotSupportedError
try:
    import json5
except ModuleNotFoundError:
    raise NotSupportedError('please install config-library[json5] for this')
from . import baseloader


class Json5Loader(baseloader.BaseLoader):
    _FILE_EXTENSIONS = ('.json5',)

    def load(self):
        with open(self.fp, 'r') as file:
            return json5.load(file)
