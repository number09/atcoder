h, n = map(int, input().split())
li_a = list(map(int, input().split()))

if sum(li_a) >= h:
    print('Yes')
else:
    print('No')
