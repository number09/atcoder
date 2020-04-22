n = int(input())
li_a = list(map(int, input().split()))

dic = {}
for a in li_a:
    dic[a] = dic.get(a, 0) + 1

for i in range(1, n + 1):
    print(dic.get(i, 0))
