int_n = int(input())

for i in reversed(range(8)):
    result = 2 ** i
    if result <= int_n:
        print(result)
        exit(0)