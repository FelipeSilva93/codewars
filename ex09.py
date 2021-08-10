import unittest

"""
https://www.codewars.com/kata/59e49b2afc3c494d5d00002a/train/python
"""


def sort_vowels(s):
    temp = []

    if isinstance(s, str):
        for letter in s:
            if letter in "aAeEiIoOuU":
                temp.append(f"|{letter}")
            else:
                temp.append(f"{letter}|")

        return "\n".join(temp)

    else:
        return ""


class TestSimple(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(
            sort_vowels("Codewars"), "C|\n|o\nd|\n|e\nw|\n|a\nr|\ns|"
        )


if __name__ == "__main__":
    unittest.main()
