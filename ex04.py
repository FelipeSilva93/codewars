"""
https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python
"""

import unittest


def persistence(n):
    if n < 10:
        return 0
    num_str = str(n)
    total = 1
    for num in num_str:
        total *= int(num)
    return 1 + persistence(total)


class TestSimple(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(persistence(39), 3)

    def test_simple_persistence_should_return_0(self):
        self.assertEqual(persistence(4), 0)

    def test_simple_persistence_should_return_2(self):
        self.assertEqual(persistence(25), 2)

    def test_simple_persistence_should_return_999(self):
        self.assertEqual(persistence(999), 4)
