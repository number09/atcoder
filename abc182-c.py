n = int(input())

tmp = sum([int(w) for w in str(n)])
if tmp % 3 == 0:
    print(0)
elif tmp % 3 == 1:

    if len([int(w) for w in str(n) if int(w) % 3 == 1]) >= 1:
        if len(str(n)) == 1:
            print(-1)
        else:
            print(1)
    else:
        if len(str(n)) == 2:
            print(-1)
        else:
            print(2)
else:
    if len([int(w) for w in str(n) if int(w) % 3 == 2]) >= 1:
        if len(str(n)) == 1:
            print(-1)
        else:
            print(1)
    else:
        if len(str(n)) == 2:
            print(-1)
        else:
            print(2)

