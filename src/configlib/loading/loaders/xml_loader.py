# -*- coding=utf-8 -*-
r"""

"""
import os
import textwrap
import typing as t
from xml.etree import ElementTree
from ..registry import register_loader


__all__ = ['load_xml']


import warnings
warnings.warn(f"Module 'xml_loader' is soon deprecated as it's bad to generalise the format and will be"
              f" removed in a future version.", PendingDeprecationWarning, stacklevel=2)


@register_loader('xml')
def load_xml(fp: t.Union[str, os.PathLike]) -> dict:
    r"""
    <?xml version="1.0" encoding="UTF-8"?>
    <message>
        <warning>
             Hello World
        </warning>
    </message>
    """
    warnings.warn(f"Module 'xml_loader' is soon deprecated as it's bad to generalise the format and will be"
                  f" removed in a future version.", PendingDeprecationWarning, stacklevel=2)
    with open(fp, 'r') as file:
        root = ElementTree.parse(file).getroot()
    return {root.tag: node2dict(root)}


def node2dict(node: ElementTree.Element) -> dict:
    obj: t.Dict[str, t.Union[str, t.Dict, t.List[t.Union[str, t.List, t.Dict]]]] = {
        f'@{attr}': value
        for attr, value in node.attrib.items()
    }
    for child in node:
        if child.tag in obj:
            if not isinstance(obj[child.tag], list):
                obj[child.tag] = [obj[child.tag]]
            obj[child.tag].append(node2dict(child))
        else:
            obj[child.tag] = node2dict(child)
    text = textwrap.dedent(node.text).strip()
    if text:
        obj['#'] = text
    return obj
