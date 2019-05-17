n, m = map(int, input().split())
li_a = list(map(int, input().split()))

sum = 0
colors = 0
for a in sorted(li_a, reverse=True):
    sum += a
    colors += 1
    if sum >= m:
        print(colors)
        exit(0)
else:
    print(n)
