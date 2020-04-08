n, k = map(int, input().split())
amari = n % k
print(min(amari, abs(amari - k)))
