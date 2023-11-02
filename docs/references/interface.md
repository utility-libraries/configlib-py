---
layout: default
title: configlib.interface
parent: References
---

```python
class Interface:
    r"""
    interface to a deep object
    """

    def __init__(self, obj: Dict[str, Any] = None):
        ...

    def __str__(self): ...
    def __repr__(self): ...
    def __format__(self, format_spec): ...
    def __len__(self): ...
    def __iter__(self): ...
    def __getitem__(self, item): ...

    def get(self, *keys: INDEX, fallback: Any = MISSING, converter: Callable[[Any], Any] = None):
        r"""
        get the configuration value
        """

    def getstr(self, *keys: INDEX, fallback: Any = MISSING) -> str:
        r"""
        Ensures the returned type is str
        """

    def getint(self, *keys: INDEX, fallback: Any = MISSING) -> int:
        r"""
        Ensures the returned type is int
        """

    def getfloat(self, *keys: INDEX, fallback: Any = MISSING) -> float:
        r"""
        Ensures the returned type is float
        """

    def getboolean(self, *keys: INDEX, fallback: Any = MISSING) -> bool:
        r"""
        Ensures the returned type is bool
        """

    def getsplit(self, *keys: INDEX, fallback: Any = MISSING) -> List[str]:
        r"""
        split (and trim) by , or ;
        """

    def getshlex(self, *keys: INDEX, fallback: Any = MISSING) -> List[str]:
        r"""
        split like the command line
        """

    def getpaths(self, *keys: INDEX, fallback: Any = MISSING) -> List[str]:
        r"""
        split by os.path.pathsep
        """

    def __delitem__(self, key): ...

    def remove(self, *keys: INDEX, failok: bool = False):
        r"""
        removes a given configuration
        """

    def __contains__(self, item): ...

    def has(self, *keys: INDEX) -> bool:
        r"""
        checks if configuration exists
        """

    def update(self, __other: dict = None, **kwargs):
        r"""
        update the configuration with replacing
        """

    def merge(self, __other: dict = None, **kwargs):
        r"""
        update the configuration with merging
        """
```
