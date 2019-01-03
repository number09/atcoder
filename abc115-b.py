n = int(input())
li_p = list()
for i in range(n):
    li_p.append(int(input()))

print(sum(p if idx != 0 else int(p/2) for idx, p in enumerate(sorted(li_p, reverse=True))))


