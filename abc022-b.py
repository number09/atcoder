n = int(input())
li_a = list()
for i in range(n):
    li_a.append(int(input()))

print(len(li_a) - len(set(li_a)))

