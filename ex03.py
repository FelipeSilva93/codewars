"""
Link desafio
https://www.codewars.com/kata/551dc350bf4e526099000ae5/train/python
"""

from unittest import TestCase


def song_decoder(song):
    new_song = song.replace("WUB", " ").split()
    return " ".join(new_song)


class TestSimple(TestCase):
    def test_wub_should_be_replaced_by_1_space(self):
        self.assertEqual(song_decoder("AWUBBWUBC"), "A B C")

    def test_multiples_wub_should_be_replaced_by_only_1_space(self):
        self.assertEqual(song_decoder("AWUBWUBWUBBWUBWUBWUBC"), "A B C")

    def test_heading_or_trailing_spaces_should_be_removed(self):
        self.assertEqual(song_decoder("WUBAWUBBWUBCWUB"), "A B C")
