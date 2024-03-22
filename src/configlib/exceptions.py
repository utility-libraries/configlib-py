#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""


class ConfigLibError(Exception):
    r"""
    any exception coming from configlib
    """
    pass


class ConfigNotFoundError(ConfigLibError, FileNotFoundError):
    r"""
    A configuration file could not be found
    """
    pass


class NotSupportedError(ConfigLibError, NotImplementedError):
    r"""
    a configuration file could not be parsed
    """
    pass
