# pybuben-core
`pybuben-core` provides some CLIs and APIs.

This module heavily depends on [SLY](https://github.com/dabeaz/sly),
which is 100% python implementation of the lex and yacc tools.

## Conversion

### CLI
`pybubenconv` is a command to convert text from standard input in ASCII into Aybuben in Unicode.

```bash
$ echo 'Barev Dzez:' | pybubenconv
Բարև Ձեզ։

$ cat anthem_ascii.txt | pybubenconv
Մեր Հայրենիք, ազատ անկախ,
Որ ապրել է դարեդար
Յուր որդիքյ արդ կանչում են
Ազատ, անկախ Հայաստան։

Ահա եգբայր քեզ մի դրոշ,
Որ իմ ձեռքով գործեցի
Գիշերներյ ես քուն չեգայ,
Արզասուքով լվացի։

Նայիր նրան՝ երեք գոյնով,
Նուիրական մեր նսջան
Թոգ փեգփոգի թշնամու դեմ
Թոգ միսպտ պանծայ Հայաստան։

Ամենայն տեգ մահը մի է
Մարդ մի անգամ պիտ մեռնի,
Բայց երանի՝ որ յուր ազգի
Ազատության կզոհվի։
```

### API
You can also use `to_aybuben` function as API.

```python
from pybuben.api import to_aybuben

converted = to_aybuben('Barev Dzez:')
print(converted) # Բարև Ձեզ։
```

### Conversion rules

#### Upper cases
| Input(ASCII) | Output(Unicode) |
| ------------ | --------------- |
| `A` | `Ա` |
| `B` | `Բ` |
| `G` | `Գ` |
| `D` | `Դ` |
| `E` | `Ե` |
| `Z` | `Զ` |
| `E'` | `Է` |
| `Y'` | `Ը` |
| `T'` | `Թ` |
| `Zh` | `Ժ` |
| `I` | `Ի` |
| `L` | `Լ` |
| `X` | `Խ` |
| `C'` | `Ծ` |
| `K` | `Կ` |
| `H` | `Հ` |
| `Dz` | `Ձ` |
| `Gh` | `Ղ` |
| `Tw` | `Ճ` |
| `M` | `Մ` |
| `Y` | `Յ` |
| `N` | `Ն` |
| `Sh` | `Շ` |
| `Vo` | `Ո` |
| `Ch` | `Չ` |
| `P` | `Պ` |
| `J` | `Ջ` |
| `Rr` | `Ռ` |
| `S` | `Ս` |
| `V` | `Վ` |
| `T` | `Տ` |
| `R` | `Ր` |
| `C` | `Ց` |
| `W` | `Ւ` |
| `P'` | `Փ` |
| `Q` | `Ք` |
| `O` | `Օ` |
| `F` | `Ֆ` |
| `U` | `Ու` |

#### Lower cases
| Input(ASCII) | Output(Unicode) |
| ------------ | --------------- |
| `a` | `ա` |
| `b` | `բ` |
| `g` | `գ` |
| `d` | `դ` |
| `e` | `ե` |
| `z` | `զ` |
| `e'` | `է` |
| `y'` | `ը` |
| `t'` | `թ` |
| `zh` | `ժ` |
| `i` | `ի` |
| `l` | `լ` |
| `x` | `խ` |
| `c'` | `ծ` |
| `k` | `կ` |
| `h` | `հ` |
| `dz` | `ձ` |
| `gh` | `ղ` |
| `tw` | `ճ` |
| `m` | `մ` |
| `y` | `յ` |
| `n` | `ն` |
| `sh` | `շ` |
| `vo` | `ո` |
| `ch` | `չ` |
| `p` | `պ` |
| `j` | `ջ` |
| `rr` | `ռ` |
| `s` | `ս` |
| `v` | `վ` |
| `t` | `տ` |
| `r` | `ր` |
| `c` | `ց` |
| `w` | `ւ` |
| `p'` | `փ` |
| `q` | `ք` |
| `o` | `օ` |
| `f` | `ֆ` |
| `u` | `ու` |
| `ev` | `և` |

#### Others
| Input(ASCII) | Output(Unicode) |
| ------------ | --------------- |
| `$` | `֏` |
| `0123456789` | `0123456789` |
| `,` | `,` |
| `.` | `.` |
| `` ` `` | `՝` |
| `:` | `։` |
| `-` | `-` |
| `(` | `(` |
| `)` | `)` |
| `<<` | `«` |
| `>>` | `»` |
| `?` | `՞` |
| `!` | `՛` |
| `!~` | `՜` |
| `␣` | `␣` |
| `\t` | `\t` |
| `\n` | `\n` |
| `\r\n` | `\r\n` |

## Collection 

### CLI
`pybubencoll` is a command to list words uniquely from text written in Armenian.

```bash
$ cat anthem_ascii.txt | pybubenconv | pybubencoll
Մեր
Հայրենիք
ազատ
անկախ
...
```

### API
`to_hayeren_words` function extracts Armenian words from texts:
```python
from pybuben.api import to_aybuben
from pybuben.api import to_hayeren_words

converted = to_aybuben('Barev Dzez:')
words = to_hayeren_words(converted)
print(words) # ['Բարև', 'Ձեզ']
```

`to_hayeren_word_set` function is the same as `to_hayeren_words`
except that it extracts words uniquely(case-sensitive).
```python
from pybuben.api import to_aybuben
from pybuben.api import to_hayeren_word_set

converted = to_aybuben('Barev Dzez, Barev dzez:')
word_set = to_hayeren_word_set(converted)
print(word_set) # OrderedSet(['Բարև', 'Ձեզ', 'ձեզ'])
```

`to_hayeren_word_dict` is the same as `to_hayeren_word_set` function
except that its return values are dictionaries, not sets.
```python
from pybuben.api import to_aybuben
from pybuben.api import to_hayeren_word_dict

converted = to_aybuben('Barev Dzez, Barev dzez:')
word_dict = to_hayeren_word_dict(converted)
print(word_dict) # {'Բարև': 2, 'Ձեզ': 1, 'ձեզ': 1}
```

## External resources
- Armenian Alphabet (https://en.wikipedia.org/wiki/Armenian_alphabet)
- Romanization of Armenian (https://en.wikipedia.org/wiki/Romanization_of_Armenian)
