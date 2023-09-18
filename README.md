# config-library
utility library to find and load configuration files

<!-- TOC -->
* [config-library](#config-library)
  * [Installation](#installation)
  * [Supported Config-Types](#supported-config-types)
  * [Install Variations](#install-variations)
  * [More about `configlib`](#more-about-configlib)
    * [Places to search for](#places-to-search-for)
  * [Usage Example](#usage-example)
<!-- TOC -->

## Installation

- `pip install config-library`
- `pip install config-library[all]`
- `pip install config-library[watcher]`
- `pip install config-library[json5]`
- `pip install config-library[toml]`
- `pip install config-library[yaml]`

## Supported Config-Types

| extension                | requires                              | link (for more information)                                                         |
|--------------------------|---------------------------------------|-------------------------------------------------------------------------------------|
| `.ini`/`.conf`/`.config` |                                       | https://en.wikipedia.org/wiki/INI_file                                              |
| `.json`                  |                                       | https://en.wikipedia.org/wiki/JSON                                                  |
| `.jsonc`                 |                                       | https://changelog.com/news/jsonc-is-a-superset-of-json-which-supports-comments-6LwR |
| `.json5`                 | `config-library[json5]`               | https://json5.org/                                                                  |
| `.toml`                  | `config-library[toml]` or python3.11+ | https://toml.io/                                                                    |
| `.yaml`/`.yml`           | `config-library[yaml]`                | https://en.wikipedia.org/wiki/YAML                                                  |
| `.xml`                   |                                       | https://en.wikipedia.org/wiki/XML                                                   |

## Install Variations

| variation                 | information                                       |
|---------------------------|---------------------------------------------------|
| `config-library[all]`     | adds all dependencies from the variations below   |
| `config-library[watcher]` | adds support to watch the config-file for changes |
| `config-library[json5]`   | support to load `.json5` files                    |
| `config-library[toml]`    | support to load `.toml` files                     |
| `config-library[yaml]`    | support to load `.yaml` files                     |


## More about `configlib`

### Places to search for

```
/path/to/your/source/code/
/path/to/your/git-repo/
/home/<user>/.config/
/home/<user>/
/etc/
```

> Note: On Windows there are respective counterparts.

And in these folders it searches for either directly the config file or a sub-folder that's named like your project.

## Usage Example

```python
# this way it's possible to write
# > from config import ...
# and it automatically restarts the python-script if app.json changes
# IMPORTANT: see configlib.configurator.restarter:restart() before usage
import configlib
configlib.Configurator("app.json").find().load().install().make_restart_on_change()
from config import HOST, PORT
...
server.bind((HOST, PORT))
```
```python
import configlib
config = configlib.autoload("./app.conf")
```
```python
from configlib.finder import find, places
config_file = find(
  name="app.conf",  # name of config-file is 'app.conf'
  places=[places.local, places.user],  # search in main.py folder and ~/.config/
  namespace="myproject",
  ns_only=True,  # only search for 'myproject/app.conf' in places
)
```

### More in detail

```python
import configlib
config = configlib.find_and_load('app.conf', 'project')
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
- /home/user/app.conf
- /home/user/project/app.conf
- /etc/app.conf
- /etc/project/app.conf
