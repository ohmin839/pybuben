import unittest
from parameterized import parameterized
from ordered_set import OrderedSet

from pybuben.api import to_hayeren_word_set

class ToHayerenWords(unittest.TestCase):
    @parameterized.expand([
        ["", []],
        ["Բարև Ձեզ։", OrderedSet(["Բարև", "Ձեզ"])],
        ["Բարև Ձեզ, Բարև ձեզ։", OrderedSet(["Բարև", "Ձեզ", "ձեզ"])],
    ])
    def test_to_hayeren_word_set(self, text, expected):
        actual = to_hayeren_word_set(text)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
