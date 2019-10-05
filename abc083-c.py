x, y = map(int, input().split())

val = x
counter = 1

while val * 2 <= y:
    val = val * 2
    counter += 1

print(counter)

