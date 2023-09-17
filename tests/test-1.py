#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""
simple test of this package
"""
import configlib


conf = configlib.findAndLoad('test-config.json')

print(conf)
