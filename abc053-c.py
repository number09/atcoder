int_x = int(input())

# 6,5,6..と繰り返すのが最短？
count = 0

count = (int_x // 11) * 2

if int_x % 11 != 0:
    if (int_x % 11) > 6:
        count += 2
    else:
        count += 1


print(count)
