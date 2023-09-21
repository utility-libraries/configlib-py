---
layout: default
title: configlib.finder
parent: References
---

```python
def find(name: str, *, places: List[str] = None, namespace: str = None, ns_only: bool = False) -> str:
    r"""
    find a config file with {name}

    :param name: name of the config file
    :param places: list of directories to search in
    :param namespace: namespace of the project
    :param ns_only: only search for {namespace}/{name}
    :return: filepath
    :raise ValueError: if no namespace is provided but ns_only is set
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
| `places.user()`         | `.config` directory in the users home directory      |
| `places.home()`         | current users home directory                         |
| `places.etc()`          | `/etc`                                               |
| `places.localappdata()` | `~/AppData/Local/` (more precise: `%APPDATA%`)       |
