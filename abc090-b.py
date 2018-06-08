int_a, int_b = map(int, input().split())

count = 0
for i in range(int_a, int_b + 1):
    if i == int(str(i)[::-1]):
        count += 1

print(count)
