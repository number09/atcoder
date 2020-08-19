from itertools import permutations

n = int(input())
li_s = []
for _ in range(n):
    li_s.append(input())

print(sorted([''.join(p) for p in permutations(li_s, 2)])[0])
