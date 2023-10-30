---
title: Basic Usage
layout: default
nav_order: 2
---

* TOC
{:toc}

# Basic Usage

Automatically finding and loading the configuration file
```python
from configlib import find_and_load

config = find_and_load("app.conf")
```
or with the `Configurator` class which has additional features and can act as a common interface for all features in the library.
```python
from configlib import Configurator

config = Configurator("app.conf").find().load().config
# Configurator("app.conf").find_and_load()
```

## Manually finding

```python
from configlib import find

config_file = find("app.conf")
```

## Manually loading

```python
from configlib import autoload

config = autoload("./app.conf")
```

## Type-Hints

Either you import the types from `configlib.loaders`

```python
from configlib import find_and_load
from configlib.loader.loaders import ConfReturnType


config: ConfReturnType = find_and_load("app.conf")
```

or you use the correct loader

```python
from configlib.loader.loaders import load_conf


config = load_conf("app.conf")
```

or of course you use your own types
