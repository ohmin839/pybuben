from ..converter.lexer  import AybubenLexer
from ..converter.parser import AybubenParser

def create_aybuben_converter():
    lexer  = AybubenLexer()
    parser = AybubenParser()
    def _convert(text):
        return parser.parse(lexer.tokenize(text))
    return _convert

