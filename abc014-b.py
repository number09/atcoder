n, X = map(int, input().split())
li_price = list(map(int, input().split()))

binx = format(X, 'b')

if len(binx) < n:
    binx = ((n - len(binx)) * '0') + binx

price_sum = 0
for p, b in zip(li_price, binx[::-1]):
    price_sum += p * int(b)

print(price_sum)
