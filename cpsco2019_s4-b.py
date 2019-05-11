n, d = map(int, input().split())
li_s = list()

for _ in range(d):
    li_s.append(input())

li_w = list()
for a in range(d):
    li_temp = list()
    for i in range(n):
        if li_s[a][i] == "o":
            li_temp.append(i)
    li_w.append(li_temp)



answer = 0
for x in range(len(li_w)):
    for y in range(len(li_w)):
        answer = max(len(set(li_w[x]).union(set(li_w[y]))), answer)
print(answer)




