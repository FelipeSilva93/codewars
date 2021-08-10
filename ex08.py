import unittest

"""
https://www.codewars.com/kata/594adadee075005308000122/train/python
"""


def even_and_odd(n):
    temp = list(str(n))

    even = "".join([x for x in temp if int(x) % 2 == 0])
    odd = "".join([x for x in temp if int(x) % 2 != 0])

    # breakpoint()

    if len(even) >= 1 and len(odd) >= 1:
        return (
            int(even),
            int(odd),
        )

    elif len(even) == 0 and len(odd) >= 1:
        return 0, int(odd)

    else:
        return int(even), 0


class TestSimple(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(even_and_odd(126453), (264, 153))

    def test_simple2(self):
        self.assertEqual(even_and_odd(3012), (2, 31))

    def test_simple3(self):
        self.assertEqual(even_and_odd(4628), (4628, 0))


if __name__ == "__main__":
    unittest.main()
