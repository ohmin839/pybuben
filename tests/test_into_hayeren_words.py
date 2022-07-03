import unittest
from parameterized import parameterized

from pybuben.api import into_hayeren_words

class IntoHayerenWords(unittest.TestCase):
    @parameterized.expand([
        ["", []],
        ["Բարև Ձեզ։", ["Բարև", "Ձեզ"]]
    ])
    def test_to_hayeren_words(self, text, expected):
        actual = into_hayeren_words(text)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
