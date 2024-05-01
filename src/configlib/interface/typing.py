# -*- coding=utf-8 -*-
r"""

"""
import typing as t


__all__ = ['INDEX', 'KEY', 'T_VALIDATION_ERROR']


INDEX = t.Union[str, int]
KEY = t.Union[
    INDEX,
    slice,
    t.Tuple[INDEX, ...], t.List[INDEX]
]


class T_VALIDATION_ERROR(t.TypedDict):  # noqa
    type: str
    loc: t.Tuple[str, ...]
    msg: str
    input: bool
    url: str
