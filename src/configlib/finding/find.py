# -*- coding=utf-8 -*-
r"""

"""
import typing as t
from pathlib import Path
from ..exceptions import ConfigNotFoundError
from ._variations import variations as iter_variations
from .default_places import DEFAULT_PLACES, T_PLACES


__all__ = ['find', 'find_iter']


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
    try:
        return next(find_iter(*variants, places=places))
    except StopIteration:
        raise ConfigNotFoundError("no config-file could be found anywhere")


def find_iter(*variants: str, places: T_PLACES = None) -> t.Iterator[Path]:
    r"""
    find all existing config files

    note: if a variant ends with .ext then every supported config-type is searched for

    note: you can make variations with file.{ext1,ext2}

    note: absolute paths have higher priority than relative

    :param variants: name-variants of the config file
    :param places: list of directories to search in
    :return: Iterator[pathlib.Path]
    """
    if places is None:
        places = DEFAULT_PLACES

    # split by absolute or relative
    absolutes, relatives = [], []

    for variation in (Path(v).expanduser() for v in iter_variations(*variants)):
        if variation.is_absolute():
            absolutes.append(variation)
        else:
            relatives.append(variation)

    # check absolutes
    for fp in absolutes:
        if fp.is_file():
            yield fp

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
                yield fp

    # don't fail
    # raise ConfigNotFoundError("no config-file could be found anywhere")
