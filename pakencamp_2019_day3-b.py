n = int(input())

li_s = list()

for i in range(n):
    li_s.append(input())

if li_s.count('black') > (n // 2):
    print('black')
else:
    print('white')
