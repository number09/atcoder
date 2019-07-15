y = int(input())

a = 0
b = 0
c = 0

if y % 4 == 0:
    a = 1

if y % 100 == 0:
    b = -1

if y % 400 == 0:
    c = 1

if a + b * 10 + c * 100 > 0:
    print("YES")
else:
    print("NO")
