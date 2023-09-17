#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import typing as t
import configparser
from ..loader import register_loader


ReturnType: t.TypeAlias = configparser.ConfigParser


@register_loader('ini', 'conf', 'config')
def load_conf(fp: str) -> ReturnType:
    parser = configparser.ConfigParser()
    with open(fp, 'r') as file:
        parser.read_file(file)
    return parser
