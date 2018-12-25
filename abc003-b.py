s = input()
t = input()

for x, y in zip(s, t):
    if x == y:
        pass
    else:
        if x == '@' or y == '@':
            w = x if y == '@' else y
            if w in 'atcoder':
                pass
            else:
                print("You will lose")
                break
        else:
            print("You will lose")
            break
else:
    print("You can win")
