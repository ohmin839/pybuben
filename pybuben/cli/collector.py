import sys
from ordered_set import OrderedSet

from ..api import into_hayeren_words

def main():
    word_set = OrderedSet()
    for line in sys.stdin:
        words = into_hayeren_words(line)
        word_set |= words
    for word in word_set:
        print(word)

if __name__ == "__main__":
    main()

