n = input()

start = n[0]

if all([start >= i for i in n]):
    print(n[0] * len(n))
else:
    print((str(int(n[0]) + 1)) * len(n))

