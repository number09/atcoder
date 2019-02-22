int_x = int(input())

result = 0
for b in range(1, 100):

    for p in range(2, 10):

        if b ** p <= int_x:
            result = max(result, b ** p)
        else:
            break

print(result)



