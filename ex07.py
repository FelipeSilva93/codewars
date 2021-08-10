import unittest

"""
https://www.codewars.com/kata/5a431c0de1ce0ec33a00000c/train/python
"""


def even_numbers(arr, n):
    return [num for num in arr if num % 2 == 0][-n:]


class TestSimple(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(
            even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], 3), [4, 6, 8]
        )

    def test_simple2(self):
        self.assertEqual(
            even_numbers([-22, 5, 3, 11, 26, -6, -7, -8, -9, -8, 26], 2),
            [-8, 26],
        )


if __name__ == "__main__":
    unittest.main()
