---
title: Basic Usage
layout: default
nav_order: 2
---

* TOC
{:toc}

# Basic Usage

Automatically finding and loading of the configuration file

```python
from configlib import find_and_load, ConfigInterface

config: ConfigInterface = find_and_load("project.conf", "project/settings.conf")
# config: ConfigInterface = find_and_load("project.{yml,yaml}")


config.get('key', ..., fallback="default")
config.get*('key', ..., fallback="default")
```

# Config distribution

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

## Environment variables

It's also possible to load the environment variables.

```bash
SHELL=/bin/bash  # not taken as it hasn't the `APP` prefix
HOME=/home/user  # not taken as it hasn't the `APP` prefix
APP_DATABASE=mysql  # this gets overriden by `APP_DATABASE__PORT`
APP_DATABASE_PORT=1234  # this is a single key
APP_DATABASE__PORT=5678  # this gets split to a deep object
```
```python
from configlib import load_environ, ConfigInterface

config: ConfigInterface = load_environ("APP")
print(config.get())  # {'database_port': "1234", 'database': {'port': 5678}}
print(config.get("database_port"))  # 1234
print(config.get("database", "port"))  # 5678
```

## ConfigInterface

The `ConfigInterface` offers a common interface to the different kind of configuration files.

### getting a value

```python
from configlib import ConfigInterface
config = ConfigInterface()
config["database":"address"]
config["database", "address"]
config.get("database", "address")
config.getstr("database", "address")
```

#### get*

every `get*()` method has the same syntax

```python
.get*(*keys)  # raises an error if not found
.get*(*keys, fallback=default)  # fallback if not found
```

| method           | function                                                             |
|------------------|----------------------------------------------------------------------|
| `get()`          | returns the raw value (also has a special `converter=` parameter)    |
| `getstr()`       | ensures it returns a string                                          |
| `getint()`       | returns an integer                                                   |
| `getfloat()`     | returns a floating number                                            |
| `getbool()`      | returns the boolean value. (recognises strings like `yes` or `true`) |
| `getlist()`      | gets as list                                                         |
| `gettuple()`     | gets as tuple                                                        |
| `getsplit()`     | splits by `;` or `,` and removes outer spaces of the values          |
| `getpath()`      | returns as pathlib.Path                                              |
| `getpaths()`     | splits by the system path-seperator (eg. `:`)                        |
| `getshlex()`     | splits like the command line                                         |
| `getinterface()` | returns a new ConfigInterface of given option                        |
| `gettype()`      | gets the class of given configuration-option                         |

### checking for a value

```python
from configlib import ConfigInterface
config = ConfigInterface()

if ("database", "address") in config: ...
if config.has("database", "address"): ...
```

### removing a value

```python
from configlib import ConfigInterface
config = ConfigInterface()

del config["database", "address"]
del config["database":"address"]
config.remove("database", "address")
```

### updating the configuration

#### `.update()`

```python
from configlib import ConfigInterface
config = ConfigInterface()

print(config.get())
# {'deep': {'something': 1}}
config.update(deep=dict(key="value"))
print(config.get())
# {'deep': {'key': "value"}}
```

#### `.merge()`

This merges the new configuration to the existing one

```python
from configlib import ConfigInterface
config = ConfigInterface()

print(config.get())
# {'deep': {'something': 1}}
config.merge(deep=dict(key="value"))
print(config.get())
# {'deep': {'something': 1, 'key': "value"}}
```

### getting `keys()`/`items()`/`values()`

```python
from configlib import ConfigInterface
config = ConfigInterface()
config.get("database").keys()
config.get("database").items()
config.get("database").values()
config.get().keys()  # this is also possible
```

## Manually finding

To manually finding a configuration file you can use the `find()` function

```python
from configlib import find

config_file = find("app.conf")
```

## Manually loading

To manually load a specific configuration file you can use the `load()` function.
This recognises the correct configuration type and returns the common `ConfigInterface`

```python
from configlib import load, ConfigInterface

config: ConfigInterface = load("./app.conf")
```
