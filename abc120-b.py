a, b, k = map(int, input().split())

counter = 0
for i in sorted(range(1, min(a, b) + 1), reverse=True):
    if a % i == 0 and b % i == 0:
        counter += 1
        if counter == k:
            print(i)
            exit(0)


