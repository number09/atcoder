int_n = int(input())
ar_int_a = list(map(int, input().split()))

max_a = max(ar_int_a)
result = []

for b in range(max_a * -1, max_a + 1):

    # print([abs(x - (b + i + 1)) for i, x in enumerate(ar_int_a)])
    result.append(sum([abs(x - (b + i + 1)) for i, x in enumerate(ar_int_a)]))

print(min(result))
