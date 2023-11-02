---
layout: default
title: configlib.configurator
parent: References
---

```python
class Configurator:
    def __init__(self, name: str, *, namespace: str = None, ns_only: bool = None, restart_on_change: bool = False):
        r"""
        :param name: name of the configuration file 
        :param namespace: namespace of the project
        :param ns_only: only search for {namespace}/{name}
        :param restart_on_change: restart the whole application if the configuration file changes
        """

    name: str
    namespace: Optional[str]
    search_namespace_only: bool
    file: Optional[str]
    config: Any
    restart_on_change: bool:
    run_atexit: bool

    def find_and_load(self) -> Self:
        r"""
        find and load the configuration file
        """

    def find(self) -> Self:
        r"""
        find the configuration file
        """

    def load(self) -> Self:
        r"""
        load the configuration file
        """

    def install(self) -> Self:
        r"""
        installed the loaded config file to be imported under 'config'

        see configlib.install
        """

    def make_restart_on_change(self, *, run_atexit: bool) -> Self:
        r"""
        restart the program on config-file changes
        """

    def watch(self) -> Self:
        r"""
        watch for changes to the configuration file and call handlers registered with .on_change()
        """
    
    def stop_watching(self) -> Self:
        r"""
        stop watching for changes
        """

    def on_change(self, handler):
        r"""
        register handler to be called when the configuration file changes
        """
```
