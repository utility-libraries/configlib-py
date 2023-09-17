#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import typing as t
import xml.etree.ElementTree
import xml.dom.minidom
from ..loader import register_loader


ReturnType: t.TypeAlias = xml.dom.minidom.Element


@register_loader('xml')
def load_xml(self) -> ReturnType:
    with open(self.fp, 'r') as file:
        document: xml.dom.minidom.Document = xml.dom.minidom.parse(file)
        # document.version, document.encoding, document.standalone
        root: xml.dom.minidom.Element = document.documentElement
    return root
