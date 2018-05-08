int_n, int_a, int_b = map(int, input().split())

total = 0

for num in range(1, int_n + 1):

    if int_a <= sum([int(s) for s in list(str(num))]) <= int_b:
        total = total + num

print(total)

