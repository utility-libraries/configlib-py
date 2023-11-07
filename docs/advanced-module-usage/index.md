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

## Restarting the Script

This should be used if the configuration file changes, and you want to apply these changes.
Normally you use `Configurator.make_restart_on_change()`.

{: .warning }
> Use with caution. Because open files or tasks are not properly closed/stopped.

```python
from configlib.configurator import atrestart, restarter

# functions registered with the atrestart.register function are always called in restart
# to run atexit.register functions use `restarter.restart(run_atexit=True)`
@atrestart.register
def on_restart():
    ...  # cleanup or so

restarter.restart()  # restarts the script immediately

print("This is never executed")
```
<small>Never execute this Example. It runs forever.<small>
