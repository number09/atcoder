n = int(input())
li_a = map(int, input().split())
li_a_left = list()
total = 0
for l in li_a:
    if len(li_a_left) == 0:
        li_a_left.append(l)
    else:
        li_a_left.append(li_a_left[-1] + l)
    total += l

print(min(abs(left - (total - left)) for left in li_a_left))



