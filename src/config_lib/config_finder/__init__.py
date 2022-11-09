#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
from .finder import ConfigFinder


def findConfig(name, *, namespace=None, **kwargs):
    return ConfigFinder(name=name, namespace=namespace, **kwargs).find()
