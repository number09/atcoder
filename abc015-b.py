import math
n = int(input())
bugs = list(map(int, input().split()))
apps = list(filter(lambda x: x != 0, bugs))

print(math.ceil(sum(apps) / len(apps)))

