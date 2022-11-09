#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import typing as t


extension_registry: t.Dict[str, 'type(BaseLoader)'] = {}


class BaseLoader:
    _FILE_EXTENSIONS: list

    def __init_subclass__(cls, **kwargs):
        if not hasattr(cls, '_FILE_EXTENSIONS'):
            raise AttributeError("missing attribute '_FILE_EXTENSIONS'")
        if getattr(cls, 'load') is BaseLoader.load:
            raise NotImplementedError('please override the .load() method')
        for extension in cls._FILE_EXTENSIONS:
            extension_registry[extension] = cls

    fp: str

    def __init__(self, fp: str):
        self.fp = fp

    def load(self):
        raise NotImplementedError()
