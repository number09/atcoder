int_n = int(input())
ar_int = list()
for i in range(int_n):
    ar_int.append(int(input()))

target = 1
counter = 0

while counter < int_n:
    target = ar_int[target - 1]
    counter += 1
    if target == 2: # button 2
        print(counter)
        exit(0)
print(-1)