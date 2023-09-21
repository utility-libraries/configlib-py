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
from configlib.loaders import load_conf

config = load_conf("app.conf")
```
