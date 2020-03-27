s = input()
t = input()

if len(s) != len(t):
    print(-1)
elif s == t:
    print(0)
else:
    for i in range(len(s) + 1):
        wk = (s * 2)[-(len(s) + i):-1 * i]
        if wk == t:
            print(i)
            exit(0)
    else:
        print(-1)
