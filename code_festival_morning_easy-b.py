n = int(input())

for i in range(5):
    if 1 + (40 * i) <= n <= 20 + (40 * i):
        w = n % 20
        if w == 0:
            print(20)
            exit(0)
        else:
            print(w)
            exit(0)
else:
    w = n % 20
    if w == 0:
        w = 20
    print(list(range(1, 21))[::-1].index(w) + 1)

