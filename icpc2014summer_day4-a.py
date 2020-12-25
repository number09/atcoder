a, b, c = map(int, input().split())
for i in range(60):
    if ((60 * i) + c) % (a + b) <= a:
        print(c + 60 * i)
        exit(0)
print(-1)