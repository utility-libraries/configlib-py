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

    def __init__(self, *variants: str, restart_on_change: bool = False):
        r"""
        :param name: name of the configuration file
        :param namespace: namespace of the project
        :param ns_only: only search for {namespace}/{name}
        :param restart_on_change: restart the whole application if the configuration file changes
        """
        self._variants = variants
        self._fp = None
        self._config = None
        self._watcher = None
        self.restart_on_change = restart_on_change
        self.run_atexit = False

    @property
    def variants(self) -> t.Tuple[str, ...]:
        return self._variants

    @property
    def file(self) -> t.Optional[str]:
        return self._fp

    @property
    def config(self) -> t.Any:
        if self._config is None:
            raise AttributeError(f"load() wasn't called yet")
        return self._config

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
        self._fp = find(*self.variants)
        return self

    def load(self) -> 'Configurator':
        r"""
        load the configuration file
        """
        from ..loader import load
        if self.file is None:
            raise CallOrderError(f"load() has to be called after find()")
        self._config = load(self.file)
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

    def make_restart_on_change(self, *, run_atexit: bool = None) -> 'Configurator':
        r"""
        restart the program on config-file changes
        """
        self.restart_on_change = True
        if run_atexit is not None:
            self.run_atexit = run_atexit
        self.watch()
        return self

    def _handle_change(self):
        from .restarter import restart
        if self.restart_on_change:
            restart(run_atexit=self.run_atexit)

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

    def stop_watching(self) -> 'Configurator':
        r"""
        stop watching for changes
        """
        if not self._watcher:
            return self
        self._watcher.stop()
        self._watcher.join()
        self._watcher = None
        return self

    def on_change(self, handler):
        r"""
        register handler to be called when the configuration file changes
        """
        return self._watcher.on_change(handler)
