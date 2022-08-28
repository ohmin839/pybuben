from sly import Lexer

class HayerenWordLexer(Lexer):
    tokens = (
        WORD,
        NEWLINE,
        ANYCHAR,
    )

    @_(f"[ԱԲԳԴԵԶԷԸԹԺԻԼԽԾԿՀՁՂՃՄՅՆՇՈՉՊՋՌՍՎՏՐՑՒՓՔՕՖՈաբգդեզէըթժիլխծկհձղճմյնշոչպջռսվտրցւփքօֆոև]+")
    def WORD(self, t):
        return t

    @_("\r?\n")
    def NEWLINE(self, t):
        pass

    @_(".")
    def ANYCHAR(self, t):
        pass

if __name__ == "__main__":
    import sys
    lexer = HayerenWordLexer()
    for tok in lexer.tokenize(sys.argv[1]):
        print(f"type={tok.type}, value={tok.value}")
