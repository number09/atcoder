int_a, int_b, int_c, int_d = map(int,input().split())

range_a = range(int_a, int_b)
range_b = range(int_c, int_d)

print(len(set(range_a).intersection(set(range_b))))


