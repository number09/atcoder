int_t, int_a, int_b = map(int, input().split())

print(int_t * int_a if int_t * int_a <= int_b else int_b)

