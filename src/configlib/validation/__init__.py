# -*- coding=utf-8 -*-
r"""
>>> import configlib
>>> from configlib.validation import *
>>>
>>> class DatabaseModel(BaseModel):
>>>     host: IPvAnyAddress
>>>     port: PositiveInt
>>>
>>> class ConfigModel(BaseModel):
>>>     database: DatabaseModel
>>>     debug: bool
>>>
>>> config: configlib.ConfigInterface = ...
>>> config.validate(ConfigModel)
"""
from pydantic import BaseModel as __BaseModel, ConfigDict as _ConfigDict  # noqa
from pydantic.types import *  # noqa
from pydantic.networks import *  # noqa


class BaseModel(__BaseModel):
    r"""
    basic configuration model. every unknown data is ignored
    """
    pass


class OpenBaseModel(BaseModel):
    r"""
    similar to BaseModel, but allows additional data
    """
    model_config = _ConfigDict(extra='allow')


class StrictBaseModel(BaseModel):
    r"""
    similar to BaseModel, but fails on additional data
    """
    model_config = _ConfigDict(extra='forbid')
