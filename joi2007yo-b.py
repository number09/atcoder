s_in = set()

for _ in range(28):
    s_in.add(int(input()))

for i in sorted(list(set(range(1, 31)).difference(s_in))):
    print(i)