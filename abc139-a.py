s = input()
t = input()

print([x == y for x, y in zip(s, t)].count(True))