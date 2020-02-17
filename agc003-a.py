s = input()

if not(s.count('N') > 0 and s.count('S') > 0 or
       s.count('N') == 0 and s.count('S') == 0):
    print('No')
elif not(s.count('W') > 0 and s.count('E') > 0 or
       s.count('W') == 0 and s.count('E') == 0):
    print('No')
else:
    print('Yes')

