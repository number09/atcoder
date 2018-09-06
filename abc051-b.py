int_k, int_s = map(int, input().split())
counter = 0
for x in range(int_k + 1):
    for y in range(int_k + 1):
        if 0 <= int_s - (x + y) <= int_k:
            counter += 1

print(counter)
