int_a, int_b = map(int, input().split())

diff = int_b - int_a
high_b = sum(range(1, diff + 1))

print(high_b - int_b)
