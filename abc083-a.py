int_a, int_b, int_c, int_d = map(int, input().split())

if int_a + int_b == int_c + int_d:
    print("Balanced")
elif int_a + int_b > int_c + int_d:
    print("Left")
else:
    print("Right")

