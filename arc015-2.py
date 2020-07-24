n = int(input())
li_a = [0, 0, 0, 0, 0, 0]
for i in range(n):
    mx, mi = map(float, input().split())

    if mx >= 35:
        li_a[0] += 1
    if 35 > mx >= 30:
        li_a[1] += 1
    if 30 > mx >= 25:
        li_a[2] += 1
    if mi >= 25:
        li_a[3] += 1
    if mi < 0 and mx >= 0:
        li_a[4] += 1
    if mx < 0:
        li_a[5] += 1

print(" ".join([str(v) for v in li_a]))
