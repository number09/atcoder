x = int(input())

w = x // 100
y = x % 100

if w * 5 >= y:
    print(1)
else:
    print(0)
