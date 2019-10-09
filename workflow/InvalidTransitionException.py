#!/usr/bin/env python3
from workflow.Status import Status


class InvalidTransitionException(ValueError):
    def __init__(self, from_status: str, to_status: str):
        message = 'Cannot transition from {} to {}'.format(from_status, to_status)
        super().__init__(message)
