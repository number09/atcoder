from collections import defaultdict
str_s = input()
str_t = input()


def check_pattern(str):
    checkdict = defaultdict(int)
    pattern = list()
    for w in str:
        if w not in checkdict:
            checkdict[w] = len(checkdict) + 1

        pattern.append(checkdict[w])
    return pattern


if check_pattern(str_s) == check_pattern(str_t):
    print("Yes")
else:
    print("No")


