#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import os
import os.path as p
import sys
from ..exceptions import ConfigNotFoundError


class ConfigFinder:
    def __init__(self, name, *, namespace=None, **kwargs):
        self.name = name
        self._namespace = namespace
        self._config = kwargs

    @property
    def namespace(self):
        return self._namespace or p.splitext(p.basename(self.name))[0]

    def find(self):
        found = self.findLocal() or self.findGit() or self.findUser() or self.findGlobal()
        if found is None:
            raise ConfigNotFoundError(f"config for {self.name!r} not found")
        return found

    def findLocal(self):
        if not self._tryLocal:
            return None

        main = sys.modules.get('__main__', None)
        if not main or not hasattr(main, '__file__'):
            return None
        directory = os.path.dirname(main.__file__)
        return self._tryFind(directory)

    def findGit(self):
        if not self._tryGit:
            return None

        main = sys.modules.get('__main__', None)
        if not main or not hasattr(main, '__file__'):
            return None
        directory = os.path.dirname(main.__file__)

        while not p.isdir(p.join(directory, '.git')) and directory != '/':
            directory = p.dirname(directory)

        if directory == '/':
            return None

        return self._tryFind(directory)

    def findUser(self):
        if not self._tryUser:
            return None

        directory = p.expanduser(p.join('~', '.config'))
        return self._tryFind(directory)

    def findGlobal(self):
        if not self._tryGlobal:
            return None

        return self._tryFind('/etc')

    def _tryFind(self, where):
        a = p.join(where, self.name)
        if os.path.isfile(a):
            return a

        b = p.join(where, self.namespace, self.name)
        if os.path.isfile(b):
            return b

        return None

    @property
    def _tryLocal(self):
        return self._config.get('local', True)

    @property
    def _tryGit(self):
        return self._config.get('git', True)

    @property
    def _tryUser(self):
        return self._config.get('user', True)

    @property
    def _tryGlobal(self):
        return self._config.get('global', True)
