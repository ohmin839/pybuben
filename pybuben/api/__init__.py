from ordered_set import OrderedSet
from ..converter.lexer  import AybubenLexer
from ..converter.parser import AybubenParser
from ..collector.lexer import HayerenWordLexer

def create_aybuben_converter():
    lexer  = AybubenLexer()
    parser = AybubenParser()
    def _convert(text):
        return parser.parse(lexer.tokenize(text))
    return _convert

to_aybuben = create_aybuben_converter()

def to_hayeren_words(text):
    lexer = HayerenWordLexer()
    return [token.value for token in lexer.tokenize(text)]

def to_hayeren_word_set(reader):
    word_set = OrderedSet()
    for line in reader:
        words = to_hayeren_words(line)
        word_set |= words
    return word_set