---
title: Installation
layout: default
nav_order: 1
---

* TOC
{:toc}

# Installation

```bash
pip3 install config-library
```

## Install Variations

| variation                    | information                                                                                                     |
|------------------------------|-----------------------------------------------------------------------------------------------------------------|
| `config-library[all]`        | adds all dependencies from the variations below                                                                 |
| `config-library[validation]` | adds support to validate the loaded configuration against a [pydantic](https://docs.pydantic.dev/latest/) model |
| `config-library[dotenv]`     | adds support to load `.env` files                                                                               |
| `config-library[json5]`      | adds support to load `.json5` files                                                                             |
| `config-library[toml]`       | adds support to load `.toml` files                                                                              |
| `config-library[yaml]`       | adds support to load `.yaml` files                                                                              |

## Supported Config-Types

| extension                | requires                              | link (for more information)                                                           |
|--------------------------|---------------------------------------|---------------------------------------------------------------------------------------|
| `.ini`/`.conf`/`.config` | -                                     | <https://en.wikipedia.org/wiki/INI_file>                                              |
| `.env`                   | `config-library[dotenv]`              | <https://pypi.org/project/python-dotenv/>                                             |
| `.json`                  | -                                     | <https://en.wikipedia.org/wiki/JSON>                                                  |
| `.jsonc`                 | -                                     | <https://changelog.com/news/jsonc-is-a-superset-of-json-which-supports-comments-6LwR> |
| `.json5`                 | `config-library[json5]`               | <https://json5.org/>                                                                  |
| `.toml`                  | `config-library[toml]` or python3.11+ | <https://toml.io/>                                                                    |
| `.yaml`/`.yml`           | `config-library[yaml]`                | <https://en.wikipedia.org/wiki/YAML>                                                  |
| `.xml`                   | -                                     | <https://en.wikipedia.org/wiki/XML>                                                   |
