n = int(input())
answer = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        for w in range(2, i):
            if i % w == 0:
                break
        else:
            answer += 1
print(answer)
