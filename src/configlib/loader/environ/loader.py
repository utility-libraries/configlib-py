# -*- coding=utf-8 -*-
r"""

"""
import os
import typing as t
from .util import default_split, default_transform


def load_env(
        prefix: str,
        override: bool = True,
        transform: t.Optional[t.Callable[[str], str]] = default_transform,
        split: t.Optional[t.Callable[[str], t.List[str]]] = default_split,
) -> t.Dict[str, t.Union[str, dict]]:
    r"""
    information for override
    if 'HELLO' and 'HELLO__WORLD' exist, then 'HELLO' gets overriden and is not included

    :param prefix: prefix to filter for (_ is automatically added to the prefix)
    :param override: in case of a conflict in a nested object the existing gets overriden, otherwise KeyError
    :param transform: function to transform the key (default: HELLO-WORLD -> hello_world)
    :param split: functions used to split the key to create a nested object (default: split by __)
    :return: dict
    """
    if transform is None:
        def transform(n):
            return n
    if split is None:
        def split(s):
            return [s]

    prefix = f"{prefix}_"

    env_object = {}

    for raw_key in os.environ.keys():
        if not raw_key.startswith(prefix):
            continue
        key = transform(raw_key.removeprefix(prefix))
        *path, setter = split(key)
        ref = env_object
        for k in path:
            k = transform(k)
            if k not in ref:
                ref[k] = {}
            elif not isinstance(ref[k], dict):
                if override:
                    ref[k] = {}
                else:
                    raise KeyError(f"{k} of {'->'.join(path)} exist")
            ref = ref[k]
        ref[setter] = os.environ[raw_key]

    return env_object
