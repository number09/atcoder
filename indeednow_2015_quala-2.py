n = int(input())
li_in = list()
w = sorted('indeednow')
for i in range(n):
    li_in.append(input())

for l in li_in:
    if sorted(l) == w:
        print('YES')
    else:
        print('NO')

