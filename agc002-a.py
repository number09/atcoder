a, b = map(int, input().split())

if a <= 0 <= b:
    print('Zero')
else:
    if b < 0:
        if (abs(a + b) + 1) % 2 == 0:
            print('Positive')
        else:
            print('Negative')
    else:
        print('Positive')
