int_a, int_b = map(int, input().split())

count = 0

for m in range(1,int_a + 1):
    for d in range(1, int_b + 1):
        if m == d:
            count += 1

print(count)

