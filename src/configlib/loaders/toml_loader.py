#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import os
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
def load_toml(fp: t.Union[str, os.PathLike]) -> ReturnType:
    r"""
    # This is a TOML document

    title = "TOML Example"

    [owner]
    name = "Tom Preston-Werner"
    dob = 1979-05-27T07:32:00-08:00

    [database]
    enabled = true
    ports = [ 8000, 8001, 8002 ]
    data = [ ["delta", "phi"], [3.14] ]
    temp_targets = { cpu = 79.5, case = 72.0 }

    [servers]

    [servers.alpha]
    ip = "10.0.0.1"
    role = "frontend"

    [servers.beta]
    ip = "10.0.0.2"
    role = "backend"
    """
    with open(fp, 'r') as file:
        return tomllib.load(file)
