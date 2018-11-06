a = int(input())

print(max([i * (a - i) for i in range(a + 1)]))
