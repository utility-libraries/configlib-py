#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""
# main.py
    import configlib
    configlib.install(dict(
        HOST="localhost",
        PORT=8000,
    ), fp=config_file)
    import sub

# config.pyi
    HOST: str
    PORT: int

# sub.py
    import config
    from config import HOST, PORT
    ...
"""
from .installer import install_config, reinstall_config
