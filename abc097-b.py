int_x = int(input())

result_b = 0
result_p = 0

for b in range(1, int_x + 1):

    for p in range(2, int_x + 1):

        if b ** p <= int_x:
            result_b, result_p = b, p
        else:
            break

print(result_b ** result_p)



