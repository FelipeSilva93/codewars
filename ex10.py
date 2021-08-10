import unittest

"""
https://www.codewars.com/kata/58712dfa5c538b6fc7000569
"""


def count_red_beads(n):
    if n == 0:
        return 0
    else:
        return n * 2 - 2


class TestSimple(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(count_red_beads(1), 0)

    def test_simple2(self):
        self.assertEqual(count_red_beads(3), 4)

    def test_simple3(self):
        self.assertEqual(count_red_beads(5), 8)


if __name__ == "__main__":
    unittest.main()
