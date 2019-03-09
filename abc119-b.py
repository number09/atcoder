n = int(input())

result = 0
for i in range(n):
    x, y = input().split()
    if y == "BTC":
        result += float(x) * 380000
    else:
        result += int(x)
print(result)
