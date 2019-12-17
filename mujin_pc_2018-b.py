a = int(input())
s = input()
if a == 0:
    print('Yes')
    exit(0)
for w in s:
    if w == '+':
        a += 1
    else:
        a -= 1
    if a == 0:
        print('Yes')
        exit(0)
else:
    print('No')
