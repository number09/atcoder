n = int(input())
li_a = list(map(int, input().split()))

d_a = {}

for s in range(n):
    num = 0
    goukei = 0
    for e in range(s, n):
        num += 1
        goukei += li_a[e]
        d_a[num] = max(d_a.get(num, 0), goukei)
for i in range(1, n + 1):
    print(d_a[i])

