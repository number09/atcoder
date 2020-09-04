n, m = map(int, input().split())
li_l = list()

answer = list(map(str, range(1, n + 1)))

for _ in range(m):
    li_l.append(input())

keep = '0'
for l in li_l:
    if l == keep:
        pass
    else:
        idx = answer.index(l)
        li_f = answer[:idx]
        li_b = answer[idx + 1:]
        answer = li_f + [keep] + li_b
        keep = l
for w in answer:
    print(w)
