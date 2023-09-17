#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import warnings

extension_registry = {}


class BaseLoader:
    def __init_subclass__(cls, **kwargs):
        if not hasattr(cls, '_FILE_EXTENSIONS'):
            raise AttributeError("missing attribute '_FILE_EXTENSIONS'")
        if getattr(cls, 'load') is BaseLoader.load:
            raise NotImplementedError('please override the .load() method')
        for extension in cls._FILE_EXTENSIONS:
            if extension in extension_registry:
                warnings.warn(f'handler for {extension!r} is replaced')
            extension_registry[extension] = cls

    def __init__(self, fp):
        self.fp = fp

    def load(self):
        raise NotImplementedError()
