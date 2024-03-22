#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""
https://github.com/muhammadmuzzammil1998/jsonc
"""
import os
import re
import json
import typing as t
from ..registry import register_loader


_REGEX = re.compile(r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)", re.MULTILINE | re.DOTALL)


@register_loader('jsonc')
def load_jsonc(fp: t.Union[str, os.PathLike]) -> dict:
    r"""
    {
        /* This is an example
           for block comment.  */
        "foot": "bar foo",  // Comments
        "true": false,      // Improve readability
        "number": 42,       // Number will always be 42
        /* Comments are ignored while
           generating JSON from JSONC. */
        // "object": {
        //   "test": "done"
        // }
        "array": [1, 2, 3]
    }
    """

    def __replace(match):
        return "" if match.group(2) is not None else match.group(1)

    with open(fp, 'r') as file:
        content = file.read()

    content = _REGEX.sub(__replace, content)

    return json.loads(content)
