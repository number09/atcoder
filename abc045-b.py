li_a = list(input())
li_b = list(input())
li_c = list(input())


def play(name):
    if name == 'A':
        current = li_a
    elif name =='B':
        current = li_b
    else:
        current = li_c

    if len(current) > 0:
        drop = current.pop(0)
        play(str(drop).upper())

    else:
        print(name)
        exit(0)

play("A")


