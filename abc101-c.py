import math

int_n, int_k = map(int, input().split())
ar_int_a = list(map(int, input().split()))

idx_minimum = ar_int_a.index(min(ar_int_a))
left = math.ceil(idx_minimum / (int_k - 1)) if idx_minimum != 0 else 0
right = math.ceil((int_n - (idx_minimum + 1)) / (int_k - 1)) if idx_minimum != (int_n - 1) else 0

print(left + right)
