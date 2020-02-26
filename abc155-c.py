n = int(input())
moji = dict()
for i in range(n):
    s = input()
    moji[s] = moji.get(s, 0) + 1
max_cnt = max([value for value in moji.values()])
for key, value in sorted(moji.items(), key=lambda x: x[0]):
    if value == max_cnt:
        print(key)
