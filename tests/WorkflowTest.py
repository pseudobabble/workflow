#!/usr/bin/env python3
import unittest

from workflow.Transition import Transition
from workflow.UndefinedStatusException import UndefinedStatusException
from tests.fixtures import test_config, TestStatus, TestWorkflow


class WorkflowTest(unittest.TestCase):

    test_statuses = [TestStatus(i) for i in test_config['statuses']]

    def test_construct(self):
        workflow = TestWorkflow()

        self.assertEqual(TestStatus, workflow.status_subclass)
        for status in workflow.statuses:
            self.assertIsInstance(status, TestStatus)
            self.assertIn(status.key, ['A', 'B'])
            self.assertIn(status.value, ['a', 'b'])
        for transition in workflow.transitions:
            self.assertIsInstance(transition, Transition)
            self.assertIn(transition.get_from(), self.test_statuses)
            self.assertIn(transition.get_to(), self.test_statuses)

    def test_get_subsequents(self):
        workflow = TestWorkflow()

        self.assertEqual(
            [TestStatus('b')],
            workflow.get_subsequents(TestStatus('a'))
        )

    def test_get_antecedents(self):
        workflow = TestWorkflow()

        self.assertEqual(
            [TestStatus('b')],
            workflow.get_antecedents(TestStatus('a'))
        )

    def test_transition_exists(self):
        workflow = TestWorkflow()

        self.assertTrue(
            workflow.transition_exists(
                from_status=TestStatus('a'),
                to_status=TestStatus('b')
            )
        )

    def test_validate_transition(self):
        workflow = TestWorkflow()

        self.assertTrue(
            workflow.validate_transition(
                from_status=TestStatus('a'),
                to_status=TestStatus('b')
            )
        )

    def test__validate_transition_fail_on_undefined_status(self):
        workflow = TestWorkflow()

        with self.assertRaises(UndefinedStatusException):
            workflow.validate_transition(from_status=TestStatus('p'), to_status=TestStatus('q'))


if __name__ == "__main__":
    unittest.main()
