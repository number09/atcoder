int_n = int(input())

if int_n in [4 * k + 7 * d for k in range(101) for d in range(101)]:
    print("Yes")
else:
    print("No")

