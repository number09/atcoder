s = input()

adds = 0


def check(o, r):
    if o == r:
        return True
    elif o == '*' or r == '*':
        return True
    else:
        return False

while(True):
    wk = s + '*' * adds
    r_wk = wk[::-1]

    if all([check(o, r) for o, r in zip(wk, r_wk)]):
        print(adds)
        exit(0)
    else:
        adds += 1




