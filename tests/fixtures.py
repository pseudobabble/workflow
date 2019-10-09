#!/usr/bin/env python3
from workflow.Status import Status
from workflow.Workflow import Workflow

test_config = {
    'statuses': ['a', 'b'],
    'transition_definitions': [
        {'from': 'a', 'to': 'b'},
        {'from': 'b', 'to': 'a'}
        # add c to this set of statuses
    ],
    'location': __file__
}


class TestStatus(Status):
    config = test_config


class TestWorkflow(Workflow):
    status_subclass = TestStatus
