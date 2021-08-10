import unittest

"""
https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python
"""


def move_zeros(array):
    n_array = [n for n in array if n != 0]
    temp = [n for n in array if n == 0]
    # n_list = n_array + temp

    return n_array + temp


class TestSimple(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(
            move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]),
            [1, 2, 1, 1, 3, 1, 0, 0, 0, 0],
        )

    def test_simple2(self):
        self.assertEqual(
            move_zeros(
                [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]
            ),
            [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        )

    def test_simple3(self):
        self.assertEqual(move_zeros([0, 0]), [0, 0])

    def test_simple4(self):
        self.assertEqual(move_zeros([]), [])


if __name__ == "__main__":
    unittest.main()
