n, m, a, b = map(int, input().split())

li_c = list()
for _ in range(m):
    li_c.append(int(input()))

for idx, c in enumerate(li_c):
    if n <= a:
        n += b
    n -= c
    if n < 0:
        print(idx + 1)
        exit(0)
else:
    print("complete")


