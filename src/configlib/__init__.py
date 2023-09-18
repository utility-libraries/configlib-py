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
__copyright__ = "Copyright 2023, PlayerG9"
__credits__ = ["PlayerG9"]
__license__ = "MIT"
__maintainer__ = "PlayerG9"
__email__ = None
__status__ = "Prototype"  # Prototype, Development, Production
__description__ = "utility library to find and load configuration files"
from .__version__ import __version__, __version_info__


from .finder import find
from .loader import autoload, SUPPORTED_EXTENSIONS, SUPPORTED_LOADERS
from . import loaders
from .configurator import Configurator


def find_and_load(name: str, namespace: str = None, ns_only: bool = None):
    fp = find(
        name=name,
        namespace=namespace,
        ns_only=ns_only if ns_only is not None else (namespace is not None),
    )
    return autoload(fp)
