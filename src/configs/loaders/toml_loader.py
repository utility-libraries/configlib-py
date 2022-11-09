#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
try:
    import tomllib
except ModuleNotFoundError:
    raise NotImplementedError('python version to low')
from . import baseloader


class TomlLoader(baseloader.BaseLoader):
    _FILE_EXTENSIONS = ('.toml',)

    def load(self):
        with open(self.fp, 'r') as file:
            return tomllib.load(file)
