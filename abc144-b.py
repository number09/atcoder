n = int(input())

if n in [x * y for x in range(1, 10) for y in range(1, 10)]:
    print("Yes")
else:
    print("No")
