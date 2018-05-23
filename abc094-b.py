int_n, int_m, int_x = map(int, input().split())

int_a_ar = list(map(int, input().split()))


to_start = len([x for x in int_a_ar if x < int_x])

to_end = len([x for x in int_a_ar if x > int_x])


cost = to_start if to_start < to_end else to_end

print(cost)
