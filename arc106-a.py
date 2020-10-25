n = int(input())

for x in range(1, 38):
    for y in range(1, 26):
        if (3 ** x) + (5 ** y) == n:
            print(x, y)
            exit(0)
else:
    print(-1)