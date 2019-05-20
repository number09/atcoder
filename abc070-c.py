n = int(input())
li_t = list()

for _ in range(n):
    li_t.append(int(input()))

li_sorted = sorted(li_t, reverse=True)
t_max = li_sorted.pop(0)


sec = 1
while(True):
    if all(map(lambda x: (t_max * sec) % x == 0, li_sorted)):
        print(sec * t_max)
        exit(0)
    else:
        sec += 1


