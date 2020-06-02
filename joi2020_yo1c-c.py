n = int(input())
li_a = list(map(int, input().split()))
answer = 0
for s in range(n):
    l = 1
    wk = li_a[s]
    for e in range(s, n):
        if s == e:
            continue
        if wk <= li_a[e]:
            wk = li_a[e]
            l += 1
        else:
            break
    answer = max(answer, l)
print(answer)

