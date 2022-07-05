import sys
from ordered_set import OrderedSet

from ..api import to_hayeren_word_set

def main():
    word_set = to_hayeren_word_set(sys.stdin)
    for word in word_set:
        print(word)

if __name__ == "__main__":
    main()

