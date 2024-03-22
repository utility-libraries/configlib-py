#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
from pathlib import Path
from ..exceptions import ConfigNotFoundError
from ._variations import variations as iter_variations
from .default_places import DEFAULT_PLACES, T_PLACES


def find(*variants: str, places: T_PLACES = None) -> Path:
    r"""
    find a config file

    note: if a variant ends with .ext then every supported config-type is searched for

    note: you can make variations with file.{ext1,ext2}

    note: absolute paths have higher priority than relative

    :param variants: name-variants of the config file
    :param places: list of directories to search in
    :return: pathlib.Path
    :raise ConfigNotFoundError: config-file could not be found
    """
    if places is None:
        places = DEFAULT_PLACES

    variations = list(iter_variations(*variants))

    # split by absolute or relative
    absolutes, relatives = [], []

    for variation in map(Path, variations):
        if variation.is_absolute():
            absolutes.append(variation)
        else:
            relatives.append(variation)

    # check absolutes
    for fp in absolutes:
        if fp.is_file():
            return fp

    # check relatives
    for place in places:
        if callable(place):
            place = place()
        if place is None:  # not-supported on this platform
            continue

        place = Path(place)
        if not place.is_dir():  # doesn't exist. No need to continue searching
            continue

        for variation in relatives:
            fp = place / variation
            if fp.is_file():
                return fp

    raise ConfigNotFoundError("no config-file could be found anywhere")
