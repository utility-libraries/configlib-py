#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import unittest


class TestBasics(unittest.TestCase):
    def test_import(self):
        import configlib  # noqa

    def test_not_found(self):
        import configlib

        with self.assertRaises(FileNotFoundError):
            configlib.find("not-found.json", places=[])
        with self.assertRaises(configlib.ConfigNotFoundError):
            configlib.find("not-found.json", places=[])


if __name__ == '__main__':
    unittest.main()
