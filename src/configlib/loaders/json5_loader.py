#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
from ..exceptions import NotSupportedError
from ..loader import register_loader
from .json_loader import ReturnType
try:
    import json5
except ModuleNotFoundError:
    raise NotSupportedError('please install config-library[json5] for this')


@register_loader('json5')
def load_json5(fp: str) -> ReturnType:
    r"""
    {
      // comments
      unquoted: 'and you can quote me on that',
      singleQuotes: 'I can use "double quotes" here',
      lineBreaks: "Look, Mom! \
    No \\n's!",
      hexadecimal: 0xdecaf,
      leadingDecimalPoint: .8675309, andTrailing: 8675309.,
      positiveSign: +1,
      trailingComma: 'in objects', andIn: ['arrays',],
      "backwardsCompatible": "with JSON",
    }
    """
    with open(fp, 'r') as file:
        return json5.load(file)
