#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""


class ConfigLibError(Exception):
    r"""
    any exception coming from configlib
    """
    pass


class ConfigNotFoundError(ConfigLibError):
    r"""
    A configuration file could not be found
    """
    pass


class NotSupportedError(ConfigLibError):
    r"""
    a configuration file could not be parsed
    """
    pass


class CallOrderError(ConfigLibError):
    r"""
    another method should have been called first
    """
    pass
