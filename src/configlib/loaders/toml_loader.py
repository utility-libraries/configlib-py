#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import typing as t
from ..exceptions import NotSupportedError
from ..loader import register_loader
try:
    import tomllib  # python 3.11+
except ModuleNotFoundError:
    try:
        import toml as tomllib  # pip install config-library[toml]
    except ModuleNotFoundError:
        raise NotSupportedError('please install config-library[toml] for this')


ReturnType: t.TypeAlias = t.Dict[str, t.Any]


@register_loader('toml')
def load_toml(self) -> ReturnType:
    with open(self.fp, 'r') as file:
        return tomllib.load(file)
