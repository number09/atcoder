n = int(input())

li_a = list(map(int, input().split()))

result = -1
for t in range(min(li_a), max(li_a) + 1):
    sum = 0
    for a in li_a:
        sum += (a - t)**2
    if result < 0:
        result = sum
    else:
        result = min(result, sum)

print(result)

