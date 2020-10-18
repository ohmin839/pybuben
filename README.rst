===================================
Pybuben
===================================

Pybuben is a tool for writing text in Armenian alphabet(*aybuben*).
**CAUTION: This is a work in progress.**


Requirements
===================================

Pybuben heavily depends on `SLY <https://github.com/dabeaz/sly>`_,
which is 100% python implementation of the lex and yacc tools.
SLY requires the use of Python 3.6 or greator(so does Pybuben).


Examples
===================================

As API, use ``to_aybuben`` function:

.. code:: python

    from pybuben.api import to_aybuben

    result = to_aybuben("Barev Dzez:")
    print(result) # Բարև Ձեզ։


As CLI, use ``pybconv`` command:

.. code::

    $ echo "Barev Dzez:" | pybconv    
    Բարև Ձեզ։


An another ``pybconv`` example:

.. code::

    $ cat anthem.txt
    Mer Hayreniq, azat ankax,
    Vor aprel e' daredar
    Yur vordiqy ard kanchum en
    Azat, ankax Hayastan:

    Aha eghbayr qez mi drvosh,
    Vor im dzerrqvov gvorc'eci
    Gishernery es qun cheghay,
    Arzasuqvov lvaci:

    Nayir nran` ereq gvoynvov,
    Nuirakan mer nsjan
    T'vogh p'eghp'voghi t'shnamu dem
    T'vogh mispt panc'ay Hayastan:

    Amenayn tegh mahy' mi e'
    Mard mi angam pit merrni,
    Bayc erani` vor yur azgi
    Azatut'yan kzvohvi:


    $ cat anthem.txt | pybconv
    Մեր Հայրենիք, ազատ անկախ,
    Որ ապրել է դարեդար
    Յուր որդիքյ արդ կանչում են
    Ազատ, անկախ Հայաստան։

    Ահա եղբայր քեզ մի դրոշ,
    Որ իմ ձեռքով գործեցի
    Գիշերներյ ես քուն չեղայ,
    Արզասուքով լվացի։

    Նայիր նրան՝ երեք գոյնով,
    Նուիրական մեր նսջան
    Թող փեղփողի թշնամու դեմ
    Թող միսպտ պանծայ Հայաստան։

    Ամենայն տեղ մահը մի է
    Մարդ մի անգամ պիտ մեռնի,
    Բայց երանի՝ որ յուր ազգի
    Ազատության կզոհվի։


Conversion Rules
===================================

Pybuben converts ASCII characters into Unicodes.

Upper cases
-----------------------------------

.. csv-table::
    :header: Input(ASCII), Output(Unicode)

    ``A``, ``Ա``
    ``B``, ``Բ``
    ``G``, ``Գ``
    ``D``, ``Դ``
    ``E``, ``Ե``
    ``Z``, ``Զ``
    ``E'``, ``Է``
    ``Y'``, ``Ը``
    ``T'``, ``Թ``
    ``Zh``, ``Ժ``
    ``I``, ``Ի``
    ``L``, ``Լ``
    ``X``, ``Խ``
    ``C'``, ``Ծ``
    ``K``, ``Կ``
    ``H``, ``Հ``
    ``Dz``, ``Ձ``
    ``Gh``, ``Ղ``
    ``Tw``, ``Ճ``
    ``M``, ``Մ``
    ``Y``, ``Յ``
    ``N``, ``Ն``
    ``Sh``, ``Շ``
    ``Vo``, ``Ո``
    ``Ch``, ``Չ``
    ``P``, ``Պ``
    ``J``, ``Ջ``
    ``Rr``, ``Ռ``
    ``S``, ``Ս``
    ``V``, ``Վ``
    ``T``, ``Տ``
    ``R``, ``Ր``
    ``C``, ``Ց``
    ``W``, ``Ւ``
    ``P'``, ``Փ``
    ``Q``, ``Ք``
    ``O``, ``Օ``
    ``F``, ``Ֆ``
    ``U``, ``Ու``

Lower cases
-----------------------------------

.. csv-table::
    :header: Input(ASCII), Output(Unicode)

    ``a``, ``ա``
    ``b``, ``բ``
    ``g``, ``գ``
    ``d``, ``դ``
    ``e``, ``ե``
    ``z``, ``զ``
    ``e'``, ``է``
    ``y'``, ``ը``
    ``t'``, ``թ``
    ``zh``, ``ժ``
    ``i``, ``ի``
    ``l``, ``լ``
    ``x``, ``խ``
    ``c'``, ``ծ``
    ``k``, ``կ``
    ``h``, ``հ``
    ``dz``, ``ձ``
    ``gh``, ``ղ``
    ``tw``, ``ճ``
    ``m``, ``մ``
    ``y``, ``յ``
    ``n``, ``ն``
    ``sh``, ``շ``
    ``vo``, ``ո``
    ``ch``, ``չ``
    ``p``, ``պ``
    ``j``, ``ջ``
    ``rr``, ``ռ``
    ``s``, ``ս``
    ``v``, ``վ``
    ``t``, ``տ``
    ``r``, ``ր``
    ``c``, ``ց``
    ``w``, ``ւ``
    ``p'``, ``փ``
    ``q``, ``ք``
    ``o``, ``օ``
    ``f``, ``ֆ``
    ``u``, ``ու``
    ``ev``, ``և``

Punctuation marks
-----------------------------------

.. csv-table::
    :header: Input(ASCII), Output(Unicode)
    :delim: space

    ``,`` ``,``
    ``.`` ``.``
    ````` ``՝``
    ``:`` ``։``
    ``-`` ``-``
    ``(`` ``(``
    ``)`` ``)``
    ``<<`` ``«``
    ``>>`` ``»``
    ``?`` ``՞``
    ``!`` ``՜``

White spaces
-----------------------------------

.. csv-table::
    :header: Input(ASCII), Output(Unicode)

    ``␣``, ``␣``
    ``\t``, ``\t``

New lines
-----------------------------------

.. csv-table::
    :header: Input(ASCII), Output(Unicode)

    ``\n``, ``\n``
    ``\r\n``, ``\r\n``


Others
-----------------------------------

.. csv-table::
    :header: Input(ASCII), Output(Unicode)

    ``$``, ``֏``
    ``1234567890``, ``1234567890``


Resources
===================================

-  Armenian Alphabet (https://en.wikipedia.org/wiki/Armenian_alphabet)

-  Romanization of Armenian (https://en.wikipedia.org/wiki/Romanization_of_Armenian)

