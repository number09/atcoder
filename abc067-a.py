int_a, int_b = map(int, input().split())

if (int_a + int_b) % 3 == 0 or int_a % 3 == 0 or int_b % 3 == 0:
    print("Possible")
else:
    print("Impossible")
