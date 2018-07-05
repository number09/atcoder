int_n = int(input())

bin_number = format(int_n, 'b')

bin_sum = sum(list(map(int, list(str(bin_number)))))

if int_n % bin_sum == 0:
    print("Yes")
else:
    print("No")

