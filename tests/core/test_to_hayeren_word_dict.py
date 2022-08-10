import unittest
from parameterized import parameterized

from pybuben.core.api import to_hayeren_word_dict

class ToHayerenWords(unittest.TestCase):
    @parameterized.expand([
        ["", {}],
        ["Բարև Ձեզ։", {"Բարև": 1, "Ձեզ": 1}],
        ["Բարև Ձեզ, Բարև ձեզ։", { "Բարև": 2, "Ձեզ": 1, "ձեզ": 1 }],
    ])
    def test_to_hayeren_word_dict(self, text, expected):
        actual = to_hayeren_word_dict(text)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
