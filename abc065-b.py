int_n = int(input())
ar_int = list()
for i in range(int_n):
    ar_int.append(int(input()))

target = 2
counter = 0

while counter < int_n:
    if target in ar_int:
        target = ar_int.index(target) + 1
        counter += 1
        if target == 1:
            print(counter)
            exit(0)
print(-1)