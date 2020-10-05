import unittest
from parameterized import parameterized

from pybuben.api import to_aybuben

class ToAybubenTest(unittest.TestCase):
    @parameterized.expand([
        ["", ""],

        [" ", " "],
        ["\t", "\t"],
        ["\n", "\n"],
        ["\r\n", "\r\n"],
    ])
    def test_to_aybuben(self, text, expected):
        actual = to_aybuben(text)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
