n, w = map(int, input().split())

if n == 1:
    print(0)
else:
    for i in range(1, n + 1):
        if ((n - i) * w + i * (w - 1)) / (n - i) > w:
            print(n - i)
            exit(0)
    else:
        print(0)