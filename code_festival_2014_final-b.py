s = input()
print(sum(map(int, s[::2])) - sum(map(int, s[1::2])))
