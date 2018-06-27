int_x, int_a, int_b = map(int, input().split())

if abs(int_x - int_a) > abs(int_x - int_b):
    print("B")
else:
    print("A")