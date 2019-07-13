n = int(input())

li_in = list()

for _ in range(n):
    li_in.append(input().split())

answer = sum([int(a[1]) for a in filter(lambda x: x[0] == "+", li_in)])

for b in [int(a[1]) for a in filter(lambda x: x[0] == "*" and x[1] != "0", li_in)]:
    answer *= b

print(answer)
