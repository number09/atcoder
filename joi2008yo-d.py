m = int(input())
li_m = []
for _ in range(m):
    li_m.append(tuple(map(int, input().split())))

n = int(input())
li_n = []
for _ in range(n):
    li_n.append(tuple(map(int, input().split())))

a, b = li_m[0]

for w_n in li_n:
    w_a, w_b = w_n
    x = w_a - a
    y = w_b - b
    li_w = [(c[0] + x, c[1] + y) for c in li_m]
    for w in li_w:
        if w not in li_n:
            break
    else:
        print(x, y)
        exit(0)



