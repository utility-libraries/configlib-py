#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import unittest
from pathlib import Path


HERE = Path(__file__).parent


class TestLoaders(unittest.TestCase):
    def test_conf(self):
        from configlib import load

        config = load(HERE / "test_configs" / "app.conf")
        self.assertEqual(config.getstr('owner', 'name'), "John Doe")
        self.assertEqual(config.getint('database', 'port'), 143)

    def test_json(self):
        from configlib import load

        config = load(HERE / "test_configs" / "app.json")
        self.assertEqual(config.getstr('first_name'), "John")
        self.assertEqual(config.getstr('phone_numbers', 0, 'type'), "home")

    def test_jsonc(self):
        from configlib import load

        config = load(HERE / "test_configs" / "app.jsonc")
        self.assertFalse(config.getbool('true'))
        self.assertEqual(config.getint('number'), 42)

    def test_json5(self):
        from configlib import load

        config = load(HERE / "test_configs" / "app.json5")
        self.assertEqual(config.get('positiveSign'), 1)

    def test_toml(self):
        from configlib import load

        config = load(HERE / "test_configs" / "app.toml")
        self.assertEqual(config.getstr('title'), "TOML Example")
        self.assertTrue(config.getbool('database', 'enabled'))

    def test_xml(self):
        from configlib import load

        config = load(HERE / "test_configs" / "app.xml")
        self.assertEqual(config.getstr('message', 'warning', '#'), "Hello World")

    def test_yaml(self):
        from configlib import load

        config = load(HERE / "test_configs" / "app.yaml")
        self.assertEqual(config.getstr('date'), "2012-08-06")
        self.assertEqual(config.getint('items', 1, 'quantity'), 1)


if __name__ == '__main__':
    unittest.main()
