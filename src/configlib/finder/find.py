#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import os.path as p
from ..exceptions import ConfigNotFoundError
from .default_places import DEFAULT_PLACES, T_PLACES


def find(name: str, *, places: T_PLACES = None, namespace: str = None, ns_only: bool = False) -> str:
    if not namespace and ns_only:
        raise ValueError('ns_only can only be used if namespace is provided')

    if places is None:
        places = DEFAULT_PLACES

    for place in places:
        if not p.isdir(place):
            continue

        # check directly for the config file
        if not ns_only:
            fp = p.join(place, name)
            if p.isfile(fp):
                return fp

        if namespace:
            # check for the config file in the namespace folder
            fp = p.join(place, namespace, name)
            if p.isfile(fp):
                return fp

    # Error Message
    cfg = f"{namespace}/{name}" if ns_only else f"{name} or {namespace}/{name}"
    raise ConfigNotFoundError(f"{cfg} nowhere found")
