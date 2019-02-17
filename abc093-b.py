int_a, int_b, int_k = map(int, input().split())

minset = set(range(int_a, int_a + int_k))
maxset = set(range(int_b - int_k + 1, int_b + 1))

result = list(minset | maxset)
result.sort()
for i in result:
    if int_a <= i <= int_b:
        print(i)

