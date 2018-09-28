n = int(input())
k = int(input())
x = int(input())
y = int(input())

stay_k = n if k > n else k
stay_after = (n - k) if n > k else 0

print(stay_k * x + stay_after * y)

