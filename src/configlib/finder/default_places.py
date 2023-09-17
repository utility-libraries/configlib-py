#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import typing as t
from . import places

T_PLACE: t.TypeAlias = t.Union[str, t.Callable[[], str]]
T_PLACES: t.TypeAlias = t.List[T_PLACE]

DEFAULT_PLACES: T_PLACES = [
    places.local,
    places.repository,
    places.user,
    places.home,
    places.etc,
    places.localappdata,
]
