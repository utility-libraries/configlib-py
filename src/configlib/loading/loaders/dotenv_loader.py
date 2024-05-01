# -*- coding=utf-8 -*-
r"""

"""
import os
import typing as t
from ...exceptions import NotSupportedError
from ..registry import register_loader
try:
    import dotenv
except ModuleNotFoundError:
    raise NotSupportedError('please install config-library[dotenv] for this')


__all__ = ['load_dotenv']


@register_loader('env')
def load_dotenv(fp: t.Union[str, os.PathLike]) -> dict:
    r"""
    # Development settings
    DOMAIN=example.org
    ADMIN_EMAIL=admin@${DOMAIN}
    ROOT_URL=${DOMAIN}/app
    """
    # todo: allow transform and split
    return dotenv.dotenv_values(fp)
