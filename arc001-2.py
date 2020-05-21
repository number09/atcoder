a, b = map(int, input().split())
answer = 0
li_p = [1, 5, 10, -1, -5, -10]
if a == b:
    print(0)
    exit(0)

while True:
    li_w = [abs(b - (a + w)) for w in li_p]
    mi = min(li_w)
    best_idx = li_w.index(mi)
    a += li_p[best_idx]
    answer += 1
    if a == b:
        print(answer)
        exit(0)
