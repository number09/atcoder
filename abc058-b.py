from itertools import zip_longest
str_o = input()
str_e = input()

print("".join(["".join([o, e]) for o, e in zip_longest(str_o, str_e, fillvalue="")]))
