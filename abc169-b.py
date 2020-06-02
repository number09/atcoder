n = int(input())
li_a = list(map(int, input().split()))

if 0 in li_a:
    print(0)
    exit(0)
w = li_a[0]
for a in li_a[1:]:
    w = w * a
    if w > 10 ** 18:
        print(-1)
        exit(0)
else:
    print(w)
    exit(0)
