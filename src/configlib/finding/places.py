#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import os
import os.path as p


def fsroot():
    r"""
    should return 'C:\' under Windows and '/' under good OS's
    """
    return p.abspath(p.sep)


def cwd():
    r"""
    current working directory
    """
    return p.abspath(os.getcwd())


def local():
    r"""
    root-directory of the python script currently executed
    """
    import sys
    main = sys.modules.get('__main__')
    if main is None or not hasattr(main, '__file__'):
        return None
    return p.abspath(
        p.dirname(main.__file__)
    )


def repository():
    r"""
    folder that contains a .git directory somewhere above local()
    """
    directory = local()
    if directory is None:
        return None

    while not p.isdir(p.join(directory, '.git')) and directory != '/':
        directory = p.dirname(directory)

    if directory == '/':
        return None

    return directory


def user_conf():
    r"""
    the .config directory in the home-directory of the current user
    ~/.config/
    """
    return p.join(
        home(), ".config"
    )


def home():
    r"""
    the home-directory of the current user
    ~/
    """
    return p.abspath(p.expanduser("~"))


def etc():
    r"""
    the etc folder in the filesystem root directory
    /etc/
    """
    return p.join(fsroot(), "etc")


def localappdata():
    r"""
    %LOCALAPPDATA%
    """
    return os.getenv("LOCALAPPDATA")
