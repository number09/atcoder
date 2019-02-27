int_n = int(input())

ar_int_a = []
for i in range(int_n):
    ar_int_a.append(int(input()))

numbers = set(ar_int_a)
written = [i for i in numbers if ar_int_a.count(i) % 2 == 1]
print(len(written))
