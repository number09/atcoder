import itertools
s = input()
gx, gy = map(int, input().split())

if gx == 0 and gx == 0:
    print('Yes')
    exit(0)

for w, x, y, z in itertools.permutations(['L', 'R', 'U', 'D'], 4):
    posx = 0
    posy = 0

    for word in s:
        command = ''
        if word == 'W':
            command = w
        elif word == 'X':
            command = x
        elif word == 'Y':
            command = y
        else:
            command = z

        if command == 'L':
            posx -= 1
        elif command == 'R':
            posx += 1
        elif command == 'U':
            posy += 1
        else:
            posy -= 1

        if posx == gx and posy == gy:
            print('Yes')
            exit(0)
else:
    print('No')

