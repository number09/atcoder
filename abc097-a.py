int_a, int_b, int_c, int_d = map(int, input().split())

result = False

if abs(int_a - int_c) <= int_d:
    result = True
elif abs(int_a - int_b) <= int_d and abs(int_b - int_c) <= int_d:
    result = True

if result:
    print('Yes')
else:
    print('No')






