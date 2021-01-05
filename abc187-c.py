n = int(input())
li_s = []
s_a = set()
s_b = set()
for _ in range(n):
    w = input()

    if w.startswith('!'):
        s_a.add(w[1:])
    else:
        s_b.add(w)
print(list(s_a.intersection(s_b))[0] if len(s_a.intersection(s_b)) > 0 else 'satisfiable')

