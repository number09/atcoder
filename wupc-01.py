n, m = map(int, input().split())

goukei = 0

for i in range(1, n + 1):
    goukei += i ** 2
print(goukei % m)