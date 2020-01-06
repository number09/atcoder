s = input()

w_s = s[::-1]

w_s = w_s.replace('b', '1')
w_s = w_s.replace('d', '2')
w_s = w_s.replace('p', '3')
w_s = w_s.replace('q', '4')

w_s = w_s.replace('1', 'd')
w_s = w_s.replace('2', 'b')
w_s = w_s.replace('3', 'q')
w_s = w_s.replace('4', 'p')

if s == w_s:
    print('Yes')
else:
    print('No')
