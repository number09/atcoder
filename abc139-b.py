a, b = map(int, input().split())

counter = 1
tap = 0

while counter < b:
    tap += 1
    counter = counter - 1 + a
print(tap)