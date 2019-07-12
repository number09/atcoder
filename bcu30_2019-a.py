n, k = map(int, input().split())
answer = 0
list_k = list()

for _ in range(n):
    list_k.append(int(input()))

single_key = sum(sorted(list_k, reverse=True)[:k])
double_key = sum(sorted(list_k, reverse=True)[k:]) * 2
print(single_key + double_key)




