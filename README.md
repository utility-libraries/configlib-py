# config-library
utility library to find and load configuration files

> see the [documentation](https://utility-libraries.github.io/configlib-py/) for more information

<img style="height: 100px" src="https://github.com/utility-libraries/configlib-py/raw/main/README.assets/configlib.svg" alt="">

<!-- TOC -->
* [config-library](#config-library)
  * [Installation](#installation)
  * [Install Variations](#install-variations)
  * [Supported Config-Types](#supported-config-types)
  * [Usage Example](#usage-example)
    * [Basic usage](#basic-usage)
    * [Config distribution](#config-distribution)
    * [Loading specific file](#loading-specific-file)
    * [Loading from environment variables](#loading-from-environment-variables)
    * [Specify/Customise search locations](#specifycustomise-search-locations)
    * [Accessing configuration](#accessing-configuration)
  * [More in detail](#more-in-detail)
    * [Searching](#searching)
    * [Loading](#loading)
<!-- TOC -->

## Installation

[![PyPI - Version](https://img.shields.io/pypi/v/config-library)
](https://pypi.org/project/config-library/)

- `pip install config-library`
- `pip install config-library[all]`
- `pip install config-library[json5]`
- `pip install config-library[toml]`
- `pip install config-library[yaml]`

## Install Variations

| variation                 | information                                       |
|---------------------------|---------------------------------------------------|
| `config-library[all]`     | adds all dependencies from the variations below   |
| `config-library[json5]`   | adds support to load `.json5` files               |
| `config-library[toml]`    | adds support to load `.toml` files                |
| `config-library[yaml]`    | adds support to load `.yaml` files                |

## Supported Config-Types

| extension                | requires                              | link (for more information)                                                           |
|--------------------------|---------------------------------------|---------------------------------------------------------------------------------------|
| `.ini`/`.conf`/`.config` | -                                     | <https://en.wikipedia.org/wiki/INI_file>                                              |
| `.json`                  | -                                     | <https://en.wikipedia.org/wiki/JSON>                                                  |
| `.jsonc`                 | -                                     | <https://changelog.com/news/jsonc-is-a-superset-of-json-which-supports-comments-6LwR> |
| `.json5`                 | `config-library[json5]`               | <https://json5.org/>                                                                  |
| `.toml`                  | `config-library[toml]` or python3.11+ | <https://toml.io/>                                                                    |
| `.yaml`/`.yml`           | `config-library[yaml]`                | <https://en.wikipedia.org/wiki/YAML>                                                  |
| `.xml`                   | -                                     | <https://en.wikipedia.org/wiki/XML>                                                   |

## Usage Example

### Basic usage

```python
from configlib import find_and_load

config = find_and_load("app.conf")
# config = find_and_load("app.json")  # format could be easily exchanged
# config = find_and_load("app.toml")  # depending on your needs and preferences
# config = find_and_load("app.yaml")  # and it should continue to work
# config = find_and_load("app.{yml,yaml}")  # (you can also specify multiple extensions)

address = config.get('database', 'address')
# address = config.getstr('database', 'address')  # also possible to ensure it's of type str
port = config.getint('database', 'port', fallback=5000)
```

### Config distribution

configlib offers a global configuration instance.
This can help you avoid the hassle of passing the configuration instance to different functions.

`main.py`
```python
from configlib import config, find_and_load
from sub import function

config.update(find_and_load("config.ext"))

function()
```

`sub.py`
```python
import logging
from configlib import config

def function():
    if config.getbool("debug"):
        logging.debug("Some information")
    ...
```

### Loading specific file

```python
import configlib

config = configlib.load("./app.conf")
```

### Loading from environment variables

```python
import configlib

# contains every environment variable that starts with 'APP_'
config = configlib.load_environ("APP")
```

### Specify/Customise search locations

```python
from configlib.finder import find, places

config_file = find(
    "project-name.conf",  # variant of the config-file to search for is 'app.conf'
    "project-name/settings.conf",  # alternate variant name to search for
    "{project-name,variant-name}/settings.conf",  # write variants 
    places=[places.local, places.user_conf],  # search in main.py folder and ~/.config/
)
```

### Accessing configuration

In the end you get an instance of the `ConfigInterface` with useful get-methods

```python
from configlib import ConfigInterface
config: ConfigInterface
config.get("database", "address", fallback="localhost")  # gets the value raw as parsed
config.getstr("database", "address", fallback="localhost")  # gets as string
config.getint("database", "port", fallback=5432)  # gets as integer
config.getfloat("database", "timeout", fallback=10.0)  # gets as floating point number
config.getbool("database", "delayed-connect", fallback=False)  # gets as boolean
config.getlist("database", "tables", fallback=[], cast=str)  # gets as list
config.gettuple("database", "tables", fallback=[], cast=str)  # gets as tuple
config.getsplit("database", "tables")  # clean split by `,` or `;`
config.getpath("database", "client-paths", fallback="./")  # returns as pathlib.Path
config.getpaths("database", "client-paths", fallback=[], as_path=True)  # split by os.path.altsep (commonly `:`)
config.getshlex("database", "additional-params", fallback=[])  # split like the command-line
config.getinterface("database")  # gets a new ConfigInterface for sub-option
config.gettype("database", "timeout")  # gets the type/class (e.g. int | float)
```

## More in detail

For the more detailed description we will use this code example.

```python
import configlib
config = configlib.find_and_load('project.conf', 'project/app.conf')
```

### Searching

The `configlib.finder` subpackage has a few predefined paths it attempts to search in.
In each of these places it attempts to find one of the passed variants (`project.conf`, `project/app.conf`).
If it can't find one it goes to the next place and repeats this process.

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
- `/home/user/path/to/repo/src/code/project.conf` (next to the started script)
- `/home/user/path/to/repo/src/code/project/app.conf`
- `/home/user/path/to/repo/project.conf`  (next to .git/)
- `/home/user/path/to/repo/project/app.conf`
- `/home/user/.config/project.conf`  (~/.config/)
- `/home/user/.config/project/app.conf`
- `/home/user/project.conf`  (~/)
- `/home/user/project/app.conf`
- `/etc/project.conf`  (/etc/)
- `/etc/project/app.conf`

### Loading

After the search returns a filepath it is passed to the `load()` function.
This function analyzes the file-extension and loads it with the correct loader.

> The loader can be extended via the `configlib.loader.register_loader` decorator.
> Important is that it should return native types to be compatible with the `ConfigInterface`
> ```python
> from configlib.loader import register_loader
> 
> @register_loader("env", "environ")  # support for *.env or *.environ files 
> def custom_loader(fp) -> dict:
>     ...
> ```
