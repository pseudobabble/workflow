#!/usr/bin/env python3
from workflow.Status import Status


class Transition(object):
    def __init__(self, from_status: Status, to_status: Status):
        self.from_status = from_status
        self.to_status = to_status

    def get_from(self):
        return self.from_status

    def get_to(self):
        return self.to_status

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return (self.from_status, self.to_status) == (other.from_status, other.to_status)
