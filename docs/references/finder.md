---
layout: default
title: configlib.finder
parent: References
---

```python
def find(*variants: str, places: list = None) -> Path:
    r"""
    find a config file

    note: if a variant ends with .ext then every supported config-type is searched for

    :param variants: name of the config file
    :param places: list of directories to search in
    :return: pathlib.Path
    :raise ConfigNotFoundError: config-file could not be found
    """
    ...
```

## places

| function                | place                                                |
|-------------------------|------------------------------------------------------|
| `places.fsroot()`       | filesystem root directory (`/` or `C:\`)             |
| `places.local()`        | same directory as your `.py` script that is executed |
| `places.repository()`   | parent folder of local that contains a `.git` folder |
| `places.user_conf()`    | `.config` directory in the users home directory      |
| `places.home()`         | current users home directory                         |
| `places.etc()`          | `/etc`                                               |
| `places.localappdata()` | `~/AppData/Local/` (more precise: `%LOCALAPPDATA%`)  |
