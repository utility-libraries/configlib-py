#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import typing as t


def findConfig(name: str, *, namespace: str = None, **kwargs: t.Dict[str, bool]) -> str:
    r"""
    search for the configuration file

    possible locations
    - directory of the executed python-file
    - in the root of the git-repository
    - in the ~/.config/ directory
    - in the /etc/ directory

    :param name: name of the configuration file
    :param namespace: possible parent directory that may also contain other configuration files
    :param kwargs:
    :return: the path to the config-file
    :raise FileNotFoundException: in case the file couldn't be found anywhere
    """
    ...


class ConfigFinder:
    r"""
    this class attempts to find the config file
    """

    name: str
    namespace: str

    def __init__(self, name: str, *, namespace: str = None, **kwargs):
        r"""
        search for the configuration file

        possible locations
        - directory of the executed python-file
        - in the root of the git-repository
        - in the ~/.config/ directory
        - in the /etc/ directory

        :param name: name of the configuration file
        :param namespace: possible parent directory that may also contain other configuration files (defaults to filename)
        :param kwargs:
        :return: the path to the config-file
        :raise FileNotFoundException: in case the file couldn't be found anywhere
        """
        ...

    def find(self) -> str: ...
    def findLocal(self) -> t.Optional[str]: ...
    def findGit(self) -> t.Optional[str]: ...
    def findUser(self) -> t.Optional[str]: ...
    def findGlobal(self) -> t.Optional[str]: ...
