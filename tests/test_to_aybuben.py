import unittest
from parameterized import parameterized

from pybuben.api import to_aybuben

class ToAybubenTest(unittest.TestCase):
    @parameterized.expand([
        # large alphabet
        ["A", "Ա"],
        ["B", "Բ"],
        ["G", "Գ"],
        ["D", "Դ"],
        ["E", "Ե"],
        ["Z", "Զ"],
        ["E'", "Է"],
        ["Y'", "Ը"],
        ["T'", "Թ"],
        ["Zh", "Ժ"],
        ["I", "Ի"],
        ["L", "Լ"],
        ["X", "Խ"],
        ["C'", "Ծ"],
        ["K", "Կ"],
        ["H", "Հ"],
        ["Dz", "Ձ"],
        ["Gh", "Ղ"],
        ["Tw", "Ճ"],
        ["M", "Մ"],
        ["Y", "Յ"],
        ["N", "Ն"],
        ["Sh", "Շ"],
        ["Vo", "Ո"],
        ["Ch", "Չ"],
        ["P", "Պ"],
        ["J", "Ջ"],
        ["Rr", "Ռ"],
        ["S", "Ս"],
        ["V", "Վ"],
        ["T", "Տ"],
        ["R", "Ր"],
        ["C", "Ց"],
        ["W", "Ւ"],
        ["P'", "Փ"],
        ["Q", "Ք"],
        ["O", "Օ"],
        ["F", "Ֆ"],
        ["U", "ՈՒ"],
        # small alphabet
        ["a", "ա"],
        ["b", "բ"],
        ["g", "գ"],
        ["d", "դ"],
        ["e", "ե"],
        ["z", "զ"],
        ["e'", "է"],
        ["y'", "ը"],
        ["t'", "թ"],
        ["zh", "ժ"],
        ["i", "ի"],
        ["l", "լ"],
        ["x", "խ"],
        ["c'", "ծ"],
        ["k", "կ"],
        ["h", "հ"],
        ["dz", "ձ"],
        ["gh", "ղ"],
        ["tw", "ճ"],
        ["m", "մ"],
        ["y", "յ"],
        ["n", "ն"],
        ["sh", "շ"],
        ["vo", "ո"],
        ["ch", "չ"],
        ["p", "պ"],
        ["j", "ջ"],
        ["rr", "ռ"],
        ["s", "ս"],
        ["v", "վ"],
        ["t", "տ"],
        ["r", "ր"],
        ["c", "ց"],
        ["w", "ւ"],
        ["p'", "փ"],
        ["q", "ք"],
        ["o", "օ"],
        ["f", "ֆ"],
        ["u", "ու"],
        ["ev", "և"],
        # punctuation
        [",", ","],
        [".", "։"],
        ["?", "՞"],
        ["!", "՜"],
        # white space
        [" ", " "],
        ["\t", "\t"],
        # new line
        ["\n", "\n"],
        ["\r\n", "\r\n"],
        # others
        ["$", "֏"],
        ["", ""],
    ])
    def test_to_aybuben_characters(self, text, expected):
        actual = to_aybuben(text)
        self.assertEqual(expected, actual)

    @parameterized.expand([
        ["Barev.", "Բարև։"],
    ])
    def test_to_aybuben_wards(self, text, expected):
        actual = to_aybuben(text)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()

