#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import os.path as p
import typing as t
import watchdog.observers
import watchdog.events


class Watcher:
    def __init__(self, file: str):
        if not p.isfile(file):
            raise FileNotFoundError(file)
        self._fp = file
        self._handlers = []
        self._observer = watchdog.observers.Observer()
        self._observer.schedule(self, file)

    def __enter__(self) -> 'Watcher':
        return self.start()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()

    @property
    def file(self) -> str:
        return self._fp

    def on_change(self, handler: t.Callable[[], None]):
        self._handlers.append(handler)
        return handler

    def start(self) -> 'Watcher':
        self._observer.start()
        return self

    def stop(self):
        self._observer.stop()
        self._observer.join()

    def dispatch(self, event: watchdog.events.FileSystemEvent):
        if event.event_type != watchdog.events.EVENT_TYPE_MODIFIED:
            return
        if event.src_path != self.file:
            return
        for handler in self._handlers:
            handler()  # maybe add some sort of catch or so later
