x, y = map(int, input().split())
if y == 0:
    print('ERROR')
else:
    a = str(x / y)
    a_a, a_b = a.split('.')
    if len(a_b) == 1:
        a_b += '0'
    print(a_a + '.' + a_b[:2])

