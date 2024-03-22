# -*- coding=utf-8 -*-
r"""

"""
import re
import itertools
import typing as t
from ..loading import get_supported_formats


PATTERN = re.compile(r"{(.+?)}")
WILDCARD_EXT = re.compile(r"\.ext$")
ALL_EXTENSIONS = f".{{{','.join(get_supported_formats())}}}"


def variations(*variants: str) -> t.Iterator[str]:
    r"""
    variations("hello.{yaml,yml}") -> ["hello.yaml", "hello.yml"]
    variations("hello.ext") -> ["hello.ini", "hello.conf", "hello.json", ...]
    """
    for variant in variants:
        variant = WILDCARD_EXT.sub(ALL_EXTENSIONS, variant)  # "hello.ext" => "hello.{ini,conf,json,...}"
        patterns: t.List[str] = PATTERN.findall(variant)
        if not patterns:
            yield variant
            continue
        patterns: t.List[t.List[str]] = [pattern.split(",") for pattern in patterns]
        template = PATTERN.sub('{}', variant)
        for values in itertools.product(*patterns):
            yield template.format(*values)
