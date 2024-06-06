# -*- coding=utf-8 -*-
r"""
>>> import configlib
>>> from configlib.validation import *
>>>
>>> class DatabaseModel(BasicConfigModel):
>>>     host: IPvAnyAddress
>>>     port: PositiveInt
>>>
>>> class ConfigModel(BasicConfigModel):
>>>     database: DatabaseModel
>>>     debug: bool
>>>
>>> config: configlib.ConfigInterface = ...
>>> config.validate(BasicConfigModel)
"""
from sys import version_info as __py_version
from pydantic import BaseModel as __PydanticModel, ConfigDict as _ConfigDict  # noqa
from pydantic.types import *  # noqa
from pydantic.networks import *  # noqa
from typing import Any, Union, Optional, Literal, Iterable, Mapping, Sequence  # noqa
if __py_version >= (3, 11):
    from typing import Required, NotRequired, Never  # noqa


class BasicConfigModel(__PydanticModel):
    r"""
    basic configuration model. every unknown data is ignored and removed
    """
    pass


class FlexibleConfigModel(BasicConfigModel):
    r"""
    similar to BasicConfigModel, but allows additional data
    """
    model_config = _ConfigDict(extra='allow')


class StrictConfigModel(BasicConfigModel):
    r"""
    similar to BasicConfigModel, but fails on additional data
    """
    model_config = _ConfigDict(extra='forbid')
