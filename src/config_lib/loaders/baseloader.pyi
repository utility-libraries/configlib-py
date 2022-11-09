# -*- coding=utf-8 -*-
r"""

"""
import typing as t


extension_registry: t.Dict[str, type[BaseLoader]] = {}


class BaseLoader:
    _FILE_EXTENSIONS: list

    fp: str

    def __init__(self, fp: str): ...

    def load(self):
        raise NotImplementedError()
