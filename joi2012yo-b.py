n = int(input())
d_score = {}

for i in range(n):
    d_score[i] = 0

for i in range((n * (n - 1)) // 2):
    a, b, c, d = map(int, input().split())

    if c == d:
        d_score[a - 1] += 1
        d_score[b - 1] += 1
    elif c > d:
        d_score[a - 1] += 3
    else:
        d_score[b - 1] += 3

sc = sorted([v for v in d_score.values()], reverse=True)

for i in range(n):
    print(sc.index(d_score[i]) + 1)
