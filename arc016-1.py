n, m = map(int, input().split())

s_w = set(range(1, n + 1))
s_w.remove(m)
print(list(s_w)[0])