import unittest
from parameterized import parameterized

from pybuben.core.api import to_hayeren_word_set
from ordered_set import OrderedSet

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
