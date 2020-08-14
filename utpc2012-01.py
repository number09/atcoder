s = input()

s = s.replace('/', '')
if sorted(s[:4]) == sorted(s[4:]):
    print('yes')
else:
    print('no')