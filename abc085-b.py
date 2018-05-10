int_n = int(input())
int_array = []

for d in range(int_n):
    int_array.append(int(input()))

int_set = set(int_array)

print(len(int_set))
