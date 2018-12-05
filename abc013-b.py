a = int(input())
b = int(input())

p1 = 0
p2 = 0
if a != b:
    if a < b:
        p1 = b - a
        p2 = a + 10 - b

    else:
        p1 = a - b
        p2 = b + 10 - a

    if p1 > p2:
        print(p2)
    else:
        print(p1)
else:
    print(0)

