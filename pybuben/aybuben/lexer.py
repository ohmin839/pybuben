import sys
from sly import Lexer

class AybubenLexer(Lexer):
    tokens = (
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


        COMMA, PERIOD, BACKQUOTE, COLON, HYPHEN,
        L_PARENTHESIS, R_PARENTHESIS,
        L_GUILLEMETS, R_GUILLEMETS,
        QUESTION, EXCLAMATION,
        WHITESPACE, NEWLINE,

        DOLLAR, DIGITS
    )

    @_("A")
    def LARGE_A(self, t):
        t.value = "\u0531"
        return t

    @_("B")
    def LARGE_B(self, t):
        t.value = "\u0532"
        return t

    @_("C[h']?")
    def LARGE_C(self, t):
        if t.value.endswith("h"):
            t.value = "\u0549"
        elif t.value.endswith("'"):
            t.value = "\u053E"
        else:
            t.value = "\u0551"
        return t

    @_("Dz?")
    def LARGE_D(self, t):
        if t.value.endswith("z"):
            t.value = "\u0541"
        else:
            t.value = "\u0534"
        return t

    @_("E'?")
    def LARGE_E(self, t):
        if t.value.endswith("'"):
            t.value = "\u0537"
        else:
            t.value = "\u0535"
        return t

    @_("F")
    def LARGE_F(self, t):
        t.value = "\u0556" 
        return t

    @_("Gh?")
    def LARGE_G(self, t):
        if t.value.endswith("h"):
            t.value = "\u0542"
        else:
            t.value = "\u0533"
        return t

    @_("H")
    def LARGE_H(self, t):
        t.value = "\u0540"
        return t

    @_("I")
    def LARGE_I(self, t):
        t.value = "\u053B"
        return t

    @_("J")
    def LARGE_J(self, t):
        t.value = "\u054B"
        return t

    @_("K")
    def LARGE_K(self, t):
        t.value = "\u053F"
        return t
        
    @_("L")
    def LARGE_L(self, t):
        t.value = "\u053C"
        return t

    @_("M")
    def LARGE_M(self, t):
        t.value = "\u0544"
        return t

    @_("N")
    def LARGE_N(self, t):
        t.value = "\u0546"
        return t

    @_("O")
    def LARGE_O(self, t):
        t.value = "\u0555"
        return t

    @_("P'?")
    def LARGE_P(self, t):
        if t.value.endswith("'"):
            t.value = "\u0553"
        else:
            t.value = "\u054A"
        return t

    @_("Q")
    def LARGE_Q(self, t):
        t.value = "\u0554"
        return t

    @_("Rr?")
    def LARGE_R(self, t):
        if t.value.endswith("r"):
            t.value = "\u054C"
        else:
            t.value = "\u0550"
        return t

    @_("Sh?")
    def LARGE_S(self, t):
        if t.value.endswith("h"):
            t.value = "\u0547"
        else:
            t.value = "\u054D"
        return t

    @_("T[w']?")
    def LARGE_T(self, t):
        if t.value.endswith("w"):
            t.value = "\u0543"
        elif t.value.endswith("'"):
            t.value = "\u0539"
        else:
            t.value = "\u054F"
        return t

    @_("U")
    def LARGE_U(self, t):
        t.value = "\u0548\u0582"
        return t

    @_("Vo?")
    def LARGE_V(self, t):
        if t.value.endswith("o"):
            t.value = "\u0548"
        else:
            t.value = "\u054E"
        return t

    @_("W")
    def LARGE_W(self, t):
        t.value = "\u0552"
        return t

    @_("X")
    def LARGE_X(self, t):
        t.value = "\u053D"
        return t
    
    @_("Y'?")
    def LARGE_Y(self, t):
        if t.value.endswith("'"):
            t.value = "\u0538"
        else:
            t.value = "\u0545"
        return t

    @_("Zh?")
    def LARGE_Z(self, t):
        if t.value.endswith("h"):
            t.value = "\u053A"
        else:
            t.value = "\u0536"
        return t


    @_("a")
    def SMALL_A(self, t):
        t.value = "\u0561"
        return t

    @_("b")
    def SMALL_B(self, t):
        t.value = "\u0562"
        return t

    @_("c[h']?")
    def SMALL_C(self, t):
        if t.value.endswith("h"):
            t.value = "\u0579"
        elif t.value.endswith("'"):
            t.value = "\u056E"
        else:
            t.value = "\u0581"
        return t

    @_("dz?")
    def SMALL_D(self, t):
        if t.value.endswith("z"):
            t.value = "\u0571"
        else:
            t.value = "\u0564"
        return t

    @_("e[v']?")
    def SMALL_E(self, t):
        if t.value.endswith("v"):
            t.value = "\u0587"
        elif t.value.endswith("'"):
            t.value = "\u0567"
        else:
            t.value = "\u0565"
        return t

    @_("f")
    def SMALL_F(self, t):
        t.value = "\u0586" 
        return t

    @_("gh?")
    def SMALL_G(self, t):
        if t.value.endswith("h"):
            t.value = "\u0572"
        else:
            t.value = "\u0563"
        return t

    @_("h")
    def SMALL_H(self, t):
        t.value = "\u0570"
        return t

    @_("i")
    def SMALL_I(self, t):
        t.value = "\u056B"
        return t

    @_("j")
    def SMALL_J(self, t):
        t.value = "\u057B"
        return t

    @_("k")
    def SMALL_K(self, t):
        t.value = "\u056F"
        return t

    @_("l")
    def SMALL_L(self, t):
        t.value = "\u056C"
        return t

    @_("m")
    def SMALL_M(self, t):
        t.value = "\u0574"
        return t

    @_("n")
    def SMALL_N(self, t):
        t.value = "\u0576"
        return t

    @_("o")
    def SMALL_O(self, t):
        t.value = "\u0585"
        return t

    @_("p'?")
    def SMALL_P(self, t):
        if t.value.endswith("'"):
            t.value = "\u0583"
        else:
            t.value = "\u057A"
        return t

    @_("q")
    def SMALL_Q(self, t):
        t.value = "\u0584"
        return t
    
    @_("rr?")
    def SMALL_R(self, t):
        if t.value == "rr":
            t.value = "\u057C"
        else:
            t.value = "\u0580"
        return t

    @_("sh?")
    def SMALL_S(self, t):
        if t.value.endswith("h"):
            t.value = "\u0577"
        else:
            t.value = "\u057D"
        return t

    @_("t[w']?")
    def SMALL_T(self, t):
        if t.value.endswith("w"):
            t.value = "\u0573"
        elif t.value.endswith("'"):
            t.value = "\u0569"
        else:
            t.value = "\u057F"
        return t

    @_("u")
    def SMALL_U(self, t):
        t.value = "\u0578\u0582"
        return t

    @_("vo?")
    def SMALL_V(self, t):
        if t.value.endswith("o"):
            t.value = "\u0578"
        else:
            t.value = "\u057E"
        return t

    @_("w")
    def SMALL_W(self, t):
        t.value = "\u0582"
        return t

    @_("x")
    def SMALL_X(self, t):
        t.value = "\u056D"
        return t

    @_("y'?")
    def SMALL_Y(self, t):
        if t.value.endswith("'"):
            t.value = "\u0568"
        else:
            t.value = "\u0575"
        return t

    @_("zh?")
    def SMALL_Z(self, t):
        if t.value.endswith("h"):
            t.value = "\u056A"
        else:
            t.value = "\u0566"
        return t


    @_(",")
    def COMMA(self, t):
        return t

    @_(r"\.")
    def PERIOD(self, t):
        return t

    @_("`")
    def BACKQUOTE(self, t):
        t.value = "\u055D"
        return t

    @_(":")
    def COLON(self, t):
        t.value = "\u0589"
        return t

    @_("-")
    def HYPHEN(self, t):
        return t

    @_(r"\(")
    def L_PARENTHESIS(self, t):
        return t

    @_(r"\)")
    def R_PARENTHESIS(self, t):
        return t

    @_("<<")
    def L_GUILLEMETS(self, t):
        t.value = "\u00AB"
        return t

    @_(">>")
    def R_GUILLEMETS(self, t):
        t.value = "\u00BB"
        return t

    @_(r"\?")
    def QUESTION(self, t):
        t.value = "\u055E"
        return t

    @_(r"!")
    def EXCLAMATION(self, t):
        t.value = "\u055C"
        return t


    @_("[ \t]")
    def WHITESPACE(self, t):
        return t

    @_("\r?\n")
    def NEWLINE(self, t):
        return t


    @_(r"\$")
    def DOLLAR(self, t):
        t.value = "\u058F"
        return t

    @_("[0-9]+")
    def DIGITS(self, t):
        return t


    def error(self, t):
        print(f"Illegal character '{t.value[0]}'")
        self.index += 1


if __name__ == "__main__":
    lexer = AybubenLexer()
    for tok in lexer.tokenize(sys.argv[1]):
        print(f"type={tok.type}, value={tok.value}")

