int_n = int(input())

power = 1

for i in range(1, int_n + 1):
    power = (power * i) % (10 ** 9 + 7)

print(power)
