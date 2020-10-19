import math

n = int(input())
li_x = list(map(int, input().split()))

ans_a = sum([abs(x) for x in li_x])
ans_b = math.sqrt(sum([abs(x) ** 2 for x in li_x]))
ans_c = max([abs(x) for x in li_x])

print(ans_a)
print(ans_b)
print(ans_c)
