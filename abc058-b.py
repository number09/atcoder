str_o = input()
str_e = input()

print("".join(["".join([o, e]) for o, e in zip(str_o, str_e)]))
