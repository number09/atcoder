n = int(input())
li_b = list(map(int, input().split()))
li_a = [9999999] * n

for idx, b in enumerate(li_b):
    li_a[idx] = min(li_a[idx], b)
    li_a[idx + 1] = min(li_a[idx + 1], b)

print(sum(li_a))
