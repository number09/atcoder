m, n, N = map(int, input().split())

answer = 0
used = 0
while True :
    answer += N
    used += N
    N = 0

    if used >= m:
        N += (used // m) * n
        used -= (used // m) * m
    else:
        break

print(answer)

