#!/usr/bin/env python3
from workflow.InvalidTransitionException import InvalidTransitionException
from workflow.Status import Status
from workflow.UndefinedStatusException import UndefinedStatusException
from workflow.Workflow import Workflow

from demo_config import config


class ReportStatus(Status):
    config = config


class ReportWorkflow(Workflow):
    status_subclass = ReportStatus


class Report(object):
    def __init__(self):
        self.workflow = ReportWorkflow()
        self.status = ReportStatus('Due')

    def update_status(self, status: ReportStatus):
        if self.workflow.validate_transition(self.status, status):
            self.status = status


if __name__ == '__main__':
    report = Report()

    report.update_status(ReportStatus('In Progress'))

    print(report.status)
    print(type(report.status))

    report.update_status(ReportStatus('Overdue'))
    print(report.status)
    print(type(report.status))

    report.update_status(ReportStatus('Completed'))
    print(report.status)
    print(type(report.status))

    try:
        report.update_status('NotARealStatus')
    except InvalidTransitionException as e:
        print(e)

    try:
        report.update_status(ReportStatus("Also Not A Status"))
    except UndefinedStatusException as e:
        print(e)
