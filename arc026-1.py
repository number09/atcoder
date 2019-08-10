n, a, b = map(int, input().split())

c_b = 0
c_a = 0

if n <= 5:
    c_b = n
elif n > 5 >= 0:
    c_b = 5

c_a = n - c_b

print(c_a * a + c_b * b)


