from unittest import TestCase

import tutorterminal

class TestJoke(TestCase):
    def test_is_string(self):
        self.assertTrue(isinstance("test", basestring))
