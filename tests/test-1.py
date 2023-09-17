#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""
simple test of this package
"""
import configlib


conf = configlib.find_and_load('test-config.json')

print(conf)
