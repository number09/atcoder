int_n, int_m = map(int, input().split())

if int_n * 2 > int_m or int_n * 4 < int_m:
    print(-1, -1, -1)
    exit(0)
else:
    for b in range(2):
        for c in range(int_n - b + 1):
            a = int_n - c - b
            if a * 2 + b * 3 + c * 4 == int_m:
                print(a, b, c)
                exit(0)

    print(-1, -1, -1)


