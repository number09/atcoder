int_n = int(input())

counter = 0
for n in range(1, int_n + 1):

    if len([n // m for m in range(1, n + 1) if (n % 2 != 0) and (n % m == 0)]) == 8 :
        counter += 1

print(counter)
