int_n = int(input())
int_d, int_x = map(int, input().split())

count = 0

array_a = []
for a in range(int_n):
    array_a.append(int(input()))


for a in array_a:
    count += len(set([(a * d) + 1 for d in range(int_d)]) & set([d + 1 for d in range(int_d)]))

print(count + int_x)
