l, h = map(int, input().split())
n = int(input())
li_a = list()
for i in range(n):
    li_a.append(int(input()))

for w_a in li_a:
    if h < w_a:
        print("-1")
    elif l <= w_a <= h:
        print("0")
    else:
        print(l - w_a)





