#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""
MIT License

Copyright (c) 2023 PlayerG9

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

__author__ = "PlayerG9"
__copyright__ = "Copyright 2024, utility-libraries"
__credits__ = ["PlayerG9"]
__license__ = "MIT"
__maintainer__ = "PlayerG9"
__email__ = None
__status__ = "Prototype"  # Prototype, Development, Production
__description__ = "utility library to find and load configuration files"
__version_info__ = (0, 14, 0)
__version__ = '.'.join(str(_) for _ in __version_info__)

from .exceptions import *
from .finding import find, places
from .loading import load, get_supported_formats, loaders
from .interface import ConfigInterface
from . import util


# global configuration instance for easier config distribution
config = ConfigInterface()


def find_and_load(*variants: str, places=None) -> ConfigInterface:
    r"""
    common interface for the `find()` and `load()` function

    basically an alias for `load(find(...))`

    :param variants: same as `find()`: name-variants of the config file
    :param places: same as `find()`: list of directories to search in
    :return: ConfigInterface
    """
    fp = find(*variants, places=places)
    return load(fp)


def load_environ(prefix: str) -> ConfigInterface:
    r"""
    loads the environment variables into an object.
    The object gets nested by splitting the environment keys on `__`

    :param prefix: app prefix to filter the environment variables
    :return: ConfigInterface
    """
    from .loading.environ import load_env
    return ConfigInterface(load_env(prefix=prefix))
