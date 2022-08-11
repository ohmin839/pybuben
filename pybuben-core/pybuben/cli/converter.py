import sys

from ..api import to_aybuben

def main():
    for line in sys.stdin:
        print(to_aybuben(line), end="")

if __name__ == "__main__":
    main()

