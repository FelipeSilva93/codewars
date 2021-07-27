"""
link desafio
https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python
"""

import unittest


def likes(names=[]):

    if len(names) == 0:
        return "no one likes this"

    elif len(names) == 1:
        return f"{names[0]} likes this"

    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"

    elif len(names) > 1 and len(names) <= 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"

    elif len(names) >= 4:
        x = len(names)
        return f"{names[0]}, {names[1]} and {x-2} others like this"


class TestSimple(unittest.TestCase):
    def test_likes_with_no_likes(self):
        self.assertEqual(likes([]), "no one likes this")

    def test_likes_with_one_like(self):
        self.assertEqual(likes(["Peter"]), "Peter likes this")

    def test_likes_with_three_or_more_likes(self):
        self.assertEqual(likes(["Max", "John", "Mark"]), "Max, John and Mark like this")

    def test_likes_with_four_or_more_likes_should_return_ans_special_message(self):
        self.assertEqual(
            likes(["Alex", "Jacob", "Mark", "Max"]),
            "Alex, Jacob and 2 others like this",
        )

    def test_likes_with_two_likes(self):
        self.assertEqual(likes(["Jacob", "Alex"]), "Jacob and Alex like this")
