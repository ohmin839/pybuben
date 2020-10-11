from sly import Parser

from .lexer import AybubenLexer

class AybubenParser(Parser):
    tokens = AybubenLexer.tokens

    @_("")
    def text(self, p):
        return ""

    @_("letters")
    def text(self, p):
        return "".join(p.letters)

    @_("letter")
    def letters(self, p):
        return [p.letter]

    @_("letters letter")
    def letters(self, p):
        p.letters.append(p.letter)
        return p.letters

    @_(
        "LARGE_A", "LARGE_B", "LARGE_C", "LARGE_D", "LARGE_E",
        "LARGE_F", "LARGE_G", "LARGE_H", "LARGE_I", "LARGE_J",
        "LARGE_K", "LARGE_L", "LARGE_M", "LARGE_N", "LARGE_O",
        "LARGE_P", "LARGE_Q", "LARGE_R", "LARGE_S", "LARGE_T",
        "LARGE_U", "LARGE_V", "LARGE_W", "LARGE_X", "LARGE_Y",
        "LARGE_Z",

        "SMALL_A", "SMALL_B", "SMALL_C", "SMALL_D", "SMALL_E",
        "SMALL_F", "SMALL_G", "SMALL_H", "SMALL_I", "SMALL_J",
        "SMALL_K", "SMALL_L", "SMALL_M", "SMALL_N", "SMALL_O",
        "SMALL_P", "SMALL_Q", "SMALL_R", "SMALL_S", "SMALL_T",
        "SMALL_U", "SMALL_V", "SMALL_W", "SMALL_X", "SMALL_Y",
        "SMALL_Z",

        "COMMA", "PERIOD", "BACKQUOTE", "COLON", "HYPHEN",
        "L_PARENTHESIS", "R_PARENTHESIS",
        "L_GUILLEMETS", "R_GUILLEMETS",
        "QUESTION", "EXCLAMATION",
        "WHITESPACE", "NEWLINE",
        "DOLLAR", "DIGITS",
    )
    def letter(self, p):
        return p[0]

if __name__ == "__main__":
    import sys

    lexer = AybubenLexer()
    parser = AybubenParser()
    result = parser.parse(lexer.tokenize(sys.argv[1]))

    print(result)

