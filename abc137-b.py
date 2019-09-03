k, x = map(int, input().split())
right_idx_max = 0
left_idx = max(x - (k - 1), -1000000)

if left_idx == -1000000:
    right_idx = -1000000 + (k - 1)
else:
    right_idx = left_idx + (k - 1)


right_idx_max = right_idx + (k - 1)
print(" ".join(map(str, range(left_idx, right_idx_max + 1))))


