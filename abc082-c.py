from collections import defaultdict

n = int(input())
li_a = input().split()

ndict = defaultdict(int)

for i in li_a:
    ndict[i] += 1

result = 0
for k in ndict.keys():
    if ndict[k] > int(k):
        result += ndict[k] - int(k)
    elif ndict[k] < int(k):
        result += ndict[k]

print(result)

