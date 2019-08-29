x, y = map(int, input().split())
k = int(input())

if y < k:
    print(y + (x - (k - y)))

else:
    print(x + k)


