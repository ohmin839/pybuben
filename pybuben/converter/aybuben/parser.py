from sly import Parser

from .lexer import AybubenLexer

class AybubenParser(Parser):
    tokens = AybubenLexer.tokens

    @_("")
    def letters(self, p):
        return ""

    @_("letter")
    def letters(self, p):
        return p.letter

    @_("letters letter")
    def letters(self, p):
        return "".join(p.letters) + p.letter


    @_("alphabet",
        "punctuation",
        "whitespace",
        "newline",
        "others",)
    def letter(self, p):
        return p[0]
    
    
    @_("large_alphabet",
        "small_alphabet")
    def alphabet(self, p):
        return p[0]

    @_("large_ayb",
        "large_ben",
        "large_gim",
        "large_da",
        "large_ech",
        "large_za",
        "large_eh",
        "large_et",
        "large_to",
        "large_zhe",
        "large_ini",
        "large_liwn",
        "large_xeh",
        "large_ca",
        "large_ken",
        "large_ho",
        "large_ja",
        "large_ghad",
        "large_cheh",
        "large_men",
        "large_yi",
        "large_now",
        "large_sha",
        "large_vo",
        "large_cha",
        "large_peh",
        "large_jheh",
        "large_ra",
        "large_seh",
        "large_vew",
        "large_tiwn",
        "large_reh",
        "large_co",
        "large_yiwn",
        "large_piwr",
        "large_keh",
        "large_oh",
        "large_feh",
        "large_vo_yiwn")
    def large_alphabet(self, p):
        return p[0]

    @_("LARGE_A")
    def large_ayb(self, p):
        return "\u0531"

    @_("LARGE_B")
    def large_ben(self, p):
        return "\u0532"

    @_("LARGE_G")
    def large_gim(self, p):
        return "\u0533"

    @_("LARGE_D")
    def large_da(self, p):
        return "\u0534"

    @_("LARGE_E")
    def large_ech(self, p):
        return "\u0535"

    @_("LARGE_Z")
    def large_za(self, p):
        return "\u0536"

    @_("LARGE_E APOSTROPH")
    def large_eh(self, p):
        return "\u0537"

    @_("LARGE_Y APOSTROPH")
    def large_et(self, p):
        return "\u0538"

    @_("LARGE_T APOSTROPH")
    def large_to(self, p):
        return "\u0539"

    @_("LARGE_Z SMALL_H")
    def large_zhe(self, p):
        return "\u053A"

    @_("LARGE_I")
    def large_ini(self, p):
        return "\u053B"

    @_("LARGE_L")
    def large_liwn(self, p):
        return "\u053C"

    @_("LARGE_X")
    def large_xeh(self, p):
        return "\u053D"

    @_("LARGE_C APOSTROPH")
    def large_ca(self, p):
        return "\u053E"

    @_("LARGE_K")
    def large_ken(self, p):
        return "\u053F"

    @_("LARGE_H")
    def large_ho(self, p):
        return "\u0540"

    @_("LARGE_D SMALL_Z")
    def large_ja(self, p):
        return "\u0541"

    @_("LARGE_G SMALL_H")
    def large_ghad(self, p):
        return "\u0542"

    @_("LARGE_T SMALL_W")
    def large_cheh(self, p):
        return "\u0543"

    @_("LARGE_M")
    def large_men(self, p):
        return "\u0544"

    @_("LARGE_Y")
    def large_yi(self, p):
        return "\u0545"

    @_("LARGE_N")
    def large_now(self, p):
        return "\u0546"

    @_("LARGE_S SMALL_H")
    def large_sha(self, p):
        return "\u0547"

    @_("LARGE_V SMALL_O")
    def large_vo(self, p):
        return "\u0548"

    @_("LARGE_C SMALL_H")
    def large_cha(self, p):
        return "\u0549"

    @_("LARGE_P")
    def large_peh(self, p):
        return "\u054A"

    @_("LARGE_J")
    def large_jheh(self, p):
        return "\u054B"

    @_("LARGE_R SMALL_R")
    def large_ra(self, p):
        return "\u054C"

    @_("LARGE_S")
    def large_seh(self, p):
        return "\u054D"

    @_("LARGE_V")
    def large_vew(self, p):
        return "\u054E"

    @_("LARGE_T")
    def large_tiwn(self, p):
        return "\u054F"

    @_("LARGE_R")
    def large_reh(self, p):
        return "\u0550"

    @_("LARGE_C")
    def large_co(self, p):
        return "\u0551"

    @_("LARGE_W")
    def large_yiwn(self, p):
        return "\u0552"

    @_("LARGE_P APOSTROPH")
    def large_piwr(self, p):
        return "\u0553"

    @_("LARGE_Q")
    def large_keh(self, p):
        return "\u0554"

    @_("LARGE_O")
    def large_oh(self, p):
        return "\u0555"

    @_("LARGE_F")
    def large_feh(self, p):
        return "\u0556"

    @_("LARGE_U")
    def large_vo_yiwn(self, p):
        return "\u0548\u0552"


    @_("small_ayb",
        "small_ben",
        "small_gim",
        "small_da",
        "small_ech",
        "small_za",
        "small_eh",
        "small_et",
        "small_to",
        "small_zhe",
        "small_ini",
        "small_liwn",
        "small_xeh",
        "small_ca",
        "small_ken",
        "small_ho",
        "small_ja",
        "small_ghad",
        "small_cheh",
        "small_men",
        "small_yi",
        "small_now",
        "small_sha",
        "small_vo",
        "small_cha",
        "small_peh",
        "small_jheh",
        "small_ra",
        "small_seh",
        "small_vew",
        "small_tiwn",
        "small_reh",
        "small_co",
        "small_yiwn",
        "small_piwr",
        "small_keh",
        "small_oh",
        "small_feh",
        "small_ech_yiwn",
        "small_vo_yiwn")
    def small_alphabet(self, p):
        return p[0]

    @_("SMALL_A")
    def small_ayb(self, p):
        return "\u0561"

    @_("SMALL_B")
    def small_ben(self, p):
        return "\u0562"

    @_("SMALL_G")
    def small_gim(self, p):
        return "\u0563"

    @_("SMALL_D")
    def small_da(self, p):
        return "\u0564"

    @_("SMALL_E")
    def small_ech(self, p):
        return "\u0565"

    @_("SMALL_Z")
    def small_za(self, p):
        return "\u0566"

    @_("SMALL_E APOSTROPH")
    def small_eh(self, p):
        return "\u0567"

    @_("SMALL_Y APOSTROPH")
    def small_et(self, p):
        return "\u0568"

    @_("SMALL_T APOSTROPH")
    def small_to(self, p):
        return "\u0569"

    @_("SMALL_Z SMALL_H")
    def small_zhe(self, p):
        return "\u056A"

    @_("SMALL_I")
    def small_ini(self, p):
        return "\u056B"

    @_("SMALL_L")
    def small_liwn(self, p):
        return "\u056C"

    @_("SMALL_X")
    def small_xeh(self, p):
        return "\u056D"

    @_("SMALL_C APOSTROPH")
    def small_ca(self, p):
        return "\u056E"

    @_("SMALL_K")
    def small_ken(self, p):
        return "\u056F"

    @_("SMALL_H")
    def small_ho(self, p):
        return "\u0570"

    @_("SMALL_D SMALL_Z")
    def small_ja(self, p):
        return "\u0571"

    @_("SMALL_G SMALL_H")
    def small_ghad(self, p):
        return "\u0572"

    @_("SMALL_T SMALL_W")
    def small_cheh(self, p):
        return "\u0573"

    @_("SMALL_M")
    def small_men(self, p):
        return "\u0574"

    @_("SMALL_Y")
    def small_yi(self, p):
        return "\u0575"

    @_("SMALL_N")
    def small_now(self, p):
        return "\u0576"

    @_("SMALL_S SMALL_H")
    def small_sha(self, p):
        return "\u0577"

    @_("SMALL_V SMALL_O")
    def small_vo(self, p):
        return "\u0578"

    @_("SMALL_C SMALL_H")
    def small_cha(self, p):
        return "\u0579"

    @_("SMALL_P")
    def small_peh(self, p):
        return "\u057A"

    @_("SMALL_J")
    def small_jheh(self, p):
        return "\u057B"

    @_("SMALL_R SMALL_R")
    def small_ra(self, p):
        return "\u057C"

    @_("SMALL_S")
    def small_seh(self, p):
        return "\u057D"

    @_("SMALL_V")
    def small_vew(self, p):
        return "\u057E"

    @_("SMALL_T")
    def small_tiwn(self, p):
        return "\u057F"

    @_("SMALL_R")
    def small_reh(self, p):
        return "\u0580"

    @_("SMALL_C")
    def small_co(self, p):
        return "\u0581"

    @_("SMALL_W")
    def small_yiwn(self, p):
        return "\u0582"

    @_("SMALL_P APOSTROPH")
    def small_piwr(self, p):
        return "\u0583"

    @_("SMALL_Q")
    def small_keh(self, p):
        return "\u0584"

    @_("SMALL_O")
    def small_oh(self, p):
        return "\u0585"

    @_("SMALL_F")
    def small_feh(self, p):
        return "\u0586"

    @_("SMALL_U")
    def small_vo_yiwn(self, p):
        return "\u0578\u0582"

    @_("SMALL_E SMALL_V")
    def small_ech_yiwn(self, p):
        return "\u0587"


    @_("comma",
        "period",
        "question",
        "exclamation")
    def punctuation(self, p):
        return p[0]
        
    @_("COMMA")
    def period(self, p):
        return ","
        
    @_("PERIOD")
    def comma(self, p):
        return "\u0589"

    @_("QUESTION")
    def question(self, p):
        return "\u055E"

    @_("EXCLAMATION")
    def exclamation(self, p):
        return "\u055C"


    @_("WHITESPACE")
    def whitespace(self, p):
        return p[0]
        

    @_("NEWLINE")
    def newline(self, p):
        return p[0]
        

    @_("dram")
    def others(self, p):
        return p[0]
        
    @_("DOLLAR")
    def dram(self, p):
        return "\u058F"

