int_a, int_b = map(int, input().split())

ar = []

ar.append(int_a + int_b)
ar.append(int_a - int_b)
ar.append(int_a * int_b)

print(max(ar))

