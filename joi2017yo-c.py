n, m, d = map(int, input().split())

li_d = []
answer = 0
for _ in range(n):
    li_d.append(input())
for r in range(n):
    for c in range(m):
        # 縦方向
        w_t = []
        for t in range(r, min(r + d, n)):
            w_t.append(li_d[t][c])
        # print(w_t)
        if len(w_t) == d and '#' not in w_t:
            answer += 1
        # 横方向
        w_y = []
        for y in range(c, min(c + d, m)):
            w_y.append(li_d[r][y])
        # print(w_y)
        if len(w_y) == d and '#' not in w_y:
            answer += 1
print(answer)
