c1, a = input().split()
c2, b = input().split()

if c1 == c2:
    print(int(abs(int(a) - int(b)) / 15))
else:
    print(int((abs(int(a)) + abs(int(b)))/ 15))

