#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""


class ConfigLibError(Exception):
    pass


class ConfigNotFoundError(ConfigLibError):
    pass


class NotSupportedError(ConfigLibError):
    pass


class CallOrderError(ConfigLibError):
    pass
