# -*- coding=utf-8 -*-
r"""

"""
import re
import typing as t


def split_double(name: str) -> t.List[str]:
    return re.split(r"_{2,}", name)


def split_single(name: str) -> t.List[str]:
    return re.split(r"_+", name)


default_split = split_double


def transform_lower(name: str) -> str:
    return name.lower().replace('-', '_')


def transform_upper(name: str) -> str:
    return name.upper().replace('-', '_')


default_transform = transform_lower
