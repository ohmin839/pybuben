import sys
from sly import Lexer

class AybubenLexer(Lexer):
    tokens = {
        LARGE_A, LARGE_B, LARGE_C, LARGE_D, LARGE_E,
        LARGE_F, LARGE_G, LARGE_H, LARGE_I, LARGE_J,
        LARGE_K, LARGE_L, LARGE_M, LARGE_N, LARGE_O,
        LARGE_P, LARGE_Q, LARGE_R, LARGE_S, LARGE_T,
        LARGE_U, LARGE_V, LARGE_W, LARGE_X, LARGE_Y,
        LARGE_Z,
        
        SMALL_A, SMALL_B, SMALL_C, SMALL_D, SMALL_E,
        SMALL_F, SMALL_G, SMALL_H, SMALL_I, SMALL_J,
        SMALL_K, SMALL_L, SMALL_M, SMALL_N, SMALL_O,
        SMALL_P, SMALL_Q, SMALL_R, SMALL_S, SMALL_T,
        SMALL_U, SMALL_V, SMALL_W, SMALL_X, SMALL_Y,
        SMALL_Z,

        APOSTROPH, COMMA, PERIOD, QUESTION, EXCLAMATION,
        WHITESPACE, NEWLINE,
        DOLLAR,
    }

    LARGE_A = "A"
    LARGE_B = "B"
    LARGE_C = "C"
    LARGE_D = "D"
    LARGE_E = "E"
    LARGE_F = "F"
    LARGE_G = "G"
    LARGE_H = "H"
    LARGE_I = "I"
    LARGE_J = "J"
    LARGE_K = "K"
    LARGE_L = "L"
    LARGE_M = "M"
    LARGE_N = "N"
    LARGE_O = "O"
    LARGE_P = "P"
    LARGE_Q = "Q"
    LARGE_R = "R"
    LARGE_S = "S"
    LARGE_T = "T"
    LARGE_U = "U"
    LARGE_V = "V"
    LARGE_W = "W"
    LARGE_X = "X"
    LARGE_Y = "Y"
    LARGE_Z = "Z"

    SMALL_A = "a"
    SMALL_B = "b"
    SMALL_C = "c"
    SMALL_D = "d"
    SMALL_E = "e"
    SMALL_F = "f"
    SMALL_G = "g"
    SMALL_H = "h"
    SMALL_I = "i"
    SMALL_J = "j"
    SMALL_K = "k"
    SMALL_L = "l"
    SMALL_M = "m"
    SMALL_N = "n"
    SMALL_O = "o"
    SMALL_P = "p"
    SMALL_Q = "q"
    SMALL_R = "r"
    SMALL_S = "s"
    SMALL_T = "t"
    SMALL_U = "u"
    SMALL_V = "v"
    SMALL_W = "w"
    SMALL_X = "x"
    SMALL_Y = "y"
    SMALL_Z = "z"

    APOSTROPH = "'"
    COMMA = ","
    PERIOD = r"\."
    QUESTION = r"\?"
    EXCLAMATION = "!"

    WHITESPACE = "[ \t]"
    NEWLINE = "\r?\n"

    DOLLAR = r"\$"

    def error(self, t):
        print(f"Illegal character '{t.value[0]}'")
        self.index += 1

if __name__ == "__main__":
    lexer = AybubenLexer()
    for tok in lexer.tokenize(sys.argv[1]):
        print(f"type={tok.type}, value={tok.value}")

