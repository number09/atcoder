n, p = map(int, input().split())
li_a = list(map(int, input().split()))

li_a = [a for a in li_a if a != 1]

for i in range(len(li_a)):
    answer = None
    # for a in li_a[i:]:
    for a in range(i, len(li_a)):
        if answer is None:
            answer = li_a[a]
        else:
            answer *= li_a[a]
        if answer == p:
            print('Yay!')
            exit(0)
        if answer > p:
            break
else:
    print(':(')

