n, t = map(int, input().split())

li_a = list()
for i in range(n):
    li_a.append(int(input()))

last_open = (0, 0)
t_seconds = 0

for a in li_a:
    if last_open[0] <= a <= last_open[1]:
        t_seconds += a + t - last_open[1]
        last_open = (last_open[0], t + a)
    else:
        t_seconds += t
        last_open = (a, a + t)
print(t_seconds)
