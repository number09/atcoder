int_n = int(input())

array = [2, 1]

for i in range(int_n - 1):
    array.append(array[i] + array[i+1])

print(array[-1])

