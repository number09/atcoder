n = int(input())
counter = 0
w = n
while w <= 100:
    counter += 1
    w = w + n

print(100 - counter)