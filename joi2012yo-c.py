import math

n = int(input())
a, b = map(int, input().split())
c = int(input())
li_i = []

for _ in range(n):
    li_i.append(int(input()))

ans = []

for i in range(n):
    ans.append(
        (c + sum(sorted(li_i, reverse=True)[:i])) / (a + (b * i))
    )
print(math.floor(max(ans)))

