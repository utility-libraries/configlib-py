#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import unittest
from pathlib import Path


HERE = Path(__file__).parent


class TestLoaders(unittest.TestCase):
    def test_conf(self):
        from configlib import autoload

        config = autoload(HERE / "test_configs" / "app.conf")
        self.assertIsNotNone(config)

    def test_json(self):
        from configlib import autoload

        config = autoload(HERE / "test_configs" / "app.json")
        self.assertIsNotNone(config)

    def test_jsonc(self):
        from configlib import autoload

        config = autoload(HERE / "test_configs" / "app.jsonc")
        self.assertIsNotNone(config)

    def test_json5(self):
        from configlib import autoload

        config = autoload(HERE / "test_configs" / "app.json5")
        self.assertIsNotNone(config)

    def test_toml(self):
        from configlib import autoload

        config = autoload(HERE / "test_configs" / "app.toml")
        self.assertIsNotNone(config)

    def test_xml(self):
        from configlib import autoload

        config = autoload(HERE / "test_configs" / "app.xml")
        self.assertIsNotNone(config)

    def test_yaml(self):
        from configlib import autoload

        config = autoload(HERE / "test_configs" / "app.yaml")
        self.assertIsNotNone(config)


if __name__ == '__main__':
    unittest.main()
