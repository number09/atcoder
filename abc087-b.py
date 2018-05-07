int_a = int(input())
int_b = int(input())
int_c = int(input())
int_x = int(input())

int_pattern = 0

for a in range(int_a + 1):
    for b in range(int_b + 1):
        for c in range(int_c + 1):
            if 500 * a + 100 * b + 50 * c == int_x:
                int_pattern = int_pattern + 1

print(int_pattern)



