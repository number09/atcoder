s = input()

x = 'ADOPQR'

if 'B' not in s:
    if s[0] not in x and s[1] not in x and s[2] in x and s[3] not in x:
        print('yes')
    else:
        print('no')
else:
    print('no')
