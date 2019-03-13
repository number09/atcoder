from collections import defaultdict

n, k = map(int, input().split())

ddict = defaultdict(int)
li_a = list(input().split())

for a in li_a:
    ddict[a] += 1

counter = 0
for w in sorted(ddict, key=lambda x: ddict[x], reverse=True)[k:]:
    counter += ddict[w]

print(counter)
