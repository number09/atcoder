n = int(input())
li_a = []

for i in range(n):
    li_a.append(int(input()))

total = 0
count = 0
for a in sorted(li_a):
    if total < a:
        total += a
        count += 1
print(count)
