# -*- coding=utf-8 -*-
r"""

"""
from pydantic import BaseModel, ConfigDict as _ConfigDict  # noqa
from pydantic.types import *  # noqa
from pydantic.networks import *  # noqa


class OpenBaseModel(BaseModel):
    r"""
    similar to BaseModel, but does allows for additional data
    """
    model_config = _ConfigDict(extra='allow')


class StrictBaseModel(BaseModel):
    r"""
    similar to BaseModel, but fails on additional data
    """
    model_config = _ConfigDict(extra='forbid')
