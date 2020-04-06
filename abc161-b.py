n, m = map(int, input().split())
li_a = list(map(int, input().split()))
s = sum(li_a)

counter = 0
for a in li_a:
    if a >= (s / (4 * m)):
        counter += 1
if m <= counter:
    print('Yes')
else:
    print('No')
