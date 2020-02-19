a, b, c = map(int, input().split())


if a % 2 != 0 or b % 2 != 0 or c % 2 != 0:
    print(0)
    exit(0)
if a == b == c and a % 2 == 0:
    print(-1)
    exit(0)

counter = 0
while True:
    counter += 1
    w_a = a / 2
    w_b = b / 2
    w_c = c / 2

    a = w_b + w_c
    b = w_a + w_c
    c = w_b + w_a

    if a % 2 == 1 or b % 2 == 1 or c % 2 == 1:
        print(counter)
        exit(0)
