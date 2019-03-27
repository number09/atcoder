b = input()

tpl = tuple(filter(lambda x: b in x, [('A', 'T'), ('C', 'G')]))[0]
print(tpl[0] if tpl[1] == b else tpl[1])

