from ..collector.lexer import HayerenWordLexer

def to_hayeren_words(text):
    lexer = HayerenWordLexer()
    return [token.value for token in lexer.tokenize(text)]

def to_hayeren_word_set(reader):
    word_set = OrderedSet()
    for line in reader:
        words = to_hayeren_words(line)
        word_set |= words
    return word_set

def to_hayeren_word_dict(reader):
    word_dict = dict()
    for line in reader:
        words = to_hayeren_words(line)
        for word in words:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1

