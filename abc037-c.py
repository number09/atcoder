n, k = map(int, input().split())

li_input = list(map(int, input().split()))

result = 0

for idx, v in enumerate(li_input, 1):
    if idx < k:
        result += v * idx
    elif (n - idx + 1) < k:
        result += v * (n - idx + 1)
    else:
        result += v * k

print(result)

