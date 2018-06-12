int_n = int(input())

if int_n % sum([int(s) for s in str(int_n)]) == 0:
    print("Yes")
else:
    print("No")
