# -*- coding=utf-8 -*-
r"""

"""
import typing as t
from ..interface.typing import INDEX


XMISSING = object()
T = t.TypeVar("T")


def get_any(getter: t.Callable[..., T], *variants: t.Iterable[INDEX], fallback: t.Any = XMISSING) -> T:
    r"""
    config = ConfigInterface()
    get_any(config.getstr, ['logging', 'console', 'level'], ['logging', 'level'], fallback="INFO")

    :param getter: ConfigInterface.get*() method
    :param variants: access variants
    :param fallback: fallback value
    :return:
    """
    for keys in variants:
        value = getter(*keys, fallback=XMISSING)
        if value is not XMISSING:
            return value
    if fallback is XMISSING:
        raise KeyError(f"can't get any for {getter.__name__}")
    else:
        return fallback
