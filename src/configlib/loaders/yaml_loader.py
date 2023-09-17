#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import typing as t
from ..exceptions import NotSupportedError
from ..loader import register_loader
try:
    import yaml
except ModuleNotFoundError:
    raise NotSupportedError('please install config-library[yaml] for this')


ReturnType: t.TypeAlias = t.Union[t.Dict[str, t.Any], t.List[t.Any]]


@register_loader('yaml', 'yml')
def load_yaml(self) -> ReturnType:
    with open(self.fp, 'r') as file:
        return yaml.safe_load(file)
