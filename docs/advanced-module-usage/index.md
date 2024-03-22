---
title: Advanced Usage
layout: default
nav_order: 3
---

* TOC
{:toc}

# Advanced Usage

## Custom selection of directories

```python
from configlib.finder import find, places

location = find(
    "app.conf",
    places=[
        places.local,
        places.user_conf,
        places.etc,
    ]
)
```

[more about places](../references/finder#places)

## Updating the configuration with environment variables

Take the following example:

`app.conf`
```ini
[database]
address=localhost
port=5432
```

`environment`
```bash
APP_DATABASE__PORT=8000
```

```python
from configlib import find_and_load, load_environ, ConfigInterface

config: ConfigInterface = find_and_load("app.conf")
config.merge(load_environ("APP"))
# config.update(load_environ("APP"))  # (wrong) don't mix up update and merge

print(config.get("database", "port"))  # 5432
```
