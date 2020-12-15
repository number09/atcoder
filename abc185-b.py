n, m, t = map(int, input().split())
li_ab = []
for _ in range(m):
    li_ab.append(list(map(int, input().split())))

w_n = n
before = 0
for ab in li_ab:
    w_n -= (ab[0] - before)

    if w_n <= 0:
        print('No')
        exit(0)
    before = ab[0]

    w_n = min(w_n + (ab[1] - before), n)
    before = ab[1]
else:
    w_n -= (t - before)
    if w_n <= 0:
        print('No')
        exit(0)
    print('Yes')
