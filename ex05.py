import unittest

"""
https://www.codewars.com/kata/551b4501ac0447318f0009cd
"""


def boolean_to_string(arg):
    return str(arg)


class TestSimple(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(boolean_to_string(True), "True")
        self.assertEqual(boolean_to_string(False), "False")


if __name__ == "__main__":
    unittest.main()
