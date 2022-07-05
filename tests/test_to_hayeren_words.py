import unittest
from parameterized import parameterized

from pybuben.api import to_hayeren_words

class ToHayerenWords(unittest.TestCase):
    @parameterized.expand([
        ["", []],
        ["Բարև Ձեզ։", ["Բարև", "Ձեզ"]]
    ])
    def test_to_hayeren_words(self, text, expected):
        actual = to_hayeren_words(text)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
