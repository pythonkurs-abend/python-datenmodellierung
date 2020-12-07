import unittest
from p30_test import is_sinn


class TestIsSinn(unittest.TestCase):
    def test_42_returns_true(self):
        result = is_sinn(42)
        self.assertTrue(result)

    def test_23_returns_false(self):
        result = is_sinn(23)
        self.assertFalse(result)

    def test_none_returns_false(self):
        result = is_sinn(None)
        self.assertFalse(result)

    def test_42_as_string_returns_true(self):
        result = is_sinn('42')
        self.assertTrue(result)
