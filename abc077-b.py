int_n = int(input())

result = 0

for i in range(int_n + 1):
    if i ** 2 <= int_n:
        result = i**2
    else:
        break
print(result)

