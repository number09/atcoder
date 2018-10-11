n = int(input())
seito = [(idx + 1, val) for idx, val in enumerate(map(int, input().split()))]

for s in sorted(seito, key=lambda x: x[1], reverse=True):
    print(s[0])
