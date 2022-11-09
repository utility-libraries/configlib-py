#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""
simple test of this package
"""
import config_lib


conf = config_lib.findAndLoad('test-config.json')

print(conf)
