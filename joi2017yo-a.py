a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if 0 <= a < b:
    if a == 0:
        print(d + (b - a) * e)
    else:
        print((b - a) * e)
elif a < 0 < b:
    print(b * e + abs(a) * c + d)
else: # a < b < 0
    print((b - a) * c)

