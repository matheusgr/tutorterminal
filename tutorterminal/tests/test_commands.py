from unittest import TestCase
import sys


import tutorterminal


class TestCommands(TestCase):
    def test_checkfile(self):
        self.assertTrue(tutorterminal.checkfile(sys.argv[0]))

    def test_not_checkfile(self):
        self.assertTrue(tutorterminal.checkfile(sys.argv[0] + "___________", exists=False))

    def test_run_command_auto_ok(self):
        self.assertTrue(tutorterminal.run_command("echo", auto=True))

    def test_run_command_auto_fail(self):
        self.assertFalse(tutorterminal.run_command("dir __1234__", auto=True))
