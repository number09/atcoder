int_a, int_b = map(int, input().split())

int_a = int_a if int_a != 1 else 20
int_b = int_b if int_b != 1 else 20

if int_a > int_b:
    print("Alice")
elif int_a < int_b:
    print("Bob")
else:
    print("Drow")

