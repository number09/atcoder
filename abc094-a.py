int_a, int_b, int_x = map(int, input().split())


if int_a <= int_x <= int_a + int_b:
    print("YES")
else:
    print("NO")
