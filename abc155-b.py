n = int(input())
li_a = list(map(int, input().split()))

for a in li_a:
    if a % 2 == 0:
        if a % 3 == 0 or a % 5 == 0:
            pass
        else:
            print('DENIED')
            exit(0)
else:
    print('APPROVED')
