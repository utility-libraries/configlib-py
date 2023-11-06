#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
from pathlib import Path
from ..exceptions import ConfigNotFoundError
from ..loader import get_supported_extensions
from .default_places import DEFAULT_PLACES, T_PLACES


def find(*variants: str, places: T_PLACES = None) -> Path:
    r"""
    find a config file

    note: if a variant ends with .ext then every supported config-type is searched for

    :param variants: name of the config file
    :param places: list of directories to search in
    :return: pathlib.Path
    :raise ConfigNotFoundError: config-file could not be found
    """
    if places is None:
        places = DEFAULT_PLACES

    # Todo. Split variants by absolute or not

    for place in places:
        if callable(place):
            place = place()
        if place is None:
            continue

        place = Path(place)
        if not place.is_dir():
            continue

        for variant in variants:
            fp = place / variant
            if fp.suffix == ".ext":
                for extension in get_supported_extensions():
                    fpx = fp.with_suffix(f".{extension}")
                    if fpx.is_file():
                        return fpx
            else:
                if fp.is_file():
                    return fp

    # Error Message
    raise ConfigNotFoundError("no config-file could be found anywhere")
