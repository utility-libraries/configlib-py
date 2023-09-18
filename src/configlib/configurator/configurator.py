#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import typing as t
from ..exceptions import CallOrderError


class Configurator:
    r"""
    utility combiner for configlib

        from configlib import Configurator
        Configurator('app.conf').find().load().install().make_restart_on_change()
        ...
        from config import HOST
    """

    def __init__(self, name: str, *, namespace: str = None, ns_only: bool = None, restart_on_change: bool = False):
        self._name = name
        self._namespace = namespace
        self._ns_only = ns_only
        self._fp = None
        self._config = None
        self._watcher = None
        self._restart_on_change = restart_on_change

    @property
    def name(self) -> str:
        return self._name

    @property
    def namespace(self) -> t.Optional[str]:
        return self._namespace

    @property
    def search_namespace_only(self) -> bool:
        return self._ns_only if self._ns_only is not None else (self._namespace is not None)

    @property
    def file(self) -> t.Optional[str]:
        return self._fp

    @property
    def config(self) -> t.Any:
        if self._config is None:
            raise AttributeError(f"load() wasn't called yet")
        return self._config

    @property
    def restart_on_change(self) -> bool:
        return self._restart_on_change

    @restart_on_change.setter
    def restart_on_change(self, value: bool):
        self._restart_on_change = value

    def find_and_load(self) -> 'Configurator':
        r"""
        find and load the configuration file
        """
        self.find()
        self.load()
        return self

    def find(self) -> 'Configurator':
        r"""
        find the configuration file
        """
        from ..finder import find
        self._fp = find(
            name=self.name,
            namespace=self.namespace,
            ns_only=self.search_namespace_only,
        )
        return self

    def load(self) -> 'Configurator':
        r"""
        load the configuration file
        """
        from ..loader import autoload
        if self.file is None:
            raise CallOrderError(f"load() has to be called after find()")
        self._config = autoload(self.file)
        return self

    def install(self) -> 'Configurator':
        r"""
        installed the loaded config file to be imported under 'config'

        see configlib.install
        """
        from ..install import install_config
        if self._config is None:
            raise CallOrderError(f"install() has to be called after load()")
        install_config(self._config)
        return self

    def make_restart_on_change(self) -> 'Configurator':
        r"""
        restart the program on config-file changes
        """
        self.restart_on_change = True
        self.watch()
        return self

    def _handle_change(self):
        from .restarter import restart
        if self.restart_on_change:
            restart(run_atexit=True)

    def watch(self) -> 'Configurator':
        r"""
        watch for changes to the configuration file and call handlers registered with .on_change()
        """
        from ..watcher import Watcher
        if self._watcher:
            return self
        if self._config is None:
            raise CallOrderError(f"watch() has to be called after find()")
        self._watcher = Watcher(self.file)
        self._watcher.start()
        self._watcher.on_change(self._handle_change)
        return self

    def on_change(self, handler):
        r"""
        register handler to be called when the configuration file changes
        """
        return self._watcher.on_change(handler)
