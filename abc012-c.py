n = int(input())

zan = 2025 - n

for a in range(1, 10):
    for b in range(1, 10):
        if a * b == zan:
            print("{0} x {1}".format(a, b))
        elif a * b > zan:
            break


