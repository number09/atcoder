n, k = map(int, input().split())

li_t = list()

for _ in range(n):
    li_t.append(int(input()))

for i in range(2, n):
    if sum(li_t[i - 2:i + 1]) < k:
        print(i + 1)
        exit(0)
else:
    print(-1)



