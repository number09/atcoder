n = int(input())
li_a = list(map(int, input().split()))

flg = False
nextval = 1
br = 0
for idx, a in enumerate(li_a):
    if a == nextval:
        nextval += 1
        flg = True
    else:
        br += 1
if flg:
    print(br)
else:
    print('-1')
