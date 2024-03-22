#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import os
import typing as t
import configparser
from ..registry import register_loader


@register_loader('ini', 'conf', 'config')
def load_conf(fp: t.Union[str, os.PathLike]) -> dict:
    r"""
    # last modified 1 April 2001 by John Doe
    [owner]
    name = John Doe
    organization = Acme Widgets Inc.

    [database]
    # use IP address in case network name resolution is not working
    server = 192.0.2.62
    port = 143
    file = "payroll.dat"
    """
    parser = configparser.ConfigParser(
        allow_no_value=False,
        strict=True,
        empty_lines_in_values=False,
        interpolation=configparser.ExtendedInterpolation(),
    )
    parser.optionxform = lambda option: option.lower().replace('-', '_')  # 'Hello-World' => 'hello_world'
    with open(fp, 'r') as file:
        parser.read_file(file)
    return {
        section: {
            option: parser.get(section, option)
            for option in parser.options(section)
        } for section in parser.sections()
    }
