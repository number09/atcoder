n = int(input())
s = input()

li_s = s.split('I')[1:-1]

for w_s in li_s:
    if 'O' in w_s:
        print('Yes')
        exit(0)
else:
    print('No')
