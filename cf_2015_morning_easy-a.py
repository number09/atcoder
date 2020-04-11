n = int(input())

li_w = [x * x for x in range(1, 101)]

li_y = [y for y in li_w if n <= y]

print(li_y[0] - n)


