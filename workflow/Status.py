#!/usr/bin/env python3
from typing import Dict

from workflow.UndefinedStatusException import UndefinedStatusException


class Status(object):
    config = None  # type: Dict

    def __init__(self, value: str):
        if not self.config:
            raise NotImplementedError('Config must be defined to use Status.')
        if value not in self.config['statuses']:
            raise UndefinedStatusException(value, self.config['location'])
        self._value = value
        self.__setattr__(value.upper().replace(' ', '_'), value)

    def __str__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.value)

    @property
    def value(self):
        return self.__getattribute__(self._value.upper().replace(' ', '_'))

    @property
    def key(self):
        return self.value.upper()

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return (self.key, self.value, self._value) == (other.key, other.value, other._value)
