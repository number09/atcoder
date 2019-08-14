n = int(input())
li_t = list()
for t in range(n):
    li_t.append(int(input()))

li_t.sort()
answer = sum(li_t)

for i in range(2 ** n):
    t1 = 0
    t2 = 0
    for m in range(n):
        if (i>>m) & 1:
            t1 += li_t[m]
        else:
            t2 += li_t[m]
    answer = min(answer, max(t1, t2))

print(answer)


