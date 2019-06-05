n = int(input())

syurui = set()

for _ in range(n):
    syurui.add(tuple(sorted(map(int, input().split()))))

print(len(syurui))
