int_x, int_a, int_b = map(int, input().split())

if int_a >= int_b:
    print("delicious")
elif int_a + int_x >= int_b:
    print("safe")
else:
    print("dangerous")

