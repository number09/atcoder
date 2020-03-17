n, m = map(int, input().split())
li_in = list()
s = ['x'] * n
for i in range(m):
    li_in.append(list(map(int, input().split())))

for l in li_in:
    idx = l[0]
    val = str(l[1])
    target_idx = idx - 1
    if s[target_idx] == 'x':
        s[target_idx] = val
    elif s[target_idx] == val:
        pass
    else:
        print(-1)
        exit(0)
if n > 1:
    if s[0] == '0':
        print(-1)
        exit(0)
    elif s[0] == 'x':
        s[0] = '1'

print(int(''.join(s).replace('x', '0')))


