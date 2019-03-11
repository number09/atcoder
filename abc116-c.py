n = int(input())

li_h = list(map(int, input().split()))

count = 0
for h in sorted(range(1, 101), reverse=True):
    now = 0
    for h_2 in li_h:
        if h_2 >= h and now < h:
            count += 1
        now = h_2

print(count)

