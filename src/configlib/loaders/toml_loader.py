#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
try:
    import tomllib  # python 3.11+
except ModuleNotFoundError:
    try:
        import toml as tomllib  # pip install config-library[toml]
    except ModuleNotFoundError:
        raise NotImplementedError('please install config-library[toml] for this')
from . import baseloader


class TomlLoader(baseloader.BaseLoader):
    _FILE_EXTENSIONS = ('.toml',)

    def load(self):
        with open(self.fp, 'r') as file:
            return tomllib.load(file)
