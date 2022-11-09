#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""
simple test of this package
"""
import configs


conf = configs.findAndLoad('test-config.json')

print(conf)
