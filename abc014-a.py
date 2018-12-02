a = int(input())
b = int(input())

if a % b != 0:
    print(((a // b) + 1) * b - a)
else:
    print(0)
