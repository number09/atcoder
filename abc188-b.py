n = int(input())
li_a = list(map(int, input().split()))
li_b = list(map(int, input().split()))

su = 0
for a, b in zip(li_a, li_b):
    su += a * b
if su == 0:
    print('Yes')
else:
    print('No')

