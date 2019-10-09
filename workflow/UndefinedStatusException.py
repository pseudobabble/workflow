#!/usr/bin/env python3


class UndefinedStatusException(BaseException):
    def __init__(self, name, location):
        message = '{} is not defined as a status in {}'.format(name, location)
        super().__init__(message)
