int_a, int_b, int_k = map(int, input().split())

ar = list(range(int_a, int_b + 1))

minset = set(ar[:int_k])
maxset = set(ar[int_k * -1:])

result = list(minset | maxset)
result.sort()
print(result)

