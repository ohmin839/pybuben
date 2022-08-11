import io
from ..collector.lexer import HayerenWordLexer
from ordered_set import OrderedSet

def to_hayeren_words(text):
    lexer = HayerenWordLexer()
    return [token.value for token in lexer.tokenize(text)]

def to_stringio(func):
    def decorator(arg):
        if type(arg) == str:
            return func(io.StringIO(arg))
        else:
            return func(arg)
    return decorator

@to_stringio
def to_hayeren_word_set(reader):
    word_set = OrderedSet()
    for line in reader:
        words = to_hayeren_words(line)
        word_set |= words
    return word_set

@to_stringio
def to_hayeren_word_dict(reader):
    word_dict = dict()
    for line in reader:
        words = to_hayeren_words(line)
        for word in words:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
    return word_dict
