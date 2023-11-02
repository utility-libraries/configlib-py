---
title: Getting Started
layout: default
nav_order: 0
---

* TOC
{:toc}

# Getting-Started

## Installation

```bash
pip3 install config-library
```

<small>For the supported config-file-formats or install variants see [installation](../installation/)</small>

## Usage

`app.conf`
```ini
[database]
address=localhost
;port=8000
```

`main.py`
```python
from configlib import find_and_load

config = find_and_load('app.conf')
# config = find_and_load("app.json")  # format could be easily exchanged
# config = find_and_load("app.toml")  # depending on your needs and preferences
# config = find_and_load("app.yaml")  # and it should continue to work

address = config.get('database', 'address')
# address = config.getstr('database', 'address')  # also possible to ensure it's of type str
port = config.getint('database', 'port', fallback=5000)
```
