# -*- coding=utf-8 -*-
r"""

"""
import typing as t


INDEX = t.Union[str, int]
KEY = t.Union[
    INDEX,
    slice,
    t.Tuple[INDEX, ...], t.List[INDEX]
]
