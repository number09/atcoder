s, p = map(int, input().split())

for i in range(1, 1000050):
    if i * (s - i) == p:
        print('Yes')
        exit(0)
else:
    print('No')