int_count = int(input())
int_arr = list(map(int, input().split()))

result = 0
number = 1

stop = False

while True:
    for num in int_arr:
        if num % 2 == 1:
            stop = True
            break
    if stop:
        break
    else:
        result = result + 1
        for i, v in enumerate(int_arr):
            int_arr[i] = v/2


print(result)



