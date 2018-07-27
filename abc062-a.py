int_x, int_y = map(int, input().split())

g_a = [1, 3, 5, 7, 8, 10, 12]
g_b = [4, 6, 9, 11]

if int_x in g_a and int_y in g_a:
    print("Yes")
elif int_x in g_b and int_y in g_b:
    print("Yes")
else:
    print("No")
