x = int(input())

w = 0
for i in range(1, x + 1):
    w += i
    if w >= x:
        print(i)
        exit(0)
