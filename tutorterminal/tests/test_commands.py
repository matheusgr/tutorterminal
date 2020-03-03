from unittest import TestCase
import sys


import tutorterminal


class TestCommands(TestCase):

    def patch(self, results_list):
        tutorterminal.ansiprint = lambda x, end=None: results_list.append(x)

    def test_checkfile(self):
        self.assertTrue(tutorterminal.checkfile(sys.argv[0]))

    def test_not_checkfile(self):
        self.assertTrue(tutorterminal.checkfile(sys.argv[0] + "___________", exists=False))

    def test_run_command_auto_ok(self):
        self.assertTrue(tutorterminal.run_command("echo", auto=True))

    def test_run_command_auto_fail(self):
        self.assertFalse(tutorterminal.run_command("dir __1234__", auto=True))

    def test_prompt(self):
        results = []
        self.patch(results)
        tutorterminal.prompt()
        self.assertRegex(results[0], '.*\\$ $')
