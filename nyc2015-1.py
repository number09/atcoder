n = int(input())
w = (bin(n))[2:]

if w == w[::-1]:
    print('Yes')
else:
    print('No')
