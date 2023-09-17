#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import xml.etree.ElementTree
import xml.dom.minidom
from .baseloader import BaseLoader


class XmlLoader(BaseLoader):
    _FILE_EXTENSIONS = ('.xml',)

    def load(self) -> xml.dom.minidom.Element:
        with open(self.fp, 'r') as file:
            document: xml.dom.minidom.Document = xml.dom.minidom.parse(file)
            # document.version, document.encoding, document.standalone
            root: xml.dom.minidom.Element = document.documentElement
        return root
