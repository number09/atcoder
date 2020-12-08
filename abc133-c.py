l, r = map(int, input().split())

answer = 2018

for i in range(l, r):
    for x in range(i + 1, r + 1):
        answer = min(answer, (i * x) % 2019)
        if answer == 0:
            print(0)
            exit(0)
print(answer)

