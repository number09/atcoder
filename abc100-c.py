int_n = int(input())

input_array = list(map(int, input().split()))

counter = 0

while True:
    templist = list(filter(lambda x: x % 2 == 0, input_array))
    if len(templist) != 0:
        max_even = max(filter(lambda x: x % 2 == 0, input_array))
        even_index = input_array.index(max_even)

        input_array = list(map(lambda x: x[1] if x[0] != even_index else x[1] / 2, enumerate(input_array)))
        print(input_array)

        counter += 1

    else:
        break

print(counter)



