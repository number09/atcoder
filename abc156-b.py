n, k = map(int, input().split())
answer = 0
while True:
    if n // k != 0:
        n = n // k
        answer += 1
    else:
        break
print(answer + 1)
