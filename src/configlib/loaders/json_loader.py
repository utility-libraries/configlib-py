#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import json
import typing as t
from ..loader import register_loader


ReturnType: t.TypeAlias = t.Union[t.Dict[str, t.Any], t.List[t.Any]]


@register_loader('json')
def load_json(self) -> ReturnType:
    with open(self.fp, 'r') as file:
        return json.load(file)
