h, w = map(int, input().split())

li_f = []
for _ in range(h):
    li_f.append(input())

answer = h * w
for w_num in range(1, h - 1):
    for b_num in range(1, h - w_num):
        r_num = h - w_num - b_num
        tmp = 0
        for a in li_f[:w_num]:
            tmp += w - a.count('W')
        for b in li_f[w_num:w_num + b_num]:
            tmp += w - b.count('B')
        for c in li_f[w_num + b_num:]:
            tmp += w - c.count('R')
        answer = min(answer, tmp)
print(answer)
