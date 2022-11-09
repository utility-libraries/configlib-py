#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
try:
    import yaml
except ModuleNotFoundError:
    raise NotImplementedError('please install pyyaml for this')
from . import baseloader


class YamlLoader(baseloader.BaseLoader):
    _FILE_EXTENSIONS = ('.yaml',)

    def load(self):
        with open(self.fp, 'r') as file:
            return yaml.save_load(file)
