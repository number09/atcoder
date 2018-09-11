import math

int_n, int_x = map(int, input().split())
li_pos = list(map(int, input().split()))

li_pos.sort()
if len(li_pos) == 1:
    print(abs(li_pos[0] - int_x))
else:
    print(math.gcd(*[abs(li_pos[i] - li_pos[i + 1]) for i in range(len(li_pos) - 1)]))

