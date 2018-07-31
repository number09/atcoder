int_n, int_k = map(int, input().split())

ar_int = list()

for i in range(int_n):
    int_a, int_b = map(int, input().split())
    for x in range(int_b):
        ar_int.append(int_a)

print(sorted(ar_int)[int_k - 1])
