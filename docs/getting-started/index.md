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

```python
from configlib import find_and_load

config = find_and_load('app.conf')
```
