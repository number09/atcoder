int_a, int_b = map(int, input().split())

if (int_a + int_b) % 3 == 0:
    print("Possible")
else:
    print("Impossible")
