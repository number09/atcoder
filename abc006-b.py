n = int(input())

def trib(n):
    a, b, c = 0, 0, 1

    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        for i in range(n - 3):
            a, b, c = b, c, (a + b + c) % 10007
        return c

print(trib(n))

