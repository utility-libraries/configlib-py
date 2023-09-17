# config-library
utility library to find and load configuration files

<!-- TOC -->
* [config-library](#config-library)
  * [Installation](#installation)
  * [Supported Config-Types](#supported-config-types)
  * [How does `configlib` work](#how-does-configlib-work)
    * [Places to search for](#places-to-search-for)
    * [Usage Example](#usage-example)
<!-- TOC -->

## Installation

- `pip install config-library`
- `pip install config-library[all]`
- `pip install config-library[json5]`
- `pip install config-library[toml]`
- `pip install config-library[yaml]`

## Supported Config-Types

| extension                | requires                              | link                                                                                |
|--------------------------|---------------------------------------|-------------------------------------------------------------------------------------|
| `.ini`/`.conf`/`.config` |                                       | https://en.wikipedia.org/wiki/INI_file                                              |
| `.json`                  |                                       | https://en.wikipedia.org/wiki/JSON                                                  |
| `.jsonc`                 |                                       | https://changelog.com/news/jsonc-is-a-superset-of-json-which-supports-comments-6LwR |
| `.json5`                 | `config-library[json5]`               | https://json5.org/                                                                  |
| `.toml`                  | `config-library[toml]` or python3.11+ | https://toml.io/                                                                    |
| `.yaml`                  | `config-library[yaml]`                | https://en.wikipedia.org/wiki/YAML                                                  |

## How does `configlib` work

### Places to search for

```
/path/to/your/source/code/
/path/to/your/git-repo/
/home/<user>/
/etc/
```

And in these folders it searches for either directly the config file or a sub-folder that's named like your project.

### Usage Example

```python
import configlib

config = configlib.findAndLoad('app.conf', 'project')
```
system file-structure
```
/
├─ etc/
├─ home/user/
│  ├─ path/to/repo/
│  │  ├─ src/code/
│  │  │  ├─ main.py
│  ├─ .config/
```
places where `config-library` searches for the config-file
- /home/user/path/to/repo/src/code/app.conf
- /home/user/path/to/repo/src/code/project/app.conf
- /home/user/path/to/repo/app.conf
- /home/user/path/to/repo/project/app.conf
- /home/user/.config/app.conf
- /home/user/.config/project/app.conf
- /etc/app.conf
- /etc/project/app.conf
