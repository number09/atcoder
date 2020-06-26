x = int(input())

for i in range(1, 360 + 1):
    if i * x % 360 == 0:
        print(i)
        exit(0)
