int_n = int(input())

counter = 0
for i in range(int_n):
    int_s, int_e = map(int, input().split())
    counter += (int_e - int_s + 1)

print(counter)