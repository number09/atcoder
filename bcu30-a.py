n, k = map(int, input().split())
li_a = list(map(int, input().split()))

pos = 0

for a in li_a:
    if pos + a == n:
        print(n)
        exit(0)
    elif pos + a < n:
        pos += a
    else:  # pos + a > n:
        pos = n - abs(pos + a - n)
print(pos)

