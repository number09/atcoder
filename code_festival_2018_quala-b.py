n, m, a, b = map(int, input().split())

set_a = set()
for i in range(m):
    l, r = map(int, input().split())
    for x in range(l, r + 1):
        set_a.add(x)
print(len(set_a) * a + (n - len(set_a)) * b)
