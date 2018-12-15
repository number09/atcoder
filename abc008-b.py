n = int(input())

li_s = list()
for i in range(n):
    li_s.append(input())

vote = [(name, li_s.count(name)) for name in set(li_s)]

print(sorted(vote, key=lambda x: x[1], reverse=True)[0][0])



