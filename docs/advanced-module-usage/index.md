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
    name="app.conf",
    places=[
        places.local,
        places.user,
        places.etc,
    ]
)
```

[more about places](../references/finder#places)

## Completely manually loading of files

```python
from configlib.loader.loaders import load_conf


config = load_conf("app.conf")
```

### Restarting the Script

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
