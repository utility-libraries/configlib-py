#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import os
import typing as t
from configlib.exceptions import NotSupportedError
from ..registry import register_loader
try:
    import yaml
except ModuleNotFoundError:
    raise NotSupportedError('please install config-library[yaml] for this')


@register_loader('yaml', 'yml')
def load_yaml(fp: t.Union[str, os.PathLike]) -> dict:
    r"""
    receipt:     Oz-Ware Purchase Invoice
    date:        2012-08-06
    customer:
        first_name:   Dorothy
        family_name:  Gale

    items:
        - part_no:   A4786
          descrip:   Water Bucket (Filled)
          price:     1.47
          quantity:  4

        - part_no:   E1628
          descrip:   High Heeled "Ruby" Slippers
          size:      8
          price:     133.7
          quantity:  1

    bill-to:  &id001
        street: |
                123 Tornado Alley
                Suite 16
        city:   East Centerville
        state:  KS

    ship-to:  *id001

    specialDelivery:  >
        Follow the Yellow Brick
        Road to the Emerald City.
        Pay no attention to the
        man behind the curtain.
    """
    with open(fp, 'r') as file:
        return yaml.safe_load(file)
