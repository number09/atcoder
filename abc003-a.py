n = int(input())

print(int(sum(i * 10000 for i in range(1, n + 1)) / n))