n = int(input())
s = input()

result = 'b'

li_addleft = ['a', 'c', 'b']
li_addright = ['c', 'a', 'b']

order = int((len(s) - 1) / 2) - 1


for i in range(order + 1):
    idx = int(i % 3)
    result = li_addleft[idx] + result + li_addright[idx]

if result == s:
    print(order + 1)
else:
    print('-1')