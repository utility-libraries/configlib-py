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
        self._event_handler = watchdog.events.FileSystemEventHandler()
        self._event_handler.on_modified = self._handle_event
        self._observer = watchdog.observers.Observer()
        self._observer.schedule(self._event_handler, file)

    def __enter__(self) -> 'Watcher':
        return self.start()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()

    @property
    def file(self):
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

    def _handle_event(self, event):
        print(self, event)
        for handler in self._handlers:
            handler()  # maybe add some sort of catch or so later
