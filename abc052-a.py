int_a, int_b, int_c, int_d = map(int, input().split())

print(int_a * int_b if int_a * int_b >= int_c * int_d else int_c * int_d)