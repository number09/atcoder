n = int(input())
li_x = list(map(int, input().split()))

answer = sum([x ** 2 for x in li_x])
for p in range(min(li_x),max(li_x) + 1):
    answer = min(answer, sum([(x - p) ** 2 for x in li_x]))

print(answer)
