import unittest

"""
https://www.codewars.com/kata/55685cd7ad70877c23000102/train/python"""


def make_negative(number):
    if number <= 0:
        return number

    else:
        return int("-" + str(number))


class TestSimple(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(make_negative(1), -1)

    def test_simple1(self):
        self.assertEqual(make_negative(-5), -5)

    def test_simple2(self):
        self.assertEqual(make_negative(0), 0)


if __name__ == "__main__":
    unittest.main()
