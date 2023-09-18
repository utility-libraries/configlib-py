#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import os
import sys
import atexit


def restart(run_atexit: bool = True):
    r"""
    This function restarts your python program.
    PID and arguments stay the same.

    Warnings:
        - Stop further execution of code behind this function
        - It does not properly close files or other logic. So be careful.

    :param run_atexit: whether function registered with @atexit should be run or not
    """
    if run_atexit:
        atexit._run_exitfuncs()  # noqa
    os.execv(sys.executable, sys.orig_argv)
