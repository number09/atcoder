int_a = int(input())
int_b = int(input())
int_c = int(input())
int_d = int(input())

result = (int_a if int_a <= int_b else int_b) + \
         (int_c if int_c <= int_d else int_d)

print(result)
