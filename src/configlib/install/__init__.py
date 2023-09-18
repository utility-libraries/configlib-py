#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""
# main.py
import configlib
config_file = configlib.find("myapp.json")
config = configlib.autoload(config_file)
configlib.install(config, fp=config_file)

# config.pyi
HOST: str
PORT: int

# sub.py
import config
from config import HOST, PORT
...
"""
import sys
import os.path as p


ModuleClass = type(sys)


def install_config(config, *, fp: str = None):
    r"""

    :param config: the config-object to translate
    :param fp: set __file__ attribute
    :return:
    """
    if 'config' in sys.modules:
        raise ValueError("'config' module already exists")

    # note: sets __name__ and __doc__
    module = ModuleClass(name="config", doc="automatically generated module bases on one object")

    if fp:
        module.__file__ = p.abspath(fp)

    if isinstance(config, dict):
        for key in config:
            setattr(module, key, config[key])
    else:
        for key in dir(config):
            setattr(module, key, getattr(config, key))

    sys.modules['config'] = module