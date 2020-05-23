a, b, c = map(int, input().split())

li_a = [a, b, c]

if li_a.count(1) >= 2:
    print('1')
else:
    print('2')
