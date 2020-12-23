n = int(input())

li_aun = []
li_check = []
for _ in range(n):
    li_aun.append(input())

for a in li_aun:
    if a == 'A':
        li_check.append('A')
    else:
        if len(li_check) > 0:
            li_check.pop()
        else:
            print('NO')
            exit(0)

if len(li_check) > 0:
    print('NO')
else:
    print('YES')
