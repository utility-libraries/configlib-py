#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import os
import json
import typing as t
from ..registry import register_loader


@register_loader('json')
def load_json(fp: t.Union[str, os.PathLike]) -> dict:
    r"""
    {
      "first_name": "John",
      "last_name": "Smith",
      "is_alive": true,
      "age": 27,
      "address": {
        "street_address": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postal_code": "10021-3100"
      },
      "phone_numbers": [
        {
          "type": "home",
          "number": "212 555-1234"
        },
        {
          "type": "office",
          "number": "646 555-4567"
        }
      ],
      "children": [
        "Catherine",
        "Thomas",
        "Trevor"
      ],
      "spouse": null
    }
    """
    with open(fp, 'r') as file:
        return json.load(file)
