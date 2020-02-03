x, k = map(int, input().split())

i = 1
while(True):
    if x < i * (10 ** k):
        print(i * (10 ** k))
        exit(0)
    else:
        i += 1
