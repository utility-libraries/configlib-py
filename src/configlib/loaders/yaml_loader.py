#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
from ..exceptions import NotSupportedError
try:
    import yaml
except ModuleNotFoundError:
    raise NotSupportedError('please install config-library[yaml] for this')
from . import baseloader


class YamlLoader(baseloader.BaseLoader):
    _FILE_EXTENSIONS = ('.yaml',)

    def load(self):
        with open(self.fp, 'r') as file:
            return yaml.safe_load(file)
