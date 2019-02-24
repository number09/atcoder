n, m = map(int, input().split())

li_m = list()

for i in range(n):
    li_m = li_m + input().split()[1:]

counter = 0
for m in set(li_m):
    if li_m.count(m) == n:
        counter += 1
print(counter)