#!/usr/bin/env python3
from typing import Type, List, Dict

from workflow.InvalidTransitionException import InvalidTransitionException
from workflow.Status import Status
from workflow.Transition import Transition


class Workflow(object):
    status_subclass = Status  # type: Type[Status]
    statuses = []  # type: List[Status]
    transitions = []  # type: List[Transition]

    def __init__(self):
        self._generate_statuses()
        self._generate_transitions()

    def get_subsequents(self, status: Status) -> list:
        subsequents = []
        for transition in self.transitions:
            if transition.get_from() == status and transition.get_to() not in subsequents:
                subsequents.append(transition.get_to())

        return subsequents

    def transition_exists(self, from_status: Status, to_status: Status) -> bool:
        transition = Transition(from_status, to_status)
        return bool(transition in self.transitions)

    def get_antecedents(self, status: Status) -> list:
        antecedents = []
        for transition in self.transitions:
            if transition.get_to() == status and transition.get_from() not in antecedents:
                antecedents.append(transition.get_from())

        return antecedents

    def validate_transition(self, from_status: Status, to_status: Status) -> bool:
        if not self.transition_exists(from_status, to_status):
            raise InvalidTransitionException(from_status, to_status)

        return True

    def _generate_statuses(self):
        for status_string in self.status_subclass.config['statuses']:
            status = self.status_subclass(status_string)
            self.statuses.append(status)

    def _generate_transitions(self):
        for transition_definition in self.status_subclass.config['transition_definitions']:
            if transition_definition['from'] == '*':
                for from_status in self.statuses:
                    to_status = self.status_subclass(transition_definition['to'])
                    self._add_to_transitions(from_status, to_status)
            elif transition_definition['to'] == '*':
                for to_status in self.statuses:
                    from_status = self.status_subclass(transition_definition['from'])
                    self._add_to_transitions(from_status, to_status)
            elif transition_definition['from'] == '*' and transition_definition['to'] == '*':
                raise InvalidTransitionException('*', '*')
            else:
                from_status = self.status_subclass(transition_definition['from'])
                to_status = self.status_subclass(transition_definition['to'])
                self._add_to_transitions(from_status, to_status)

    def _add_to_transitions(self, from_status: Status, to_status: Status):
        valid_transition = Transition(from_status, to_status)

        if valid_transition not in self.transitions and valid_transition.get_from() != valid_transition.get_to():
            self.transitions.append(valid_transition)
