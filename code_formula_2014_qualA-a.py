a = int(input())

for i in range(1, a + 1):
    if i * i * i == a:
        print('YES')
        exit(0)
else:
    print('NO')
