c11, c12, c13 = map(int, input().split())
c21, c22, c23 = map(int, input().split())
c31, c32, c33 = map(int, input().split())


for a1 in range(0, 101):
    b1 = c11 - a1
    b2 = c12 - a1
    b3 = c13 - a1
    a2 = c21 - b1
    a3 = c31 - b1

    if all([c22 == a2 + b2,
           c23 == a2 + b3,
           c32 == a3 + b2,
           c33 == a3 + b3]):
        print("Yes")
        exit(0)
else:
    print("No")
