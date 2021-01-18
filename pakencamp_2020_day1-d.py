N, K = map(int, input().split())

if K < N:
    res = K**3
elif K < 2 * N:
    res = K**3 - 3 * (K - N)**3
elif K < 3 * N:
    res = N**3 * 6 - (3 * N - K)**3
else:
    res = N**3 * 6

print(res)
