s = input()

if all(w in ('R', 'U', 'D') for w in s[::2]) and \
        all(w in ('L', 'U', 'D') for w in s[1::2]):
    print("Yes")
else:
    print("No")
