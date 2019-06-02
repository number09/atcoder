n = int(input())

maxnum = 0

for _ in range(n):
    maxnum = max(maxnum, sum(map(int, input().split())))

print(maxnum)
