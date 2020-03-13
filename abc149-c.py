x = int(input())

while True:
    if any(x % i == 0 for i in range(2, (x // 2))):
        x += 1
    else:
        print(x)
        exit(0)
