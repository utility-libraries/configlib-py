#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import configparser
from . import baseloader


class ConfigLoader(baseloader.BaseLoader):
    _FILE_EXTENSIONS = ('.ini', '.conf', '.config')

    def load(self):
        parser = configparser.ConfigParser()
        with open(self.fp, 'r') as file:
            parser.read_file(file)
        return parser
